class Parameter:

    def __init__(self, width = 1920, height = 1080, auto_focus = 1.0, manual_focus = 0,
                 auto_exposure = 1.0, exposure = 0, gain = 0,
                 auto_white_balance = 1.0, white_balance = 3500,
                 brightness = 128, contrast = 128, saturation = 128, sharpness = 128):
        self._width = width
        self._height = height
        self._auto_focus = auto_focus
        self._manual_focus = manual_focus
        self._auto_exposure = auto_exposure
        self._exposure = exposure
        self._gain = gain
        self._auto_white_balance = auto_white_balance
        self._white_balance = white_balance
        self._brightness = brightness
        self._contrast = contrast
        self._saturation = saturation
        self._sharpness = sharpness
    
    def get_parameters(self):
        parameters = {
            "width": self._width,
            "height": self._height,
            "auto_focus": self._auto_focus,
            "manual_focus": self._manual_focus,
            "auto_exposure": self._auto_exposure,
            "exposure": self._exposure,
            "gain": self._gain, 
            "auto_white_balance": self._auto_white_balance,
            "white_balance": self._white_balance,
            "brightness": self._brightness,
            "contrast": self._contrast,
            "saturation": self._saturation,
            "sharpness": self._sharpness
        }
        return parameters
    