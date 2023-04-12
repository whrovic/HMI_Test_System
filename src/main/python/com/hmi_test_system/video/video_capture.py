import queue
from abc import ABC, abstractmethod

class VideoCapture(ABC):

    width: int
    height: int

    def __init__(self, width=1920, height=1080):
        self.frame_queue = queue.Queue()
        self.width = width
        self.height = height

    def get_image(self):
        if (self.frame_queue.empty()):
            return None
        else:
            return self.frame_queue.get()
    
    def clear_queue(self):
        self.frame_queue.queue.clear()

    @abstractmethod
    def start_capture(self):
        pass

    @abstractmethod
    def stop_capture(self):
        pass
