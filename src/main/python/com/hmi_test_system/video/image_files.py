import os

import cv2
import numpy as np
from data.path import Path
from video.video_capture import VideoCapture


class ImageFiles(VideoCapture):

    _path: list

    def __init__(self, path, width=1920, height=1080):
        super().__init__(width, height)

        self._path = [os.path.join(Path.get_resources_directory(), p) for p in path]

    def start_capture(self):
        for p in self._path:
            img = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self._frame_queue.put(img)
            
    def stop_capture(self):
        pass
