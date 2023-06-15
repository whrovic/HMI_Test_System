import cv2
import numpy as np

from .displaycv import Displaycv
from .ledcv import LEDcv
from data.path import Path


class HMIcv():

    @staticmethod
    def led_test(img, led):

        # Cut the image wanted
        img = LEDcv.cut_led(img, led)

        # Get the colors read on the led image
        led_color = LEDcv.read_color(img)

        return led_color 
    
    @staticmethod
    def read_characters(img):

        # Extract display
        display = Displaycv.extract_display(img)
        if display is None:
            return None
        
        # Read characters on the display
        text = Displaycv.read_display(display)

        return text

    @staticmethod
    def display_backlight_test(img):
        
        # Extract the display
        display = Displaycv.extract_display(img)
        if display is None:
            return None

        # Convert image to grayscale
        image_gray = cv2.cvtColor(display, cv2.COLOR_BGR2GRAY)

        # Calculate the average pixel value
        average_brightness = np.mean(image_gray)

        # Check if the average brightness is below the threshold
        threshold = 10
        return average_brightness <= threshold

    @staticmethod
    def display_characters_test(img, model_display):
        
        if model_display is None:
            # TODO: Error Code
            return -1

        # Extract the display
        image_display = Displaycv.extract_display(img)
        if image_display is None:
            # TODO: Error Code
            return -1

        # Compare image_display with model_display
        result = Displaycv.compare_display(image_display, model_display, threshold_avg_ssim=0.93, threshold_min_ssim=0.84, threshold_mse=8)

        return result
    
    @staticmethod
    def display_color_pattern_test(img, model_display):
        
        if model_display is None:
            # TODO: Error Code
            return -1

        # Extract the display
        image_display = Displaycv.extract_display(img)
        if image_display is None:
            # TODO: Error Code
            return -1

        # Compare image_display with model_display
        result = Displaycv.compare_display(image_display, model_display, threshold_avg_ssim=0.87, threshold_min_ssim=0.62, threshold_mse=20)

        return result
    
    @staticmethod
    def read_ref_images_from_file(model_name):
        try:
            chr_ref_img = cv2.imread(Path.get_model_images_directory() + '/' + model_name + '_chr.png')
            pal_ref_img = cv2.imread(Path.get_model_images_directory() + '/' + model_name + '_pal.png')
            return chr_ref_img, pal_ref_img
        except:
            return None, None    