import os

import cv2
from data.path import Path
from video.video_device import VideoDevice


class VideoFile(VideoDevice):

    _path: str
    _frame_count: int
    _frames_per_second: float
    _current_frame: int

    def __init__(self, path, interval=0.5, width=1920, height=1080):
        super().__init__(interval, width, height)

        self._path = os.path.join(Path.get_resources_directory(), path)

        self._cap = cv2.VideoCapture(self._path)
        self._frame_count = self._cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self._frames_per_second = self._cap.get(cv2.CAP_PROP_FPS)
        self._current_frame = 0

    def get_frame(self):
        if (self._current_frame > self._frame_count):
            return None
        else:
            _, frame = self._cap.read()

            self._move_cursor()

            return frame

    def _move_cursor(self):
        self._current_frame = int(self._current_frame + self._interval * self._frames_per_second)
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, self._current_frame)
