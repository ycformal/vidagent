import os
# Enforce the download/cache directory for Hugging Face models.
os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import openai
import copy

from .step_interpreters import register_step_interpreters, parse_step


class Program:
    def __init__(self, prog_str, init_state=None):
        self.prog_str = prog_str
        self.state = init_state if init_state is not None else {}
        self.instructions = self.prog_str.split('\n')


class ProgramInterpreter:
    def __init__(self):
        self.step_interpreters = register_step_interpreters()

    def execute_step(self, prog_step, inspect):
        step_name = parse_step(prog_step.prog_str, partial=True)['step_name']
        print(step_name)
        return self.step_interpreters[step_name].execute(prog_step, inspect)

    def execute(self, prog, init_state, inspect=False):
        results = []
        if isinstance(prog, str):
            prog = Program(prog, init_state)
        else:
            assert isinstance(prog, Program)

        prog_steps = [Program(instruction, init_state=prog.state)
                      for instruction in prog.instructions]

        html_str = '<hr>'
        for prog_step in prog_steps:
            if inspect:
                step_output, step_html = self.execute_step(prog_step, inspect)
                html_str += step_html + '<hr>'
            else:
                step_output = self.execute_step(prog_step, inspect)
            results.append(step_output)

        if inspect:
            return step_output, prog.state, html_str

        return step_output, prog.state


class ProgramGenerator:
    def __init__(self, prompter, model_name_or_path="THUDM/glm-4-9b-hf",
                 temperature=0.7, top_p=0.5, prob_agg='mean'):
        """
        Initialize the ProgramGenerator using Hugging Face Transformers to load
        the Meta-Llama-3.1-70B model with offloading to avoid GPU OOM issues.

        Args:
            prompter: A function that takes inputs and returns a prompt string.
            model_name_or_path: The Hugging Face model identifier (or local path) to load.
            temperature: Generation temperature.
            top_p: Top-p (nucleus) sampling parameter.
            prob_agg: Aggregation method for probabilities (not used here).
        """
        self.prompter = prompter
        self.temperature = temperature
        self.top_p = top_p
        self.prob_agg = prob_agg
        self.model_name_or_path = model_name_or_path

        if model_name_or_path != 'gpt-3.5-turbo-instruct':
            # Load the tokenizer and model from the given path,
            # enforcing the cache directory to be /home/hice1/yxu846/scratch/models.
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name_or_path,
                cache_dir="/home/hice1/yxu846/scratch/models"
            )

            # Use max_memory and offload_folder to avoid OOM when loading the huge 70B model.
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name_or_path,
                cache_dir="/home/hice1/yxu846/scratch/models",
                device_map="auto",            # Automatically map layers to available devices.
                torch_dtype=torch.float16,      # Use fp16 precision.
                low_cpu_mem_usage=True
            )

            self.generator = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer
            )

    def compute_prob(self, response):
        """
        The Hugging Face text-generation pipeline does not provide token-level log probabilities.
        Here, we return a default probability value.
        """
        return 1.0

    def generate(self, inputs):
        """
        Generate a program based on the input prompt.
        """
        if self.model_name_or_path == 'gpt-3.5-turbo-instruct':
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                prompt=self.prompter(inputs),
                temperature=self.temperature,
                max_tokens=512,
                top_p=self.top_p,
                frequency_penalty=0,
                presence_penalty=0,
                n=1,
                logprobs=1
            )

            prob = self.compute_prob(response)
            prog = response.choices[0]['text'].lstrip('\n').rstrip('\n')
            return prog, prob
        else:
            prompt_text = self.prompter(inputs)
            input_ids = self.tokenizer(prompt_text)["input_ids"]
            generated = self.generator(
                prompt_text,
                max_length=len(input_ids) + 256,  # Safeguard maximum generation length.
                temperature=self.temperature,
                top_p=self.top_p,
                do_sample=True,
                early_stopping=True,
                eos_token_id=self.tokenizer.eos_token_id,  # Let the model stop when it predicts EOS.
                pad_token_id=self.tokenizer.eos_token_id,
            )
            # The pipeline returns a list of dictionaries with a "generated_text" key.
            if generated and "generated_text" in generated[0]:
                full_text = generated[0]["generated_text"].strip()
                # Extract only the generated continuation beyond the prompt.
                prog = full_text[len(prompt_text):].strip().split('\n\n')[0].strip()
            else:
                prog = ""
            prob = self.compute_prob(generated)
            return prog, prob
