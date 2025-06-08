import cv2
import math
from moviepy import VideoFileClip
from PIL import Image, ImageDraw, ImageFont, ImageOps

class Video:
    def __init__(self, file_path, clip_start=0.0, clip_end=None):
        """
        Initialize the Video object with the file path and clip boundaries.
        If clip_end is not provided, it is set to the total video length.
        """
        self.file_path = file_path
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {file_path}")
        self.fps = cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        total_time = self.frame_count / self.fps

        # Ensure the clip boundaries are valid.
        if clip_end is None or clip_end > total_time:
            clip_end = total_time
        if clip_start < 0 or clip_start > clip_end:
            raise ValueError("Invalid clip start and end times.")
            
        self.clip_start = clip_start
        self.clip_end = clip_end
        cap.release()

    @classmethod
    def read_file(cls, file_path):
        """
        Reads an MP4 file and returns a Video object representing the full video.
        """
        return cls(file_path)

    def get_video_length(self):
        """
        Returns the length of the video clip (in seconds) as a floating point number.
        For a full video, this is the total duration; for a clipped video,
        it is the duration of the clip (clip_end - clip_start).
        """
        return self.clip_end - self.clip_start

    def clip(self, start, end):
        """
        Clips the video and returns a new Video object representing only the portion
        from 'start' seconds to 'end' seconds relative to the current clip.
        
        Args:
            start (float): The starting second (relative to the current clip, starting at 0).
            end (float): The ending second (relative to the current clip).
        
        Returns:
            Video: A new Video object representing the clipped portion.
            
        Raises:
            ValueError: If the provided times are out of bounds.
        """
        if start < 0 or start > end:
            raise ValueError("Invalid clipping times.")
        if end > self.get_video_length():
            end = self.get_video_length()
        new_clip_start = self.clip_start + start
        new_clip_end = self.clip_start + end
        return Video(self.file_path, clip_start=new_clip_start, clip_end=new_clip_end)

    def extract_frame(self, t):
        """
        Extracts a frame from the video at time 't' seconds (relative to the clip start)
        and returns it as a Pillow Image in RGB format.
        
        Args:
            t (float): The time in seconds (relative to the current clip) at which
                       the frame will be extracted.
        
        Returns:
            PIL.Image.Image: The extracted frame as an image in RGB format.
        
        Raises:
            ValueError: If t is outside the duration of the current clip or frame extraction fails.
        """
        if t < 0 or t > self.get_video_length():
            raise ValueError("t is outside video length.")
        
        # The actual timestamp in the underlying video file:
        actual_time = self.clip_start + t

        # Open the video file and set the read pointer to the desired time (in milliseconds).
        cap = cv2.VideoCapture(self.file_path)
        cap.set(cv2.CAP_PROP_POS_MSEC, actual_time * 1000)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            raise ValueError(f"Failed to extract frame at {actual_time} seconds.")
        
        # Convert the image from BGR (OpenCV's default) to RGB and create a Pillow Image.
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return Image.fromarray(frame_rgb)

    def extract_frames(self):
        """
        Extracts frames every 1 second from the beginning of the clip until the end,
        and returns a tuple containing:
          - A list of Pillow Images (RGB) for the extracted frames.
          - A list of time stamps (in seconds) at which the frames were extracted.
        
        For example, if the clip is 10 seconds long, frames are extracted at
        t = 0, 1, 2, ..., 10 seconds (11 frames total).
        
        Returns:
            tuple: (list of PIL.Image.Image, list of int)
        """
        duration = self.get_video_length()
        frames = []
        times = []
        # Extract frames at each integer second
        for sec in range(math.ceil(duration)):
            try:
                img = self.extract_frame(sec)
                frames.append(img)
                times.append(sec)
            except:
                pass
        return frames, times
    def extract_all_frames(self, max_frame_num=16):
        """
        Uniformly sample frames across the clip. The total number of frames
        sampled is max(ceil(duration), min(total_frames_in_clip, 16)),
        where total_frames_in_clip = fps * duration.

        Returns:
          - List of PIL.Image frames (RGB)
          - List of timestamps (in seconds) at which each frame was extracted
        """
        duration = self.get_video_length()
        if duration <= 0:
            return [], []

        # approximate total frames in this clip
        total_frames_in_clip = int(self.fps * duration)

        # compute how many to sample
        num_samples = max(
            min(math.ceil(duration * 2), max_frame_num),
            min(total_frames_in_clip, max_frame_num)
        )

        # if only one sample, just take t=0
        if num_samples == 1:
            try:
                img = self.extract_frame(0.0)
                return [img], [0.0]
            except ValueError:
                return [], []

        frames = []
        times = []

        # pick evenly‐spaced times between 0 and duration
        for i in range(num_samples):
            t = (i / (num_samples - 1)) * (duration - 1e-2)
            try:
                img = self.extract_frame(t)
                frames.append(img)
                times.append(t)
            except ValueError:
                break

        return frames, times

    def save(self, file_path, fps: float = None):
        """
        Saves the video clip (from self.clip_start to self.clip_end) to the specified file path.
        If fps is None, uses a fast sequential copy at the original frame rate.
        Otherwise falls back to your per-frame time-seek/resample logic.
        """
        # 1) open source to grab properties
        cap0 = cv2.VideoCapture(self.file_path)
        if not cap0.isOpened():
            raise ValueError(f"Failed to open video file: {self.file_path}")
        orig_fps = cap0.get(cv2.CAP_PROP_FPS)
        width   = int(cap0.get(cv2.CAP_PROP_FRAME_WIDTH))
        height  = int(cap0.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap0.release()

        # 2) decide output fps
        use_orig = fps is None
        fps_out  = orig_fps if use_orig else fps
        if fps_out <= 0:
            raise ValueError("fps must be > 0")

        # 3) prepare writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out    = cv2.VideoWriter(file_path, fourcc, fps_out, (width, height))

        # compute frame indices
        start_frame = int(math.floor(self.clip_start * orig_fps))
        end_frame   = int(math.ceil (self.clip_end   * orig_fps))

        cap = cv2.VideoCapture(self.file_path)
        if not cap.isOpened():
            raise ValueError(f"Failed to reopen video file: {self.file_path}")

        if use_orig:
            # ---- FAST PATH: sequential copy at original FPS ----
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            for _ in range(end_frame - start_frame):
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

        else:
            # ---- FALLBACK: resample at new FPS via time-based seeks ----
            duration   = self.clip_end - self.clip_start
            num_frames = max(1, math.ceil(duration * fps_out))
            for i in range(num_frames):
                t_rel = (i / fps_out)
                cap.set(cv2.CAP_PROP_POS_MSEC, (self.clip_start + t_rel) * 1000)
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

        cap.release()
        out.release()
    def make_montage(self, frames, start_sec):
        padding, border = 20, 5
        extra_gap = padding * 3
        bg = (255, 255, 255)

        w, h = frames[0][1].size
        n = len(frames)

        # label area height and font
        label_h = int(h * 0.2)
        font_sz = max(32, int(label_h * 0.8))
        font    = ImageFont.truetype("arial.ttf", font_sz)

        total_w = padding + n*(w + 2*border) + (extra_gap if n>4 else 0) + padding
        total_h = padding + h + 2*border + label_h + padding

        canvas = Image.new("RGB", (total_w, total_h), bg)
        draw   = ImageDraw.Draw(canvas)

        x_off = padding
        edges = []
        for i, (t_rel, img) in enumerate(frames):
            # white frame
            frame_box = [x_off, padding, x_off + w + 2*border, padding + h + 2*border]
            draw.rectangle(frame_box, fill=(255,255,255))
            canvas.paste(img, (x_off+border, padding+border))

            L = x_off + border
            R = L + w
            edges.append((L, R))

            # timestamp label
            actual = start_sec + t_rel
            lbl    = f"{actual:.0f}s"
            bb     = draw.textbbox((0,0), lbl, font=font)
            tw, th = bb[2]-bb[0], bb[3]-bb[1]
            lx = x_off + (w + 2*border - tw)//2
            ly = padding + h + 2*border + (label_h - th)//2
            draw.text((lx, ly), lbl, fill=(0,0,0), font=font)

            x_off += w + 2*border
            if i == 2 and n > 4:
                x_off += extra_gap

        # draw “…” in the big gap
        if n > 4:
            r3 = edges[2][1]
            l4 = edges[3][0]
            mid = (r3 + l4)//2
            ell = "…"
            ebb = draw.textbbox((0,0), ell, font=font)
            tw_ell = ebb[2]-ebb[0]
            xpos = mid - tw_ell//2
            ypos = padding + border + (h//2) - (font_sz//2)
            draw.text((xpos, ypos), ell, fill=(0,0,0), font=font)

        return canvas

    def add_filmframe(self, montage):
        # ── tweak these ───────────────────────────────
        hole_h     = 20    # height of each hole band
        hole_w     = 8     # width of each black hole (thinner)
        hole_gap   = 20    # gap between holes (wider white spacer)
        line_thick = 4     # thickness of each solid line

        line_col = (0, 0, 0)         # black for lines & holes
        bg_color = (255, 255, 255)   # white background

        mw, mh = montage.size
        fw = mw
        # total height = top line + top holes + mid line + image +
        #                lower line + bottom holes + bottom line
        fh = ( line_thick
            + hole_h
            + line_thick
            + mh
            + line_thick
            + hole_h
            + line_thick )

        film = Image.new("RGB", (fw, fh), bg_color)
        draw = ImageDraw.Draw(film)

        y = 0
        # 1) Top solid line
        draw.rectangle([0, y, fw, y + line_thick], fill=line_col)

        # 2) Top hole band
        y += line_thick
        count   = fw // (hole_w + hole_gap)
        total_w = count * hole_w + (count - 1) * hole_gap
        x0      = (fw - total_w) // 2
        for i in range(count):
            x = x0 + i * (hole_w + hole_gap)
            draw.rectangle([x, y, x + hole_w, y + hole_h], fill=line_col)

        # 3) Middle solid line
        y += hole_h
        draw.rectangle([0, y, fw, y + line_thick], fill=line_col)

        # 4) Paste montage
        y += line_thick
        film.paste(montage, (0, y))

        # 5) Lower solid line (below montage)
        y += mh
        draw.rectangle([0, y, fw, y + line_thick], fill=line_col)

        # 6) Bottom hole band
        y += line_thick
        for i in range(count):
            x = x0 + i * (hole_w + hole_gap)
            draw.rectangle([x, y, x + hole_w, y + hole_h], fill=line_col)

        # 7) Bottom solid line
        y += hole_h
        draw.rectangle([0, y, fw, y + line_thick], fill=line_col)

        return film

    def visualize(self):
        clip   = VideoFileClip(self.file_path).subclipped(self.clip_start, self.clip_end)
        ints = list(range(int(clip.duration) + 1))
        times = ints if len(ints) <= 5 else ints[:3] + ints[-2:]
        frames = [(t, Image.fromarray(clip.get_frame(t))) for t in times]

        montage = self.make_montage(frames, self.clip_start)
        film    = self.add_filmframe(montage)
        return film


