from video.video_capture import VideoCapture
import cv2
from data.path import Path
import numpy as np
import os

class ImageFiles(VideoCapture):

    _path: list

    def __init__(self, path, width=1920, height=1080):
        super().__init__(width, height)

        self.set_path(path)

    def set_path(self, path):
        resources_path = Path.get_resources_directory()
        self._path = [os.path.join(resources_path, p) for p in path]

    def start_capture(self):
        
        for p in self._path:
            img = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self._frame_queue.put(img)
            
    def stop_capture(self):
        pass