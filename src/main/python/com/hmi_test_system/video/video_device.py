from video.video_capture import VideoCapture
from abc import ABC, abstractmethod
from threading import Thread
import cv2

class VideoDevice(VideoCapture, ABC):
    
    _interval: int
    _thread: Thread
    _is_capturing: bool
    _cap: cv2.VideoCapture

    def __init__(self, width=1920, height=1080):
        super().__init__(width, height)
        pass

    def start_capture(self):
        pass

    def stop_capture(self):
        pass

    def capture_loop(self):
        pass
    
    @abstractmethod
    def get_frame(self):
        pass
