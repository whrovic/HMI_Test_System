from .video_capture import VideoCapture
from abc import ABC, abstractmethod
from threading import Thread
import time

class VideoDevice(VideoCapture, ABC):
    
    _interval: float
    _thread: Thread
    _is_capturing: bool

    def __init__(self, interval=0.5, width=1920, height=1080):
        super().__init__(width, height)

        self._interval = interval
        self._is_capturing = False
        self._thread = Thread(target=self.capture_loop)

    def start_capture(self):
        if not self._is_capturing:
            self._is_capturing = True
            self._thread.start()

    def stop_capture(self):
        self._is_capturing = False
        if self._thread.is_alive():
            self._thread.join()

    def capture_loop(self):
        
        while self._is_capturing:            
            frame = self.get_frame()
            if (frame is not None):
                self._frame_queue.put((frame, time.time()))

            time.sleep(self._interval)
    
    @abstractmethod
    def get_frame(self):
        pass