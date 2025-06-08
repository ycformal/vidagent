import torch
import io, tokenize
from PIL import Image
from transformers import (OwlViTProcessor, OwlViTForObjectDetection, AutoProcessor, BlipForQuestionAnswering, TvpForVideoGrounding, AutoModelForCausalLM, Blip2Processor, Blip2ForConditionalGeneration, Qwen2_5_VLForConditionalGeneration, LlavaNextVideoProcessor, LlavaNextVideoForConditionalGeneration)
from nltk.stem import PorterStemmer
import nltk
from .clustering import cluster
import av
import gc

from vis_utils import html_embed_image, html_colored_span, vis_masks
import openai
import json
import numpy as np

from llava.model.builder import load_pretrained_model
from llava.mm_utils import tokenizer_image_token
from llava.constants import DEFAULT_IMAGE_TOKEN, IMAGE_TOKEN_INDEX
from llava.conversation import conv_templates
import copy
import re
from qwen_vl_utils import process_vision_info
from sentence_transformers import SentenceTransformer, util

import threading

gpu_lock = threading.Lock()

nltk.download('punkt_tab') # If there's error message, just modify the package name according to what the error message says

def parse_step(step_str,partial=False):
    tokens = list(tokenize.generate_tokens(io.StringIO(step_str).readline))
    output_var = tokens[0].string
    step_name = tokens[2].string
    parsed_result = dict(
        output_var=output_var,
        step_name=step_name)
    if partial:
        return parsed_result

    arg_tokens = [token for token in tokens[4:-3] if token.string not in [',','=']]
    num_tokens = len(arg_tokens) // 2
    args = dict()
    for i in range(num_tokens):
        args[arg_tokens[2*i].string] = arg_tokens[2*i+1].string
    parsed_result['args'] = args
    return parsed_result


def html_step_name(content):
    step_name = html_colored_span(content, 'red')
    return f'<b>{step_name}</b>'


def html_output(content):
    output = html_colored_span(content, 'green')
    return f'<b>{output}</b>'


def html_var_name(content):
    var_name = html_colored_span(content, 'blue')
    return f'<b>{var_name}</b>'


def html_arg_name(content):
    arg_name = html_colored_span(content, 'darkorange')
    return f'<b>{arg_name}</b>'

    
class EvalInterpreter():
    step_name = 'EVAL'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        step_input = eval(parse_result['args']['expr'])
        assert(step_name==self.step_name)
        return step_input, output_var
    
    def html(self,eval_expression,step_input,step_output,output_var):
        eval_expression = eval_expression.replace('{','').replace('}','')
        step_name = html_step_name(self.step_name)
        var_name = html_var_name(output_var)
        output = html_output(step_output)
        expr = html_arg_name('expression')
        return f"""<div>{var_name}={step_name}({expr}="{eval_expression}")={step_name}({expr}="{step_input}")={output}</div>"""

    def execute(self,prog_step,inspect=False):
        step_input, output_var = self.parse(prog_step)
        prog_state = dict()
        for var_name,var_value in prog_step.state.items():
            if isinstance(var_value,str):
                if var_value in ['yes','no']:
                    prog_state[var_name] = var_value=='yes'
                elif var_value.isdecimal():
                    prog_state[var_name] = var_value
                else:
                    prog_state[var_name] = f"'{var_value}'"
            else:
                prog_state[var_name] = var_value
        
        eval_expression = step_input

        if 'xor' in step_input:
            step_input = step_input.replace('xor','!=')

        step_input = step_input.format(**prog_state)
        step_output = eval(step_input)
        prog_step.state[output_var] = step_output
        if inspect:
            html_str = self.html(eval_expression, step_input, step_output, output_var)
            return step_output, html_str

        return step_output


class ResultInterpreter():
    step_name = 'RESULT'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['args']['var']
        assert(step_name==self.step_name)
        return output_var

    def html(self,output,output_var):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        if isinstance(output, Image.Image):
            output = html_embed_image(output,300)
        else:
            output = html_output(output)
            
        return f"""<div>{step_name} -> {output_var} -> {output}</div>"""

    def execute(self,prog_step,inspect=False):
        output_var = self.parse(prog_step)
        if output_var in prog_step.state:
            output = prog_step.state[output_var]
        else:
            output = eval(output_var)
        if inspect:
            html_str = self.html(output,output_var)
            return output, html_str

        return output

class FlagInterpreter():
    step_name = 'FLAG'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        begin = parse_result['args']['begin']
        middle = parse_result['args']['middle']
        end = parse_result['args']['end']
        assert(step_name==self.step_name)
        return begin, middle, end, output_var

    def html(self):
            
        return f"""<div>FLAG is only for internal use.</div>"""

    def execute(self,prog_step,inspect=False):
        begin, middle, end, output_var = self.parse(prog_step)
        prog_step.state[output_var] = {'begin': eval(begin), 'middle': eval(middle), 'end': eval(end)}
        if inspect:
            html_str = self.html()
            return {'begin': eval(begin), 'middle': eval(middle), 'end': eval(end)}, html_str

        return {'begin': eval(begin), 'middle': eval(middle), 'end': eval(end)}

class VQAInterpreter():
    step_name = 'VQA'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        # self.processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
        # self.processor = Blip2Processor.from_pretrained(f"Salesforce/blip2-flan-t5-xxl")
        # self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large").to(self.device)
        # self.model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xxl").to(self.device)
        # self.model.eval()
        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3.5-vision-instruct", 
            device_map="cuda", 
            trust_remote_code=True, 
            torch_dtype="auto", 
            _attn_implementation='flash_attention_2'    
        )
        self.model.eval()
        self.processor = AutoProcessor.from_pretrained("microsoft/Phi-3.5-vision-instruct", 
            trust_remote_code=True, 
            num_crops=4
            )
        self.stemmer = PorterStemmer()

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        args = parse_result['args']
        video_var = args['video']
        question = eval(args['question'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return video_var,question,output_var

    def predict(self, video, questions):
        # 1) extract all frames
        images, _ = video.extract_all_frames(max_frame_num=8)
        if len(images) == 0:
            return []

        answers = []

        for image in images:
            image.thumbnail((640,640),Image.Resampling.LANCZOS)
            answer = ''

            for i in range(len(questions)):
                imgs = [image]
                messages = [
                    {"role": "user", "content": "<|image_1|>\n" + questions[i]},
                ]
                prompt = self.processor.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
                )
                inputs = self.processor(prompt, imgs, return_tensors="pt").to("cuda:0")
                generation_args = { 
                    "max_new_tokens": 1024, 
                    "temperature": 0.0, 
                    "do_sample": False, 
                }
                with gpu_lock:
                    with torch.inference_mode():
                        generate_ids = self.model.generate(**inputs, 
                        eos_token_id=self.processor.tokenizer.eos_token_id, 
                        **generation_args
                        )
                generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
                response = self.processor.batch_decode(generate_ids, 
                    skip_special_tokens=True, 
                    clean_up_tokenization_spaces=False)[0]
                
                answer += 'User: ' + questions[i] + '\nAssistant: ' + response + '\n\n'
            answer += 'Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.'
            answers.append(answer)
        # # 2) build a list of identical questions, one per image
        # questions = [question] * len(images)

        # # 3) single batched encoding
        # encoding = self.processor(
        #     images,
        #     questions,
        #     return_tensors="pt",
        #     padding=True,        # pad to the longest in the batch
        #     truncation=True      # if your questions might be long
        # ).to(self.device)

        # # 4) one batched generate
        # with gpu_lock:
        #     with torch.no_grad():
        #         outputs = self.model.generate(
        #             **encoding,
        #             max_new_tokens=64,  # tune as needed
        #             num_beams=5,        # optional
        #             do_sample=False
        #         )

        # # 5) decode each answer
        # answers = [
        #     self.processor.decode(
        #         out_ids, skip_special_tokens=True
        #     ).strip()
        #     for out_ids in outputs
        # ]
        return answers

    def html(self,img,question,answer,output_var):
        step_name = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        answer = html_output(answer)
        output_var = html_var_name(output_var)
        video_arg = html_arg_name('video')
        question_arg = html_arg_name('question')
        return f"""<div>{output_var}={step_name}({video_arg}={img_str},&nbsp;{question_arg}='{question}')={answer}</div>"""

    def execute(self,prog_step,inspect=False):
        video_var,question,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]

        questions = question.split('|')

        questions[0] = prog_step.state['QUESTION']

        if 'TIME' in prog_step.state:
            time_flag = prog_step.state['TIME']
            
            time_suffix = ''
            if time_flag['begin'] is not None and '[' in time_flag['begin']:
                time_suffix = 'near the beginning of the original video'
            elif time_flag['middle'] is not None and '[' in time_flag['middle']:
                time_suffix = 'near the middle of the original video'
            elif time_flag['end'] is not None and '[' in time_flag['end']:
                time_suffix = 'near the end of the original video'

            for i in range(len(questions)):
                if video_var + '_EVENT' in prog_step.state:
                    if time_suffix == '':
                        questions[i] = 'This is a frame from the original video ' + prog_step.state[video_var + '_TIME'] + " " + prog_step.state[video_var + '_EVENT'].lower() + '\n' + questions[i]
                    else:
                        questions[i] = 'This is a frame ' + time_suffix + ' ' + prog_step.state[video_var + '_TIME'] + " " + prog_step.state[video_var + '_EVENT'].lower() + '\n' + questions[i]
                elif time_suffix != '':
                    questions[i] = 'This is a frame ' + time_suffix + '.\n' + questions[i]

        answers = self.predict(video,questions)
        prog_step.state[output_var] = answers
        if inspect:
            # get the middle frame of the video
            length = video.get_video_length()
            middle_frame = int(length / 2)
            frame = video.extract_frame(middle_frame)
            html_str = self.html(frame, question, answers, output_var)
            return answers, html_str
        return answers

class VIDQAInterpreter:
    step_name = 'VIDQA'

    def __init__(
        self,
        model_choice: str = "qwen",
        pretrained: str = "lmms-lab/LLaVA-Video-7B-Qwen2",
        model_name: str = "llava_qwen",
        llava_model_id: str = "llava-hf/LLaVA-NeXT-Video-7B-hf",
        max_frames: int = 64,
        conv_template: str = "qwen_1_5",
        device: str = "cuda"
    ):
        print(f"Registering {self.step_name} step with {pretrained}")
        self.device = device if torch.cuda.is_available() else "cpu"
        self.max_frames = max_frames
        self.conv_template = conv_template

        if model_choice == "qwen":
            # Load the original Qwen-based model
            self.tokenizer, self.model, self.image_processor, _ = load_pretrained_model(
                pretrained, None, model_name
            )
            self.model.to(self.device).eval()

        elif model_choice == "llava":
            # Load the LLaVA-NeXT-Video model and processor
            self.processor = LlavaNextVideoProcessor.from_pretrained(llava_model_id)
            self.model = LlavaNextVideoForConditionalGeneration.from_pretrained(
                llava_model_id,
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True,
            ).to(self.device).eval()


    def parse(self, prog_step):
        pr = parse_step(prog_step.prog_str)
        assert pr['step_name'] == self.step_name
        video_var = pr['args']['video']
        question = eval(pr['args']['question'])
        output_var = pr['output_var']
        return video_var, question, output_var

    def predict_qwen(self, video, questions, choices):

        frames, timestamps = video.extract_all_frames()
        frames_np = np.stack([np.array(img) for img in frames])
        frame_time_str = ",".join(f"{t:.2f}s" for t in timestamps)
        video_time = video.get_video_length()

        # preprocess frames to pixel_values tensor
        pixel_values = self.image_processor.preprocess(
            frames_np, return_tensors="pt"
        )["pixel_values"].to(self.device).half()
        # pack into list as the model expects
        video_inputs = [pixel_values]

        # build conversation
        time_instr = (
            f"The video lasts for {video_time:.2f} seconds, "
            f"and {pixel_values.shape[1]} frames are uniformly sampled at {frame_time_str}. "
        )

        answer = ''

        for i in range(len(questions)):
            if i == 0:
                prompt_text = DEFAULT_IMAGE_TOKEN + "\n" + time_instr + "\n" + questions[i] + f"\nChoices (choose one): {', '.join(choices)}."
                prompt_text = DEFAULT_IMAGE_TOKEN + "\n" + time_instr + "\n" + questions[i]
            else:
                prompt_text = DEFAULT_IMAGE_TOKEN + "\n" + time_instr + "\n" + questions[i]

            conv = copy.deepcopy(conv_templates[self.conv_template])
            conv.append_message(conv.roles[0], prompt_text)
            conv.append_message(conv.roles[1], None)
            prompt = conv.get_prompt()

            # tokenize with image token
            input_ids = tokenizer_image_token(
                prompt,
                self.tokenizer,
                IMAGE_TOKEN_INDEX,
                return_tensors="pt"
            ).unsqueeze(0).to(self.device)

            # generate
            with gpu_lock:
                with torch.no_grad():
                    outputs = self.model.generate(
                        input_ids,
                        images=video_inputs,
                        modalities=["video"],
                        do_sample=False,
                        temperature=0.0,
                        max_new_tokens=512,
                    )

            answer += 'User: ' + questions[i] + '\nAssistant: ' + self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip() + '\n\n'

            del input_ids, outputs, prompt
            torch.cuda.empty_cache()
            gc.collect()

            # prompt_text = DEFAULT_IMAGE_TOKEN + "\n" + time_instr + f"\nPlease describe this video in detail."

            # conv = copy.deepcopy(conv_templates[self.conv_template])
            # conv.append_message(conv.roles[0], prompt_text)
            # conv.append_message(conv.roles[1], None)
            # prompt = conv.get_prompt()

            # # tokenize with image token
            # input_ids = tokenizer_image_token(
            #     prompt,
            #     self.tokenizer,
            #     IMAGE_TOKEN_INDEX,
            #     return_tensors="pt"
            # ).unsqueeze(0).to(self.device)

            # # generate
            # with gpu_lock:
            #     with torch.no_grad():
            #         outputs = self.model.generate(
            #             input_ids,
            #             images=video_inputs,
            #             modalities=["video"],
            #             do_sample=False,
            #             temperature=0.0,
            #             max_new_tokens=512,
            #         )

            # result = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip()
            # if answer not in result:
            #     answer = "Caption: " + self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip() + "(trust the caption **only if** it **explicitly** mentions evidence that fully supports another answer. Otherwise trust VLM more. **Events that are not mentioned should not be considered as incorrect.**)\nVLM answer: " + answer
            # # answer += ' (please judge according to **both** the answer above and the caption below. For the caption, only take **explicitly** mentioned things as evidence. **If something is not mentioned, you cannot directly judge it as wrong, as the caption may overlook details.**)\n' + self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip()
            # print(answer)
            # del input_ids, outputs, prompt
            # torch.cuda.empty_cache()
            # gc.collect()
        answer += 'Note: This is not a continuous conversation. Each question is independant. User questions may include wrong assumptions. First judge based on explicit things (with majority voting if contradictory) mentioned by assistant.'
        print(answer)
        return [answer]

    def predict_llava(self, video, questions, choices):
        answers = ''
        # Extract frames
        frames, timestamps = video.extract_all_frames()
        frames_np = np.stack([np.array(img) for img in frames])
        for i in range(len(questions)):
            if i > 0:
                answers += '\n'
            conversation = [
                {"role": "user", "content": [
                    {"type": "text", "text": questions[i] + f"\nChoices (choose one): {', '.join(choices)}" if i == 0 else questions[i]},
                    {"type": "video"}
                ]}
            ]
            prompt = self.processor.apply_chat_template(
                conversation,
                add_generation_prompt=True
            )
            inputs = self.processor(
                text=prompt,
                videos=frames_np,
                padding=True,
                return_tensors="pt"
            ).to(self.device)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=512,
                    do_sample=False
                )

            # decode and return
            answer = self.processor.decode(outputs[0], skip_special_tokens=True).strip()
            del inputs, outputs, prompt
            torch.cuda.empty_cache()
            gc.collect()
            answers += answer
        return [answers]

    def html(self, img, question, answers, output_var):
        step = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        ans_str = html_output(answers[0])
        q_arg = html_arg_name('question')
        v_arg = html_arg_name('video')
        out = html_var_name(output_var)
        return (
            f"<div>"
            f"{out}={step}({v_arg}={img_str}, {q_arg}='{question}')="
            f"{ans_str}"
            f"</div>"
        )

    def execute(self, prog_step, inspect=False):
        video_var, question, output_var = self.parse(prog_step)
        video = prog_step.state[video_var]

        questions = question.split('|')

        questions[0] = prog_step.state['QUESTION']

        if 'TIME' in prog_step.state:
            time_flag = prog_step.state['TIME']
            
            time_suffix = ''
            if time_flag['begin'] is not None and '[' in time_flag['begin']:
                time_suffix = 'at the beginning of the original video'
            elif time_flag['middle'] is not None and '[' in time_flag['middle']:
                time_suffix = 'at the middle of the original video'
            elif time_flag['end'] is not None and '[' in time_flag['end']:
                time_suffix = 'at the end of the original video'

            for i in range(len(questions)):
                if video_var + '_EVENT' in prog_step.state:
                    if time_suffix == '':
                        questions[i] = 'The video is clipped from the original video ' + prog_step.state[video_var + '_TIME'] + " " + prog_step.state[video_var + '_EVENT'].lower() + '\n' + questions[i]
                    else:
                        questions[i] = 'The video is clipped ' + time_suffix + ' ' + prog_step.state[video_var + '_TIME'] + " " + prog_step.state[video_var + '_EVENT'].lower() + '\n' + questions[i]
                elif time_suffix != '':
                    questions[i] = 'The video is clipped ' + time_suffix + '.\n' + questions[i]
        answers = self.predict_qwen(video, questions, prog_step.state["CHOICES"])
        prog_step.state[output_var] = answers

        if inspect:
            mid_t = video.get_video_length() / 2
            frame = video.extract_frame(mid_t)
            html_str = self.html(frame, question, answers, output_var)
            return answers, html_str

        return answers

class VLMInterpreter:
    step_name = 'VLM'

    def __init__(
        self,
        pretrained: str = "lmms-lab/LLaVA-Video-7B-Qwen2",
        model_name: str = "llava_qwen",
        max_frames: int = 64,
        conv_template: str = "qwen_1_5",
        device: str = "cuda"
    ):
        print(f"Registering {self.step_name} step with {pretrained}")
        self.device = device if torch.cuda.is_available() else "cpu"
        self.max_frames = max_frames
        self.conv_template = conv_template
        self._embedder = SentenceTransformer("hkunlp/instructor-xl")

        # load tokenizer, model, image_processor
        self.tokenizer, self.model, self.image_processor, _ = load_pretrained_model(
            pretrained, None, model_name)
        self.model.to(self.device).eval()

    def parse(self, prog_step):
        pr = parse_step(prog_step.prog_str)
        assert pr['step_name'] == self.step_name
        video_var = pr['args']['video']
        question = eval(pr['args']['question'])
        output_var = pr['output_var']
        return video_var, question, output_var

    def predict(self, video, question: str, choices):

        frames, timestamps = video.extract_all_frames()
        frames_np = np.stack([np.array(img) for img in frames])
        frame_time_str = ",".join(f"{t:.2f}s" for t in timestamps)
        video_time = video.get_video_length()

        # preprocess frames to pixel_values tensor
        pixel_values = self.image_processor.preprocess(
            frames_np, return_tensors="pt"
        )["pixel_values"].to(self.device).half()
        # pack into list as the model expects
        video_inputs = [pixel_values]

        # build conversation
        time_instr = (
            f"The video lasts for {video_time:.2f} seconds, "
            f"and {pixel_values.shape[1]} frames are uniformly sampled at {frame_time_str}. "
        )
        prompt_text = DEFAULT_IMAGE_TOKEN + "\n" + time_instr + "\n" + question + f"\nChoices (choose one): {', '.join(choices)}."

        conv = copy.deepcopy(conv_templates[self.conv_template])
        conv.append_message(conv.roles[0], prompt_text)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()

        # tokenize with image token
        input_ids = tokenizer_image_token(
            prompt,
            self.tokenizer,
            IMAGE_TOKEN_INDEX,
            return_tensors="pt"
        ).unsqueeze(0).to(self.device)

        # generate
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids,
                images=video_inputs,
                modalities=["video"],
                do_sample=False,
                temperature=0.0,
                max_new_tokens=512,
            )

        answer = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip()

        max_emb = self._embedder.encode(answer, convert_to_tensor=True)
        choice_embs = self._embedder.encode(choices, convert_to_tensor=True)
        sims = util.cos_sim(max_emb, choice_embs)[0]
        answer_index = int(sims.argmax())
        
        del input_ids, outputs, prompt
        torch.cuda.empty_cache()
        gc.collect()
        
        return answer_index

    def html(self, img, question, answer, output_var):
        step = html_step_name(self.step_name)
        img_str = html_embed_image(img)
        ans_str = html_output(answer)
        q_arg = html_arg_name('question')
        v_arg = html_arg_name('video')
        out = html_var_name(output_var)
        return (
            f"<div>"
            f"{out}={step}({v_arg}={img_str}, {q_arg}='{question}')="
            f"{ans_str}"
            f"</div>"
        )

    def execute(self, prog_step, inspect=False):
        video_var, question, output_var = self.parse(prog_step)
        video = prog_step.state[video_var]

        event_question = prog_step.state["QUESTION"]

        answer = self.predict(video, event_question, prog_step.state["CHOICES"])
        prog_step.state[output_var] = answer

        if inspect:
            mid_t = video.get_video_length() / 2
            frame = video.extract_frame(mid_t)
            html_str = self.html(frame, question, answer, output_var)
            return answer, html_str

        return answer

class LocInterpreter():
    step_name = 'LOC'

    def __init__(self,thresh=0.1,nms_thresh=0.5):
        print(f'Registering {self.step_name} step')
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.processor = OwlViTProcessor.from_pretrained("google/owlvit-large-patch14")
        self.model = OwlViTForObjectDetection.from_pretrained("google/owlvit-large-patch14").to(self.device)
        self.model.eval()
        self.thresh = thresh
        self.nms_thresh = nms_thresh
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.processor_vqa = AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
        self.model_vqa = BlipForQuestionAnswering.from_pretrained(
            "Salesforce/blip-vqa-capfilt-large").to(self.device)
        self.model_vqa.eval()
        self.stemmer = PorterStemmer()

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        video_var = parse_result['args']['video']
        question = eval(parse_result['args']['question'])
        answer = eval(parse_result['args']['answer'])
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return video_var,question,answer,output_var

    def normalize_coord(self,bbox,img_size):
        w,h = img_size
        x1,y1,x2,y2 = [int(v) for v in bbox]
        x1 = max(0,x1)
        y1 = max(0,y1)
        x2 = min(x2,w-1)
        y2 = min(y2,h-1)
        return [x1,y1,x2,y2]

    def predict(self, video, question, answer):
        images, frame_no = video.extract_frames()
        # get all nouns from the question
        tokens = nltk.word_tokenize(question)
        tagged = nltk.pos_tag(tokens)
        nouns = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
        
        # Process in batches of 20 to avoid OOM
        batch_size = 20 // len(nouns)
        frames_with_all_nouns = []
        
        for i in range(0, len(images), batch_size):
            batch_images = images[i:i+batch_size]
            batch_frame_indices = list(range(i, min(i+batch_size, len(images))))
            
            # Create text prompts for each noun for each image in batch
            batch_text_prompts = []
            for _ in range(len(batch_images)):
                for noun in nouns:
                    batch_text_prompts.append(f"a photo of {noun}")
            
            # Restructure for batch processing
            encoding = self.processor(
                text=batch_text_prompts,
                images=[img for img in batch_images for _ in range(len(nouns))],
                return_tensors='pt', 
                padding=True
            )
            encoding = {k: v.to(self.device) for k, v in encoding.items()}
            
            with torch.no_grad():
                outputs = self.model(**encoding)
            
            # Post-process batch results
            target_sizes = torch.Tensor([img.size[::-1] for img in batch_images for _ in range(len(nouns))])
            batch_results = self.processor.post_process_object_detection(
                outputs=outputs,
                threshold=self.thresh,
                target_sizes=target_sizes
            )
            
            # Restructure results back into per-image format
            restructured_results = []
            for j in range(len(batch_images)):
                image_results = {'labels': set()}
                for k in range(len(nouns)):
                    result_idx = j * len(nouns) + k
                    if result_idx < len(batch_results):
                        labels = batch_results[result_idx]['labels']
                        for label in labels:
                            image_results['labels'].add(k)  # Add the noun index
                restructured_results.append(image_results)
                
            # Find frames containing all nouns in this batch
            for j, results in enumerate(restructured_results):
                if set(results['labels']) == set(range(len(nouns))):
                    frames_with_all_nouns.append(batch_frame_indices[j])

        # frames_with_all_nouns = list(range(0, len(images)))
        
        # Process VQA in batches too
        frames_with_answer = []
        batch_frames = [video.extract_frame(frame_idx) for frame_idx in frames_with_all_nouns]
        
        batch_answers = []
        for frame in batch_frames:
            answer_vqa = self.get_vqa(frame, question)
            words = nltk.word_tokenize(answer_vqa)
            stemmed_words_vqa = [self.stemmer.stem(word) for word in words]
            stemmed_words_answer = [self.stemmer.stem(word) for word in answer]
            
            if len(set(stemmed_words_answer) & set(stemmed_words_vqa)) > 0:
                batch_answers.append(True)
            else:
                batch_answers.append(False)
        
        # Add frame indices with matching answers
        for j, has_answer in enumerate(batch_answers):
            if has_answer:
                frames_with_answer.append(batch_frame_indices[j])
        
        # cluster frame numbers from the original frame_no list
        # ensuring we're using the frames that actually have answers
        if frames_with_answer:
            # Get indices into frame_no that correspond to frames_with_answer
            indices_to_cluster = [frame_no.index(frame) for frame in frames_with_answer if frame in frame_no]
            clusters = cluster([indices_to_cluster])  # Assuming cluster() expects indices
            clusters = [frame_no[i] for i in clusters[0]]
        else:
            # Fallback to middle frames if no answer frames found
            duration = video.get_video_length()
            middle_frame = int(duration) // 2
            return [i for i in range(middle_frame-2, middle_frame+3) if i < duration and i >= 0]
        
        return clusters

    def html(self,img,question,answer,resulting_frame,output_var):
        step_name=html_step_name(self.step_name)
        img_arg=html_arg_name('image')
        output_var=html_var_name(output_var)
        question_arg=html_arg_name('question')
        answer_arg=html_arg_name('answer')
        img=html_embed_image(img,300)
        resulting_frame = html_embed_image(resulting_frame,300)
        return f"<div>{output_var}={step_name}({img_arg}={img}, {question_arg}='{question}', {answer_arg}='{answer}')={resulting_frame}</div>"
    
    def get_vqa(self,img,question):
        encoding = self.processor_vqa(img,question,return_tensors='pt')
        encoding = {k:v.to(self.device) for k,v in encoding.items()}
        with torch.no_grad():
            outputs = self.model_vqa.generate(**encoding)
        
        return self.processor_vqa.decode(outputs[0], skip_special_tokens=True)

    def execute(self,prog_step,inspect=False):
        video_var,question,answer,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        frame_no = self.predict(video,question,answer)
        resulting_frame_img = video.extract_frame(frame_no[0])
        duration = video.get_video_length()
        img = video.extract_frame(duration // 2)

        prog_step.state[output_var] = frame_no
        if inspect:
            html_str = self.html(img, question, answer, resulting_frame_img, output_var)
            return frame_no, html_str

        return frame_no

class LocInterpreter():
    step_name = 'LOC'

    def __init__(self, device: str = None):
        self.device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
        # load the Intel/tvp-base model & processor
        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
                "wwwyyy/TimeZero-Charades-7B",
                use_sliding_window=True,
                torch_dtype=torch.bfloat16,
                attn_implementation="flash_attention_2",
            ).to(self.device)
        self.model.eval()
        self.model = torch.compile(self.model)

        self.processor = AutoProcessor.from_pretrained("wwwyyy/TimeZero-Charades-7B")

    def inference(self, video_path, prompt, model, processor, max_new_tokens=2048, device="cuda:0"):
        messages = [
            {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"video": video_path, 
                    "total_pixels": 3584 * 28 * 28, 
                    "min_pixels": 16 * 28 * 28,
                    },
                ]
            },
        ]
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
        fps_inputs = video_kwargs['fps']
        
        inputs = processor(text=[text], images=image_inputs, videos=video_inputs, fps=fps_inputs, padding=True, return_tensors="pt")
        inputs = inputs.to(device)

        with torch.no_grad():
            output_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
        
        generated_ids = [output_ids[i][len(inputs.input_ids[i]):] for i in range(len(output_ids))]
        output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        del text, image_inputs, video_inputs, video_kwargs, inputs, output_ids, generated_ids
        torch.cuda.empty_cache()
        gc.collect()
        return output_text[0]

    def parse_timestamp_output(self, output_string):
        matches = re.findall(r"(\d+\.?\d*) (to|and) (\d+\.?\d*)", output_string)
        if not matches:
            answer_match = re.search(r"<answer>(.*?)</answer>", output_string)
            if answer_match:
                answer_content = answer_match.group(1).strip()
                answer_matches = re.findall(r"(\d+\.?\d*) (to|and) (\d+\.?\d*)", answer_content)
                if answer_matches:
                    last_match = answer_matches[-1]
                    return float(last_match[0]), float(last_match[2])
            return None, None

        last_match = matches[-1]
        start_time_str = last_match[0]
        end_time_str = last_match[2]
        
        try:
            start_time = float(start_time_str)
            end_time = float(end_time_str)
            return start_time, end_time
        except ValueError:
            return None, None

    def predict(self, video, event):
        prompt = f"""To accurately pinpoint the event "{event}" in the video, determine the precise time period of the event.

Output your thought process within the <think> </think> tags, including analysis with either specific timestamps (xx.xx) or time ranges (xx.xx to xx.xx) in <timestep> </timestep> tags.

Then, provide the start and end times (in seconds, precise to two decimal places) in the format "start time to end time" within the <answer> </answer> tags. For example: "12.54 to 17.83"."""
        video.save('tmp.mp4',fps=None)
        ans = self.inference('tmp.mp4', prompt, self.model, self.processor)
        rel_start, rel_end = self.parse_timestamp_output(ans)
        if rel_start is None:
            rel_start = 0
            rel_end = int(video.get_video_length())

        return [rel_start, rel_end]

    def parse(self, prog_step):
        # unchanged
        parse_result = parse_step(prog_step.prog_str)
        assert parse_result['step_name'] == self.step_name
        vid, q = parse_result['args']['video'], parse_result['args']['event']
        return vid, eval(q), parse_result['output_var']

    def execute(self, prog_step, inspect=False):
        video_var, question, output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        interval = self.predict(video, question)
        prog_step.state[output_var + '_EVENT'] = question
        prog_step.state[output_var] = interval
        if inspect:
            return interval, f"Localized interval: {interval}s"
        return interval

class CapInterpreter():
    step_name = 'CAP'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self.device     = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.processor  = AutoProcessor.from_pretrained(
            "microsoft/Florence-2-large",
            trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Florence-2-large",
            torch_dtype=self.torch_dtype,
            trust_remote_code=True
        ).to(self.device)
        self.model.eval()

    def parse(self, prog_step):
        pr = parse_step(prog_step.prog_str)
        assert pr['step_name'] == self.step_name
        return pr['args']['video'], pr['output_var']

    def predict_batch(self, imgs: list[Image.Image]) -> list[str]:
        # build a prompt for each image
        prompts = ["<MORE_DETAILED_CAPTION>"] * len(imgs)

        # one processor call for the entire batch
        with gpu_lock:
            inputs = self.processor(
                text=prompts,
                images=imgs,
                return_tensors="pt",
                padding=True
            ).to(self.device, self.torch_dtype)

        # single batched generate
        generated_ids = self.model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            num_beams=3,
            do_sample=False
        )

        # batch‐decode all sequences
        texts = self.processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )

        del generated_ids, inputs, prompts
        torch.cuda.empty_cache()
        gc.collect()

        # post‐process each caption
        out = []
        for txt, img in zip(texts, imgs):
            parsed = self.processor.post_process_generation(
                txt,
                task="<MORE_DETAILED_CAPTION>",
                image_size=(img.width, img.height)
            )
            out.append(parsed["<MORE_DETAILED_CAPTION>"])
        return out

    def html(self, img, output, output_var):
        step_name = html_step_name(self.step_name)
        img_str   = html_embed_image(img)
        out       = html_output(output)
        var       = html_var_name(output_var)
        arg       = html_arg_name('video')
        return f"<div>{var}={step_name}({arg}={img_str})={out}</div>"

    def execute(self, prog_step, inspect=False):
        video_var, output_var = self.parse(prog_step)
        video = prog_step.state[video_var]

        # sample timestamps
        dur   = video.get_video_length()
        times = np.linspace(0, dur, num=min(int(dur), 10), endpoint=False).tolist()

        # extract all frames at once
        frames = [video.extract_frame(t) for t in times]

        # batch‐predict
        captions = self.predict_batch(frames)

        # write back to state
        prog_step.state[output_var] = captions

        if inspect:
            # for html, just show the middle frame
            mid_img  = video.extract_frame(dur / 2)
            html_str = self.html(mid_img, captions, output_var)
            return captions, html_str

        return captions

        
class SelectInterpreter():
    step_name = 'SELECT'

    def __init__(self):
        print(f'Registering {self.step_name} step')
        self._embedder = SentenceTransformer("hkunlp/instructor-xl")

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        question = eval(parse_result['args']['question'])
        information_var = parse_result['args']['information']
        choices_var = parse_result['args']['choices']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return question,information_var,choices_var,output_var

    def html(self,question,information,choices,output_var,answer):
        step_name = html_step_name(self.step_name)
        output_var = html_var_name(output_var)
        question_arg = html_arg_name('question')
        choices_arg = html_arg_name('choices')
        information_arg = html_arg_name('information')
        output = html_output(answer)
        return f"""<div>{output_var}={step_name}({question_arg}={question}, {information_arg}={information}, {choices_arg}={choices})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        question,information_var,choices_var,output_var = self.parse(prog_step)
        information = prog_step.state[information_var]
        choices = prog_step.state[choices_var]
        prompt = f"You are doing a video QA task.\nQuestion: {question}\nBased on the information on potential relative frames {information}, your task is to estimate the possibility of each choice in {choices} to be the correct answer. Note that the answers may not be absolutely correct and everything (like grammar) may be inaccurate, so each choice has possibility, and it is possible that all choices have a low possibility. Explicitly mentioned things weights more and implied things weights less. Your response must should be a json:\n{{\"reasoning\": \"<Your think step-by-step reasoning>\", \"possibility\": <A dict of estimated possibility distribution of each choice in format choice: possibility (0-100)>}}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=1000,
            )
        except:
            response = openai.ChatCompletion.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=1000,
            )
        answer = response['choices'][0]['message']['content']
        json_answer = json.loads(answer)
        possibility_dict = json_answer['possibility']
        print(possibility_dict)
        max_score = -1
        max_choice = None
        
        for choice, score in possibility_dict.items():
            if score > max_score:
                max_score = score
                max_choice = choice
        
        # Find the index of the choice with the highest score in the choices list
        if max_choice in choices:
            answer_index = choices.index(max_choice)
        else:
            # Fallback if the exact text doesn't match
            max_emb = self._embedder.encode(max_choice, convert_to_tensor=True)
            choice_embs = self._embedder.encode(choices, convert_to_tensor=True)
            sims = util.cos_sim(max_emb, choice_embs)[0]
            answer_index = int(sims.argmax())
            print(f"Warning: Could not find '{max_choice}' in choices list.")
        print(json_answer['reasoning'])

        prog_step.state[output_var] = answer_index
        prog_step.state["PROB"] = possibility_dict
        if inspect:
            html_str = self.html(question, information, choices, output_var, answer_index)
            return answer_index, html_str
        return answer_index


class ClipInterpreter():
    step_name = 'CLIP'

    def __init__(self):
        print(f'Registering {self.step_name} step')

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        video_var = parse_result['args']['video']
        frame_var = parse_result['args']['frame']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return video_var,frame_var,output_var

    def html(self,img,out_img,output_var,frame):
        img = html_embed_image(img,300)
        out_img = html_embed_image(out_img,300)
        output_var = html_var_name(output_var)
        video_arg = html_arg_name('video')
        step_name = html_step_name(self.step_name)
        frame_arg = html_arg_name('frame')
        return f"""<div>{output_var}={step_name}({video_arg}={img}, {frame_arg}=[{frame[0]} to {frame[-1]}])={out_img}</div>"""

    def execute(self,prog_step,inspect=False):
        video_var,frame_var,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        frames = prog_step.state[frame_var]
        if len(frames) > 0:
            clipped_video = video.clip(frames[0], frames[-1])
        else:
            clipped_video = video
        prog_step.state[output_var + '_EVENT'] = prog_step.state[frame_var + '_EVENT']
        prog_step.state[output_var + '_TIME'] = 'when'
        prog_step.state[output_var] = clipped_video
        if inspect:
            img = video.extract_frame(video.get_video_length() // 2)
            out_img = clipped_video.extract_frame(clipped_video.get_video_length() // 2)
            html_str = self.html(img, out_img, output_var, frames)
            return clipped_video, html_str
        return clipped_video


class ClipBeforeInterpreter(ClipInterpreter):
    step_name = 'CLIP_BEFORE'

    def execute(self,prog_step,inspect=False):
        video_var,frame_var,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        frames = prog_step.state[frame_var]
        if len(frames) > 0:
            clipped_video = video.clip(0, (frames[0] + frames[-1]) / 2)
        else:
            clipped_video = video
            
        prog_step.state[output_var] = clipped_video
        prog_step.state[output_var + '_EVENT'] = prog_step.state[frame_var + '_EVENT']
        prog_step.state[output_var + '_TIME'] = 'before'
        if inspect:
            img = video.extract_frame(video.get_video_length() // 2)
            out_img = clipped_video.extract_frame(clipped_video.get_video_length() // 2)
            html_str = self.html(img, out_img, output_var, frames)
            return clipped_video, html_str
        return clipped_video

class ClipAfterInterpreter(ClipInterpreter):
    step_name = 'CLIP_AFTER'

    def execute(self,prog_step,inspect=False):
        video_var,frame_var,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        frames = prog_step.state[frame_var]
        if len(frames) > 0:
            clipped_video = video.clip(frames[0], video.get_video_length())
        else:
            clipped_video = video
        prog_step.state[output_var] = clipped_video
        prog_step.state[output_var + '_EVENT'] = prog_step.state[frame_var + '_EVENT']
        prog_step.state[output_var + '_TIME'] = 'after'
        if inspect:
            img = video.extract_frame(video.get_video_length() // 2)
            out_img = clipped_video.extract_frame(clipped_video.get_video_length() // 2)
            html_str = self.html(img, out_img, output_var, frames)
            return clipped_video, html_str
        return clipped_video


class ClipAroundInterpreter():
    step_name = 'CLIP_AROUND'

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        video_var = parse_result['args']['video']
        frame_no = parse_result['args']['center_frame']
        if frame_no.isdecimal():
            frame_no = int(frame_no)
        else:
            frame_no = prog_step.state[frame_no]
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return video_var,frame_no,output_var

    def html(self,img,out_img,output_var,frame_no):
        img = html_embed_image(img,300)
        out_img = html_embed_image(out_img,300)
        output_var = html_var_name(output_var)
        video_arg = html_arg_name('video')
        step_name = html_step_name(self.step_name)
        frame_arg = html_arg_name('center_frame')
        return f"""<div>{output_var}={step_name}({video_arg}={img}, {frame_arg}={frame_no})={out_img}</div>"""

    def execute(self,prog_step,inspect=False):
        video_var,frame_no,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        if 'invalid=True' in prog_step.prog_str:
            prog_step.state[output_var] = video
            if inspect:
                img = video.extract_frame(video.get_video_length() // 2)
                out_img = video.extract_frame(video.get_video_length() // 2)
                html_str = self.html(img, out_img, output_var, frame_no)
                return video, html_str
            return video
        if frame_no == -1:
            frame_no = video.get_video_length()
        assert frame_no >= 0 and frame_no <= video.get_video_length()
        radius = max(video.get_video_length() / 10, 4)
        start = max(0, frame_no - radius)
        end = min(video.get_video_length(), frame_no + radius)
        if start > frame_no - radius:
            end = min(video.get_video_length(), frame_no + radius + (start - (frame_no - radius)))
        elif end < frame_no + radius:
            start = max(0, frame_no - radius - (frame_no + radius - end))
        clipped_video = video.clip(start, end)
        prog_step.state[output_var] = clipped_video
        if inspect:
            img = video.extract_frame(video.get_video_length() // 2)
            out_img = clipped_video.extract_frame(clipped_video.get_video_length() // 2)
            html_str = self.html(img, out_img, output_var, frame_no)
            return clipped_video, html_str
        return clipped_video
    

class LengthInterpreter():
    step_name = 'LENGTH'

    def parse(self,prog_step):
        parse_result = parse_step(prog_step.prog_str)
        step_name = parse_result['step_name']
        video_var = parse_result['args']['video']
        output_var = parse_result['output_var']
        assert(step_name==self.step_name)
        return video_var,output_var

    def html(self,img,output_var,length):
        img = html_embed_image(img)
        output_var = html_var_name(output_var)
        video_arg = html_arg_name('video')
        step_name = html_step_name(self.step_name)
        output = html_output(length)
        return f"""<div>{output_var}={step_name}({video_arg}={img})={output}</div>"""

    def execute(self,prog_step,inspect=False):
        video_var,output_var = self.parse(prog_step)
        video = prog_step.state[video_var]
        length = video.get_video_length()
        prog_step.state[output_var] = length
        if inspect:
            img = video.extract_frame(length // 2)
            html_str = self.html(img, output_var, length)
            return length, html_str
        return length
        
def register_step_interpreters(method = 'agent'):
    if method == 'agent':
        return dict(
            VIDQA=VIDQAInterpreter(),
            VQA=VQAInterpreter(),
            EVAL=EvalInterpreter(),
            RESULT=ResultInterpreter(),
            LOC=LocInterpreter(),
            SELECT=SelectInterpreter(),
            CLIP=ClipInterpreter(),
            CLIP_BEFORE=ClipBeforeInterpreter(),
            CLIP_AFTER=ClipAfterInterpreter(),
            CLIP_AROUND=ClipAroundInterpreter(),
            LENGTH=LengthInterpreter(),
            # VLM=VLMInterpreter(),
            FLAG=FlagInterpreter(),
            CAP = CapInterpreter()
        )
    else:
        return dict(VLM = VLMInterpreter())