
class Color:

    def __init__(self, name: str, hsv_min_1, hsv_max_1, hsv_min2 = None, hsv_max2 = None):
        self._name = name
        self._hsv_min_1 = hsv_min_1
        self._hsv_max_1 = hsv_max_1
        self._hsv_min2 = hsv_min2
        self._hsv_max2 = hsv_max2 

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_hsv_min1(self):
        return self._hsv_min_1
    
    def get_hsv_max1(self):
        return self._hsv_max_1
    
    def get_hsv_min2(self):
        return self._hsv_min2
    
    def get_hsv_max2(self):
        return self._hsv_max2
    
    def set_hsv_min1(self, hsv_min_1):
        self._hsv_min_1 = hsv_min_1
    
    def set_hsv_max1(self, hsv_max_1):
        self._hsv_max_1 = hsv_max_1
    
    def set_hsv_min2(self, hsv_min2):
        self._hsv_min2 = hsv_min2
    
    def set_hsv_max2(self, hsv_max2):
        self._hsv_max2 = hsv_max2
        
class OffColor(Color):

    def __init__(self):
        super().__init__("Off", None, None)

class UnknownColor(Color):
    
    def __init__(self):
        super().__init__("Unknown", None, None)
