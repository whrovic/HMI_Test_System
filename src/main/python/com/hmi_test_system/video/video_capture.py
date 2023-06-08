import queue
from abc import ABC, abstractmethod

import cv2


class VideoCapture(ABC):

    _width: int
    _height: int

    def __init__(self, width=1920, height=1080):
        self._frame_queue = queue.Queue()
        self._width = width
        self._height = height

    def get_image(self):
        if (self._frame_queue.empty()):
            return None, None
        else:
            return self._frame_queue.get()
    
    def clear_queue(self):
        self._frame_queue.queue.clear()

    @staticmethod
    def list_available_cameras():
        cameras = []
        
        i = 0
        while (True):
            cap = cv2.VideoCapture(i)
            if (cap is not None and cap.isOpened()):
                cameras.append((i, cap.get(cv2.CAP_PROP_BACKEND)))
                i += 1
            else:
                break

        return cameras
        
    @abstractmethod
    def start_capture(self):
        pass

    @abstractmethod
    def stop_capture(self):
        pass
