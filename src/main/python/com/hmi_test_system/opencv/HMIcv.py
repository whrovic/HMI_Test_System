import numpy as np
from LEDcv import LEDcv

class HMIcv():

    def led_test(img, led):
        return False
        #get the colors read on the led imagd
        led_colors = LEDcv.read_led_color(img, leds)
        #compare the colors obtained with the expected ones
        if np.array_equal(led_colors, expected):
            return True
        else:
            return False
    
    def display_characters_test(img, lcd):
        return False
    
    def display_backlight_test(img, lcd):
        return False
    
    def display_color_pattern_test(img, lcd):
        return False