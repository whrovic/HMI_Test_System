class Color:

    def __init__(self, name, hsv_min_1, hsv_max_1, hsv_min2 = None, hsv_max2 = None):
        self._name = name
        self._hsv_min_1 = hsv_min_1
        self._hsv_max_1 = hsv_max_1
        self._hsv_min2 = hsv_min2
        self._hsv_max2 = hsv_max2

class OffColor(Color):
    def __init__(self):
        super().__init__("Off", None, None, None, None)