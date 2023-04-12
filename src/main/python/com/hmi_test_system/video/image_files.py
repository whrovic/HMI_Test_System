from video.video_capture import VideoCapture
import cv2
from pathlib import Path
import numpy as np

class ImageFiles(VideoCapture):

    path: list
    width: int
    height: int

    def __init__(self, path, width=1920, height=1080):
        super().__init__(width, height)

        self.set_path(path)

    def set_path(self, path):
        cwd = Path.cwd().parent
        resources_path = (cwd / "../../../resources").resolve()

        self.path = [(resources_path / p).resolve() for p in path]

    def start_capture(self):
        
        for p in self.path:
            #img = cv2.imread(i)
            img = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self.frame_queue.put(img)
            
    def stop_capture(self):
        pass