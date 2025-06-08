# from .step_interpreters import parse_step
import io
import tokenize
import copy
from engine.video import Video
from PIL import Image, ImageDraw, ImageFont
import math, ast

def compute_intersection(p1, p2, p3, p4, eps=1e-6):
    """
    Compute the intersection point (xi, yi) of line segments p1→p2 and p3→p4.
    p1, p2, p3, p4 are tuples/lists (x, y).
    If segments intersect at an interior point, return (xi, yi).
    Otherwise, return None.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < eps:
        return None

    det1 = x1 * y2 - y1 * x2
    det2 = x3 * y4 - y3 * x4
    xi = (det1 * (x3 - x4) - (x1 - x2) * det2) / den
    yi = (det1 * (y3 - y4) - (y1 - y2) * det2) / den

    def on_segment(xi, yi, xa, ya, xb, yb):
        return (min(xa, xb) - eps <= xi <= max(xa, xb) + eps and
                min(ya, yb) - eps <= yi <= max(ya, yb) + eps)

    if on_segment(xi, yi, x1, y1, x2, y2) and on_segment(xi, yi, x3, y3, x4, y4):
        def is_near(a, b, eps=1e-6):
            return abs(a[0] - b[0]) < eps and abs(a[1] - b[1]) < eps

        if is_near((xi, yi), (x1, y1), eps) or is_near((xi, yi), (x2, y2), eps):
            return None
        if is_near((xi, yi), (x3, y3), eps) or is_near((xi, yi), (x4, y4), eps):
            return None

        return (xi, yi)

    return None


def draw_line_with_bridge(draw, existing_segments, x1, y1, x2, y2, bridge_radius=3):
    """
    Draw a straight line from (x1,y1) to (x2,y2). If it crosses any segment
    in existing_segments, insert a small semicircular "bridge" at the intersection
    and continue. Afterwards, add the full (unbroken) segment ((x1,y1),(x2,y2))
    to existing_segments.
    """
    p_start = (x1, y1)
    p_end   = (x2, y2)
    new_seg = (p_start, p_end)

    intersections = []
    for (q_start, q_end) in existing_segments:
        intr = compute_intersection(p_start, p_end, q_start, q_end)
        if intr is not None:
            intersections.append(intr)

    if not intersections:
        draw.line([x1, y1, x2, y2], fill='black', width=1)
        existing_segments.append(new_seg)
        return

    dx = x2 - x1
    dy = y2 - y1
    seg_len = math.hypot(dx, dy)
    if seg_len < 1e-6:
        draw.line([x1, y1, x2, y2], fill='black', width=1)
        existing_segments.append(new_seg)
        return

    ux = dx / seg_len
    uy = dy / seg_len

    def param_t(pt):
        return ((pt[0] - x1) * ux + (pt[1] - y1) * uy) / seg_len

    intr_with_t = [(param_t(pt), pt) for pt in intersections]
    intr_with_t.sort(key=lambda x: x[0])

    current_pt = p_start
    for (t, (xi, yi)) in intr_with_t:
        bx1 = xi - ux * bridge_radius
        by1 = yi - uy * bridge_radius
        draw.line([current_pt[0], current_pt[1], bx1, by1], fill='black', width=1)

        if abs(dy) < abs(dx):
            bbox = [xi - bridge_radius, yi - bridge_radius, xi + bridge_radius, yi + bridge_radius]
            draw.arc(bbox, start=0, end=180, fill='black', width=1)
        else:
            bbox = [xi - bridge_radius, yi - bridge_radius, xi + bridge_radius, yi + bridge_radius]
            draw.arc(bbox, start=270, end=450, fill='black', width=1)

        current_pt = (xi + ux * bridge_radius, yi + uy * bridge_radius)

    draw.line([current_pt[0], current_pt[1], x2, y2], fill='black', width=1)
    existing_segments.append(new_seg)


def parse_step(step_str, partial=False):
    tokens = list(tokenize.generate_tokens(io.StringIO(step_str).readline))
    output_var = tokens[0].string
    step_name = tokens[2].string
    parsed_result = {'output_var': output_var, 'step_name': step_name}
    if partial:
        return parsed_result

    arg_tokens = [tok for tok in tokens[4:-3] if tok.string not in [',', '=']]
    num_tokens = len(arg_tokens) // 2
    args = {}
    for i in range(num_tokens):
        args[arg_tokens[2*i].string] = arg_tokens[2*i + 1].string
    parsed_result['args'] = args
    return parsed_result


class Node:
    def __init__(self, prev=None, prev_method='', value=None):
        if prev is None:
            prev = []
        self.prev = prev
        self.prev_method = prev_method
        self.value = value
        self.next = []

    def __str__(self):
        return f'Node(prev={self.prev}, prev_method={self.prev_method}, value={self.value})'

    def __repr__(self):
        return self.__str__()

    def get_horizontal_for_child(self, node):
        assert node in self.next
        idx = 0
        while idx < len(self.next):
            if self.next[idx] == node:
                break
            idx += 1
        return self.horizontal - self.width // 2 + int((idx + 1) / (len(self.next) + 1) * self.width)


def visualize(program, state, text=None):
    """
    Draw a computation tree from `program` (newline-separated steps) and `state` (mapping variables to Video or values).
    If `text` is provided, wrap it (honoring explicit '\n') to fit within the width of the last layer and draw below, centered.
    """
    # 1) Split lines (skip first if empty)
    program_lines = program.split('\n')[1:]

    # 2) Build Node tree
    tree = {'VIDEO': Node()}
    for line in program_lines:
        parse_result = parse_step(line)
        step_name = parse_result['step_name']
        output_var = parse_result['output_var']

        if step_name == "EVAL":
            expr = eval(parse_result['args']['expr'])
            class NameCollector(ast.NodeVisitor):
                def __init__(self):
                    self.names = set()

                def visit_Name(self, node):
                    # Whenever we see a Name() in the AST, record its id
                    self.names.add(node.id)
                    self.generic_visit(node)

            tree_ast = ast.parse(expr, mode='eval')
            collector = NameCollector()
            collector.visit(tree_ast)

            # 3) Now collector.names is a set of every "bare" identifier from raw_expr
            #    (e.g. {"ANSWER0", "VIDEO0", ...}).  We filter only those already in our tree.
            vars_in_expr = [v for v in collector.names if v in tree]
            for var in vars_in_expr:
                assert var in tree
            tree[output_var] = Node(prev=[tree[var] for var in vars_in_expr], prev_method=expr)
            for var in vars_in_expr:
                tree[var].next.append(tree[output_var])

        elif step_name == "LOC":
            video_var = parse_result['args']['video']
            event = eval(parse_result['args']['event'])
            if event not in tree:
                tree[event] = Node(value=event)
            if video_var not in tree:
                raise RuntimeError(f"Unknown video var: {video_var}")
            tree[output_var] = Node(prev=[tree[video_var], tree[event]], prev_method='LOC')
            tree[video_var].next.append(tree[output_var])
            tree[event].next.append(tree[output_var])

        elif step_name in ('CLIP_BEFORE', 'CLIP_AFTER', 'CLIP'):
            video_var = parse_result['args']['video']
            frame_var = parse_result['args']['frame']
            output_var = parse_result['output_var']
            if video_var not in tree or frame_var not in tree:
                raise RuntimeError(f"Unknown var in {step_name}: {video_var} / {frame_var}")
            tree[output_var] = Node(prev=[tree[video_var], tree[frame_var]], prev_method=step_name)
            tree[video_var].next.append(tree[output_var])
            tree[frame_var].next.append(tree[output_var])

        elif step_name == 'CLIP_AROUND':
            video_var = parse_result['args']['video']
            cf = parse_result['args']['center_frame']
            if cf.isdecimal():
                center_frame_val = eval(cf)
                tree[center_frame_val] = Node(value=center_frame_val)
                center_node = tree[center_frame_val]
            else:
                center_node = tree[cf]
            if video_var not in tree:
                raise RuntimeError(f"Unknown video var: {video_var}")
            tree[output_var] = Node(prev=[tree[video_var], center_node], prev_method='CLIP_AROUND')
            tree[video_var].next.append(tree[output_var])
            center_node.next.append(tree[output_var])

        elif step_name == 'LENGTH':
            video_var = parse_result['args']['video']
            if video_var not in tree:
                raise RuntimeError(f"Unknown video var: {video_var}")
            tree[output_var] = Node(prev=[tree[video_var]], prev_method='LENGTH')
            tree[video_var].next.append(tree[output_var])

        else:
            continue

    # 3) Compute levels for layering
    node_to_name = {node: name for name, node in tree.items()}
    level_cache = {}
    def compute_level(node):
        if node in level_cache:
            return level_cache[node]
        if not node.prev:
            level_cache[node] = 0
            return 0
        prev_lvls = [compute_level(p) for p in node.prev]
        lvl = max(prev_lvls) + 1
        level_cache[node] = lvl
        return lvl

    for node in tree.values():
        compute_level(node)

    max_level = max(level_cache.values(), default=0)
    layers = [[] for _ in range(max_level + 1)]
    for node, lvl in level_cache.items():
        name = node_to_name[node]
        layers[lvl].append(name)

    # 4) Update node.value from state
    for key in tree:
        if key in state:
            tree[key].value = state[key]

    consola_font = ImageFont.truetype("consolas.ttf", 12)
    times_font   = ImageFont.truetype("Times New Roman.ttf", 12)

    # 5) Render each node as image or text box
    for level in layers:
        for name in level:
            node = tree[name]
            if isinstance(node.value, Video):
                node.image = node.value.visualize()
                node.image.thumbnail((480, 480))
                node.width = node.image.width
            else:
                text_str = str(node.value)
                text_w, text_h = times_font.getsize(text_str)
                img = Image.new("RGB", (text_w + 12, text_h + 12), "white")
                draw_txt = ImageDraw.Draw(img)
                draw_txt.text((6, 6), text_str, fill="black", font=times_font)
                node.image = img
                node.width = img.width

    # 6) Compute horizontal centers:
    x_cursor = 20
    for name in layers[0]:
        node = tree[name]
        w, _ = node.image.size
        node.horizontal = x_cursor + w // 2
        x_cursor += w + 20

    for i in range(1, len(layers)):
        for name in layers[i]:
            node = tree[name]
            prev_xs = [p.get_horizontal_for_child(node) for p in node.prev]
            node.horizontal = sum(prev_xs) / len(prev_xs)

    # 7) Compute vertical centers by layer (50px spacing)
    layer_heights = []
    for level in layers:
        heights = [tree[name].image.size[1] for name in level]
        layer_heights.append(max(heights))

    y_cursor = 20
    for i, level in enumerate(layers):
        layer_h = layer_heights[i]
        for name in level:
            node = tree[name]
            node.vertical = y_cursor + layer_h // 2
        y_cursor += layer_h + 50

    # 8) Determine base canvas size (before text)
    all_lefts = []
    all_rights = []
    for name, node in tree.items():
        w, _ = node.image.size
        left = node.horizontal - w // 2
        right = node.horizontal + w // 2
        all_lefts.append(left)
        all_rights.append(right)
    min_left = min(all_lefts)
    max_right = max(all_rights)
    base_width = int(max_right - min_left + 20)
    base_height = int(y_cursor + 20)

    # 9) If text is provided, wrap it (honoring '\n') to fit within last layer’s width
    wrapped_lines = []
    text_block_height = 0
    if text is not None and layers:
        # Split on explicit newlines
        paragraphs = text.split('\n')
        max_box_width = base_width - 20

        # Wrap each paragraph separately
        _, single_h = times_font.getsize("Ay")  # approximate line height
        for para in paragraphs:
            words = para.split()
            if not words:
                # blank line
                wrapped_lines.append("")
                continue

            current_line = ""
            for word in words:
                test_line = word if current_line == "" else f"{current_line} {word}"
                test_w, _ = times_font.getsize(test_line)
                if test_w <= max_box_width:
                    current_line = test_line
                else:
                    wrapped_lines.append(current_line)
                    current_line = word
            if current_line:
                wrapped_lines.append(current_line)

        text_block_height = len(wrapped_lines) * single_h

    # 10) Create canvas, extending height if we have wrapped text
    if text is not None and layers:
        total_height = base_height + 20 + text_block_height
    else:
        total_height = base_height

    canvas = Image.new('RGB', (base_width, total_height), 'white')
    draw = ImageDraw.Draw(canvas)

    # 11) Paste each node’s image onto the canvas
    for name, node in tree.items():
        img = node.image
        w, h = img.size
        x_center = node.horizontal - min_left + 10
        y_center = node.vertical
        top_left = (int(x_center - w // 2), int(y_center - h // 2))
        canvas.paste(img, top_left)

    # 12) Draw edges + annotate prev_method, using bridges for intersections
    existing_segments = []
    for name, node in tree.items():
        if not node.prev:
            continue

        _, node_h = node.image.size
        node_top_y = node.vertical - node_h // 2
        node_x = node.horizontal - min_left + 10

        if len(node.prev) == 1:
            prev_node = node.prev[0]
            pw, ph = prev_node.image.size
            prev_bottom_y = prev_node.vertical + ph // 2
            prev_x = prev_node.get_horizontal_for_child(node) - min_left + 10

            draw_line_with_bridge(
                draw,
                existing_segments,
                prev_x,
                prev_bottom_y,
                node_x,
                node_top_y
            )

            mid_x = (prev_x + node_x) / 2
            mid_y = (prev_bottom_y + node_top_y) / 2
            draw.text((mid_x + 2, mid_y - 10), node.prev_method, fill='black', font=consola_font)

        else:
            prev_xs = []
            prev_bottom_ys = []
            for prev_node in node.prev:
                pw, ph = prev_node.image.size
                prev_bottom_y = prev_node.vertical + ph // 2
                prev_x = prev_node.get_horizontal_for_child(node) - min_left + 10
                prev_xs.append(prev_x)
                prev_bottom_ys.append(prev_bottom_y)

            sep_y = max(prev_bottom_ys) + 10

            for idx, prev_node in enumerate(node.prev):
                px = prev_xs[idx]
                py0 = prev_bottom_ys[idx]
                py1 = sep_y
                draw_line_with_bridge(
                    draw,
                    existing_segments,
                    px, py0,
                    px, py1
                )

            min_x = min(prev_xs)
            max_x = max(prev_xs)
            draw_line_with_bridge(
                draw,
                existing_segments,
                min_x, sep_y,
                max_x, sep_y
            )

            mid_x = (min_x + max_x) / 2
            draw_line_with_bridge(
                draw,
                existing_segments,
                mid_x, sep_y,
                node_x, node_top_y
            )

            text_y_mid = sep_y + (node_top_y - sep_y) / 2 - 10
            draw.text((mid_x + 2, text_y_mid), node.prev_method, fill='black', font=consola_font)

    # 13) Draw wrapped text block, if any, centered under last layer
    if text is not None and layers:
        center_x_canvas = (sum(tree[name].horizontal for name in layers[-1]) / len(layers[-1])) - min_left + 10
        _, single_h = times_font.getsize("Ay")
        last_layer_h = layer_heights[-1]
        last_layer_center = tree[layers[-1][0]].vertical
        bottom_y = last_layer_center + last_layer_h // 2

        for i, line in enumerate(wrapped_lines):
            line_w, _ = times_font.getsize(line)
            text_x = center_x_canvas - (line_w / 2)
            line_y = bottom_y + 20 + i * single_h
            draw.text((text_x, line_y), line, fill='black', font=times_font)

    return canvas
