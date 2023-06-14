from time import sleep

import cv2

from .video_device import VideoDevice


class Camera(VideoDevice):

    _device_id: int

    def __init__(self, device=0, interval=0.5, width=1280, height=720):
        super().__init__(interval, width, height)

        self._device_id = device
        self._cap = cv2.VideoCapture(device, cv2.CAP_DSHOW)
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def get_frame(self):
        _, frame = self._cap.read()
        return frame

    def set_settings(self, settings: dict[str, any]):

        ret_val = True

        if settings is None:
            settings = {}
        
        width = settings.get('width', 1280)
        height = settings.get('height', 720)
        auto_focus = settings.get('auto_focus', 1.0)
        manual_focus = settings.get('manual_focus', 1.0)
        auto_exposure = settings.get('auto_exposure', 1.0)
        exposure = settings.get('exposure', 0)
        gain = settings.get('gain', 0)
        auto_white_balance = settings.get('auto_white_balance', 1.0)
        white_balance = settings.get('white_balance', 4000)
        brightness = settings.get('brightness', 128)
        contrast = settings.get('contrast', 128)
        saturation = settings.get('saturation', 128)
        sharpness = settings.get('sharpness', 128)

        if not self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, width): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_AUTOFOCUS, auto_focus): ret_val = False
        if not auto_focus:
            if not self._cap.set(cv2.CAP_PROP_FOCUS, manual_focus): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, auto_exposure): ret_val = False
        if not auto_exposure:
            if not self._cap.set(cv2.CAP_PROP_EXPOSURE, exposure): ret_val = False
            if not self._cap.set(cv2.CAP_PROP_GAIN, gain): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_AUTO_WB, auto_white_balance): ret_val = False
        if not auto_white_balance:
            if not self._cap.set(cv2.CAP_PROP_WB_TEMPERATURE, white_balance): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_CONTRAST, contrast): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_SATURATION, saturation): ret_val = False
        if not self._cap.set(cv2.CAP_PROP_SHARPNESS, sharpness): ret_val = False

        sleep(0.5)

        return ret_val

    def closed(self):
        return ((self._cap is None) or (not self._cap.isOpened()))
    
    def close(self):
        self.stop_capture()
        self.clear_queue()
        if self._cap is not None:
            self._cap.release()
    