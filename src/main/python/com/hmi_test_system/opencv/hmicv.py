import cv2
import numpy as np
from data.model.display import Display
from skimage.metrics import structural_similarity as ssim

from .displaycv import Displaycv
from .ledcv import LEDcv


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
        display = Displaycv.__get_extracted_display(img)
        if display is None:
            return None

        # Correct areas with low sharpness
        corrected_display = Displaycv.__correct_low_sharpness(display, threshold=25, strength=2.5)

        # Read characters on the display
        text = Displaycv.__read_char(corrected_display)

        return text

    @staticmethod
    def display_backlight_test(img):
        
        # Extract the display
        display = Displaycv.__get_extracted_display(img)
        if display is None:
            return None

        # Convert image to grayscale
        image_gray = cv2.cvtColor(display, cv2.COLOR_BGR2GRAY)

        # Calculate the average pixel value
        average_brightness = np.mean(image_gray)

        # Check if the average brightness is below the threshold
        threshold = 10
        return (average_brightness <= threshold)

    @staticmethod
    def display_characters_test(img, model_display):
        
        # Extract the reference display
        model_transformation_matrix, model_coordinates = Displaycv.__get_transformation_matrix(model_display)
        if model_transformation_matrix is None:
            # TODO: Error Code
            return -1
        model_display = Displaycv.__extract_display(model_display, model_transformation_matrix, model_coordinates)
        
        # Extract the display
        image_display = Displaycv.__get_extracted_display(img)
        if image_display is None:
            # TODO: Error Code
            return -1
        
        # Correct areas with low sharpness
        model_display = Displaycv.__correct_low_sharpness(model_display, threshold=25, strength=2.5)
        image_display = Displaycv.__correct_low_sharpness(image_display, threshold=25, strength=2.5)

        # Convert images to grayscale
        model_gray = cv2.cvtColor(model_display, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.cvtColor(image_display, cv2.COLOR_BGR2GRAY)

        # Calcula o SSIM entre as imagens
        win_size = min(image_gray.shape[0], image_gray.shape[1]) // 7 * 2 + 1
        ssim_score = ssim(image_gray, model_gray, win_size=win_size, full=True)[0]

        # Check if the ssim score is above the threshold
        threshold = 0.95
        return (ssim_score > threshold)
    
    @staticmethod
    def display_color_pattern_test(img, model_display):
        
        # Extract the reference display
        model_transformation_matrix, model_coordinates = Displaycv.__get_transformation_matrix(model_display)
        if model_transformation_matrix is None:
            # TODO: Error Code
            return -1
        model_display = Displaycv.__extract_display(model_display, model_transformation_matrix, model_coordinates)

        # Extract the display
        image_display = Displaycv.__get_extracted_display(img)
        if image_display is None:
            # TODO: Error Code
            return -1
        
        # Convert the images to RGB color space
        image = cv2.cvtColor(image_display, cv2.COLOR_BGR2RGB)
        model = cv2.cvtColor(model_display, cv2.COLOR_BGR2RGB)
        
        # Calculate mean squared error (MSE) between the intensities of the two plots
        mse = np.square(np.subtract(image, model)).mean()

        # Compare the MSE against the threshold
        threshold = 10
        return (mse <= threshold)