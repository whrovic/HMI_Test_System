import numpy as np
from .ledcv import LEDcv
from data.model.display import Display
from .displaycv import Displaycv

class HMIcv():

    def led_test(img, led):
        # Cut the image wanted
        img = LEDcv.cut_led(img, led)

        # Get the colors read on the led image
        led_color = LEDcv.read_color(img)

        return led_color 
        
    def display_characters_test(img, model_display: Display):
        # Create an instance of the Displaycv class
        displaycv = Displaycv()

        # Cut display from HMI image
        display = displaycv.cut_display(img, model_display)

        # Read character pattern from display
        character_pattern = displaycv.read_char(display)

        # Compare character pattern from image and model and return the result  
        if (character_pattern == model_display.get_char):
            return True
        else:
            return False
    
    def display_backlight_test(img, model_display: Display):
        # Create an instance of the Displaycv class
        displaycv = Displaycv()

        # Cut display from HMI image
        display = displaycv.cut_display(img, model_display)

        # Get color pattern from display
        color_pattern = displaycv.get_color_pattern(display)

        # Verify if each color is black within a tolerance range of 5
        result = True
        for i in range(len(color_pattern)):
            if not np.allclose(color_pattern[i], [0,0,0], atol=5):
                result = False
                break
        
        # Return the result
        return result
    
    def display_color_pattern_test(img, model_display: Display):
        # Create an instance of the Displaycv class
        displaycv = Displaycv()

        # Cut display from HMI image
        display = displaycv.cut_display(img, model_display)

        # Get color pattern from display
        color_pattern = displaycv.get_color_pattern(display)

        # Get color pattern from model
        model_color_pattern = model_display.get_color_vector()

        # Compare the two color patterns within a tolerance range of 5
        result = True
        for i in range(len(color_pattern)):
            if not np.allclose(color_pattern[i], model_color_pattern[i], atol=5):
                result = False
                break
        
        # Return the result of the comparison
        return result
