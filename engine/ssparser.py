# from .step_interpreters import parse_step
import io
import tokenize
import copy

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

def fix(program, question, module_list, state_dict = {"VIDEO": None}):
    state_dict = copy.deepcopy(state_dict)
    lines =program.split('\n')
    program_lines = program.split('\n')
    TEMPORAL_EQUIVALENCE_GROUPS = [
        {"before", "prior", "earlier"},
        {"after", "later", "subsequently"},
        {"while", "as", "when", "during"}
    ]
    flag_line = program_lines[0]
    parse_result = parse_step(flag_line)
    flag_start = False
    flag_middle = False
    flag_end = False
    if parse_result['args']['begin'] != 'None' and '[' in parse_result['args']['begin']:
        flag_start = True
    if parse_result['args']['middle'] != 'None' and '[' in parse_result['args']['middle']:
        flag_middle = True
    if parse_result['args']['end'] != 'None' and '[' in parse_result['args']['end']:
        flag_end = True
    for i, line in enumerate(program_lines):
        if lines[i] != line:
            line = lines[i]
        parse_result = parse_step(line)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']
        if step_name not in module_list:
            # print(f"Invalid step name: {step_name}")
            return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
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
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
        elif step_name == "LOC":
            video_var = parse_result['args']['video']
            event = parse_result['args']['event']
            output_var = parse_result['output_var']
            if video_var not in state_dict:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            state_dict[output_var] = [0,0]
        elif step_name == "FLAG":
            if 'begin' not in parse_result['args'] or 'middle' not in parse_result['args'] or 'end' not in parse_result['args']:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            state_dict[output_var] = {}
        elif step_name == 'CLIP_BEFORE':
            video_var = parse_result['args']['video']
            frame_var = parse_result['args']['frame']
            output_var = parse_result['output_var']
            if video_var not in state_dict or frame_var not in state_dict:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            words = question.lower().split()
            if len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[0])) == 0 and len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[1])) + len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[2])) > 0:
                if len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[1])) == 0:
                    lines[i] = line.replace('CLIP_BEFORE', 'CLIP')
                elif len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[2])) == 0:
                    lines[i] = line.replace('CLIP_BEFORE', 'CLIP_AFTER')
                else:
                    return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            elif len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[0])) == 0:
                lines[i] = line.replace('CLIP_BEFORE', 'CLIP')
            state_dict[output_var] = state_dict['VIDEO']
        elif step_name == 'CLIP_AFTER':
            video_var = parse_result['args']['video']
            frame_var = parse_result['args']['frame']
            output_var = parse_result['output_var']
            if video_var not in state_dict or frame_var not in state_dict:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            words = question.lower().split()
            if len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[1])) == 0 and len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[0])) + len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[2])) > 0:
                if len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[0])) == 0:
                    lines[i] = line.replace('CLIP_AFTER', 'CLIP')
                elif len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[2])) == 0:
                    lines[i] = line.replace('CLIP_AFTER', 'CLIP_BEFORE')
                else:
                    return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            elif len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[1])) == 0:
                lines[i] = line.replace('CLIP_AFTER', 'CLIP')
            state_dict[output_var] = state_dict['VIDEO']
        elif step_name == 'CLIP':
            if 'frame' not in parse_result['args'] or 'video' not in parse_result['args']:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            video_var = parse_result['args']['video']
            frame_var = parse_result['args']['frame']
            output_var = parse_result['output_var']
            if video_var not in state_dict or frame_var not in state_dict:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            words = question.lower().split()
            if len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[2])) == 0 and len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[1])) + len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[0])) > 0:
                if len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[1])) == 0:
                    lines[i] = line.replace('CLIP', 'CLIP_BEFORE')
                elif len(set(words).intersection(TEMPORAL_EQUIVALENCE_GROUPS[0])) == 0:
                    lines[i] = line.replace('CLIP', 'CLIP_AFTER')
                else:
                    return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            state_dict[output_var] = state_dict['VIDEO']
        elif step_name == 'VQA' or step_name == 'VIDQA' or step_name == 'CAP':
            video_var = parse_result['args']['video']
            output_var = parse_result['output_var']
            if video_var not in state_dict:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            state_dict[output_var] = []
        elif step_name == 'CLIP_AROUND':
            video_var = parse_result['args']['video']
            center_frame = eval(parse_result['args']['center_frame']) if parse_result['args']['center_frame'].isdecimal() else state_dict[parse_result['args']['center_frame']]
            output_var = parse_result['output_var']
            if flag_start == False and flag_middle == False and flag_end == False:
                lines[i] = f"{output_var}=CLIP_AROUND(video={video_var},center_frame={center_frame},invalid=True)"
            if video_var not in state_dict or center_frame < -1:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            state_dict[output_var] = state_dict['VIDEO']
        elif step_name == 'LENGTH':
            video_var = parse_result['args']['video']
            output_var = parse_result['output_var']
            if video_var not in state_dict:
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            state_dict[output_var] = 0
        elif step_name == "SELECT":
            choices_var = parse_result['args']['choices']
            info_var = parse_result['args']['information']
            if choices_var not in state_dict or info_var not in state_dict:
                # print(f"Invalid var: {line}")
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            output_var = parse_result['output_var']
            state_dict[output_var] = ''
        elif step_name == "RESULT":
            var = parse_result['args']['var']
            if var not in state_dict:
                # print(f"Invalid var: {line}")
                return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
            output_var = parse_result['output_var']
            state_dict[output_var] = state_dict[var]
        else:
            # print(f"Invalid step name: {step_name}")
            return f"""ANSWERS0=VQA(video=VIDEO,question=\"{question}\")"""
    program = '\n'.join(lines)
    return program
