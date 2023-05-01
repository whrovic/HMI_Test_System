import numpy as np
from LEDcv import LEDcv
from data.color.color import OffColor

class HMIcv():

    def led_test(img, led):

        #cut the image wanted
        img = LEDcv.cut_led(img, led)

        #get the colors read on the led image
        led_color = LEDcv.read_led_color(img, led)

        return led_color 
        
       
    
    def display_characters_test(img, lcd):
        return False
    
    def display_backlight_test(img, lcd):
        return False
    
    def display_color_pattern_test(img, lcd):
        return False