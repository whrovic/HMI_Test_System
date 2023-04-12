from video.video_device import VideoDevice

class Camera(VideoDevice):

    _device_id: int

    def __init__(self, width=1920, height=1080):
        super().__init__(width, height)
        pass

    def get_frame(self):
        pass