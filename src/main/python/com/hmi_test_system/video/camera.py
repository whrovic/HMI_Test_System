from .video_device import VideoDevice
import cv2

class Camera(VideoDevice):

    _device_id: int

    def __init__(self, device=0, interval=0.5, width=1920, height=1080):
        super().__init__(interval, width, height)

        self._cap = cv2.VideoCapture(device)

    def get_frame(self):
        _, frame = self._cap.read()
        return frame