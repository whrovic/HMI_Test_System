from video.video_device import VideoDevice
from pathlib import Path
import cv2

class VideoFile(VideoDevice):

    _path: str
    _frame_count: int
    _frames_per_second: float
    _current_frame: int

    def __init__(self, device, interval=0.5, width=1920, height=1080):
        super().__init__(device, interval, width, height)

        self.set_path(device)

        self._frame_count = self._cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self._frames_per_second = self._cap.get(cv2.CAP_PROP_FPS)
        self._current_frame = 0

    def set_path(self, path):
        cwd = Path.cwd().parent
        resources_path = (cwd / "../../../resources").resolve()

        self._path = str((resources_path / path).resolve())
        self._cap = cv2.VideoCapture(self._path)

    def get_frame(self):
        if (self._current_frame > self._frame_count):
            return None
        else:
            _, frame = self._cap.read()
            frame = self.resize_frame(frame)

            self.move_cursor()

            return frame

    def move_cursor(self):
        self._current_frame = int(self._current_frame + self._interval * self._frames_per_second)
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)

    def resize_frame(self, frame):
        (h, w) = frame.shape[:2]

        if (h < w):
            return cv2.resize(frame, (self._width, self._height))
        else:
            return cv2.resize(frame, (int(w*self._height / h), self._height), interpolation=cv2.INTER_AREA)
