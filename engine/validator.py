# from .step_interpreters import parse_step

import nltk
nltk.download('averaged_perceptron_tagger_eng')
import inflect
import io
import tokenize

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

def validate(program, question, module_list, state_dict = {"IMAGE": None}):
    inflect_engine = inflect.engine()
    lines =program.split('\n')
    num_box_arrays = 0
    num_image_arrays = 0
    program_lines = program.split('\n')
    for i, line in enumerate(program_lines):
        if lines[i] != line:
            line = lines[i]
        parse_result = parse_step(line)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        if step_name not in module_list:
            # print(f"Invalid step name: {step_name}")
            return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
        if step_name == "EVAL":
            try:
                expr = eval(parse_result['args']['expr'])
                for var_name,var_value in state_dict.items():
                    if isinstance(var_value,str):
                        if var_value in ['yes','no']:
                            state_dict[var_name] = var_value=='yes'
                        elif var_value.isdecimal():
                            state_dict[var_name] = var_value
                        else:
                            state_dict[var_name] = f"'{var_value}'"
                    else:
                        state_dict[var_name] = var_value

                if 'xor' in expr:
                    expr = expr.replace('xor','!=')

                expr = expr.format(**state_dict)
                step_output = eval(expr)
                state_dict[output_var] = step_output

                lines[i] = line.replace(" == 'no'", " == False")
                lines[i] = lines[i].replace(" == 'yes'", " == True")
            except:
                # print(f"Invalid expression: {parse_result['args']['expr']}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
        elif step_name == "LOC":
            object_name = eval(parse_result['args']['object'])
            last_word =object_name.split()[-1]
            output_var = parse_result['output_var']
            # judge whether the last word is a noun
            if nltk.pos_tag([last_word])[0][1] not in ['NN','NNS','NNP','NNPS']:
                # print(f"Invalid object name: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            image = parse_result['args']['image']
            if image not in state_dict:
                # print(f"Invalid image: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            if nltk.pos_tag([last_word])[0][1] in ['NNS','NNPS']:
                lines[i] = f"{output_var}=LOC(image={image},object='{object_name}',plural=True)"
            last_word_plural = inflect_engine.plural(last_word)
            question_clean = question.replace('?','')
            question_clean = question_clean.replace('.','')
            question_clean = question_clean.replace(',','')
            if last_word not in question_clean.split() and last_word_plural not in question_clean.split():
                # print(f"Invalid object: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            if last_word not in question_clean.split() and last_word_plural in question_clean.split():
                lines[i] = f"{output_var}=LOC(image={image},object='{object_name}',plural=True)"
            state_dict[output_var] = [[0,0,100,100]]
            # the following if statement is designed to better handle questions like "Are both people wearing glasses?". This is just a modification that makes the solution of such tasks more interpretable. Feel free to comment it out if you think it is unnecessary.
            if 'all' in question or 'every' in question or 'each' in question or 'both' in question:
                cropped_image = None
                for line_after in program_lines[i+1:]:
                    parse_result_after = parse_step(line_after)
                    step_name_after = parse_result_after['step_name']
                    if step_name_after == 'CROP' and parse_result_after['args']['box'] == output_var:
                        cropped_image = parse_result_after['output_var']
                        break
                if cropped_image is None:
                    continue
                VQA_output_vars = []
                for line_after in lines[i+1:]:
                    parse_result_after = parse_step(line_after)
                    step_name_after = parse_result_after['step_name']
                    if step_name_after == 'VQA' and parse_result_after['args']['image'] == cropped_image:
                        VQA_output_vars.append(parse_result_after['output_var'])
                if len(VQA_output_vars) <= 1:
                    continue
                lines[i] = f"BOX_ARRAY{num_box_arrays}=LOC(image={image},object='{object_name}',plural=True)"
                state_dict[f"BOX_ARRAY{num_box_arrays}"] = [[0,0,100,100]]
                num_box_arrays += 1
                VQA_image_index = {}
                for j in range(i+1,len(program_lines)):
                    parsed_result_after = parse_step(program_lines[j])
                    if parsed_result_after['step_name'] == 'CROP' and parsed_result_after['args']['box'] == output_var:
                        lines[j] = lines[j].replace(cropped_image,f"IMAGE_ARRAY{num_image_arrays}")
                        VQA_image_index[num_image_arrays] = 1
                        lines[j] = lines[j].replace(output_var,f"BOX_ARRAY{num_box_arrays-1}")
                        num_image_arrays += 1
                    if parsed_result_after['step_name'] == 'VQA':
                        VQA_output_var = parsed_result_after['output_var']
                        VQA_image_var = parsed_result_after['args']['image']
                        question = eval(parsed_result_after['args']['question'])
                        # remove words like "first", "second", etc. from the question
                        words = question.split()
                        words = [word for word in words if word not in ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']]
                        question = ' '.join(words)
                        new_image_var = f"IMAGE_ARRAY{int(VQA_image_var.split('IMAGE')[-1])}"
                        index = VQA_image_index[int(VQA_image_var.split('IMAGE')[-1])]
                        lines[j] = f'{VQA_output_var}=VQA(image={new_image_var},index={index},question="{question}")'
                        VQA_image_index[int(VQA_image_var.split('IMAGE')[-1])] += 1
        elif 'CROP' in step_name:
            box = parse_result['args']['box']
            image = parse_result['args']['image']
            if image not in state_dict or box not in state_dict:
                # print(f"Invalid image or box: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[image]
        elif step_name == "COUNT":
            box = parse_result['args']['box']
            if box not in state_dict:
                # print(f"Invalid box: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = len(state_dict[box])
        elif step_name == "VQA":
            image = parse_result['args']['image']
            if image not in state_dict:
                # print(f"Invalid image: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = '0'
        elif step_name == "RESULT":
            var = parse_result['args']['var']
            if var not in state_dict:
                # print(f"Invalid var: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[var]
        elif step_name == "GET":
            image = parse_result['args']['image']
            if image not in state_dict:
                # print(f"Invalid image: {line}")
                return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[image]
        else:
            # print(f"Invalid step name: {step_name}")
            return f"""ANSWER0=VQA(image=IMAGE,question=\"{question}\")\nFINAL_RESULT=RESULT(var=ANSWER0)"""
    program = '\n'.join(lines)
    return program
