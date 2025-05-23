import cv2
from PIL import Image
import math

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
    def extract_all_frames(self):
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
            math.ceil(duration),
            min(total_frames_in_clip, 16)
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
            t = (i / (num_samples - 1)) * duration
            try:
                img = self.extract_frame(t)
                frames.append(img)
                times.append(t)
            except ValueError:
                break

        return frames, times

    def save(self, file_path, fps: float = None):
        """
        Saves the video clip (from self.clip_start to self.clip_end) to the specified file path,
        at the given fps (frames per second). If fps is None, uses the original video's fps.
        Playback speed remains the same; we simply sample at the new rate.

        Args:
            file_path (str): Where to write the clip.
            fps (float, optional): Desired output frame rate. Defaults to original fps.
        """
        # 1) open source just to grab frame size
        cap = cv2.VideoCapture(self.file_path)
        if not cap.isOpened():
            raise ValueError(f"Failed to open video file: {self.file_path}")
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()

        # 2) decide output fps
        fps_out = self.fps if fps is None else fps
        if fps_out <= 0:
            raise ValueError("fps must be > 0")

        # 3) set up writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out    = cv2.VideoWriter(file_path, fourcc, fps_out, (width, height))

        # 4) compute how many frames to emit
        duration    = self.clip_end - self.clip_start
        num_frames  = max(1, math.ceil(duration * fps_out))

        # 5) reopen cap for sampling
        cap = cv2.VideoCapture(self.file_path)
        if not cap.isOpened():
            raise ValueError(f"Failed to reopen video file: {self.file_path}")

        for i in range(num_frames):
            # time offset within clip
            t_rel = i / fps_out
            # clamp at end
            if t_rel > duration:
                t_rel = duration

            # seek and read
            cap.set(cv2.CAP_PROP_POS_MSEC, (self.clip_start + t_rel) * 1000)
            ret, frame = cap.read()
            if not ret:
                break

            out.write(frame)

        # 6) clean up
        cap.release()
        out.release()


