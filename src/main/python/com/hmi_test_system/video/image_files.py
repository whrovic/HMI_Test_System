from video.video_capture import VideoCapture
import cv2
from pathlib import Path
import numpy as np

class ImageFiles(VideoCapture):

    _path: list

    def __init__(self, path, width=1920, height=1080):
        super().__init__(width, height)

        self.set_path(path)

    def set_path(self, path):
        cwd = Path.cwd()
        resources_path = (cwd / "C:/Users/filip/Desktop/ES/HMI_Test_System/src/main/resources").resolve()

        self._path = [(resources_path / p).resolve() for p in path]

    def start_capture(self):
        
        for p in self._path:
            #img = cv2.imread(i)
            img = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self._frame_queue.put(img)
            
    def stop_capture(self):
        pass