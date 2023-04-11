from video_capture import VideoCapture
import cv2

class ImageFiles(VideoCapture):

    path: tuple

    def __init__(self, width, height, path):
        super().__init__(width, height)
        self.path = path

    def start_capture(self):
        
        for i in self.path:
            img = cv2.imread(i)
            self.frame_queue.put(img)
            
    def stop_capture(self):
        pass
