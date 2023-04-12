import queue
from abc import ABC, abstractmethod

class VideoCapture(ABC):

    _width: int
    _height: int

    def __init__(self, width=1920, height=1080):
        self._frame_queue = queue.Queue()
        self._width = width
        self._height = height

    def get_image(self):
        if (self._frame_queue.empty()):
            return None
        else:
            return self._frame_queue.get()
    
    def clear_queue(self):
        self._frame_queue.queue.clear()

    @abstractmethod
    def start_capture(self):
        pass

    @abstractmethod
    def stop_capture(self):
        pass
