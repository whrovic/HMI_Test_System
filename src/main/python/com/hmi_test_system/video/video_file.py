from video.video_device import VideoDevice

class VideoFile(VideoDevice):

    _path: str
    _frame_count: int
    _frames_per_second: int
    _current_frame: int

    def __init__(self, width=1920, height=1080):
        super().__init__(width, height)
        pass

    def get_frame(self):
        pass