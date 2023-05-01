import cv2
import numpy as np
from data.model.Led import Led
from data.color.color import OffColor, UnknownColor
from data.color.list_of_colors import ListOfColors

class LEDcv:
    
    def cut_led(image, led: Led):
        return image[led.get_pos_y()-2:led.get_pos_y()+2, led.get_pos_x()-2:led.get_pos_x()+2]


    def read_color(image):

        # Convert the image from RGB to HSV 
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Get the list of colors
        colors = ListOfColors.get_list_of_colors()

        # Check if the LED is off ( if the image is completely black)
        if cv2.countNonZero(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)) == 0:
            return OffColor()

        # Check each color in the ListOfColor to see if it matches the image
        for color in colors:
            hsv_min_1 = color.get_hsv_min1()
            hsv_max_1 = color.get_hsv_max1()
            hsv_min_2 = color.get_hsv_min2()
            hsv_max_2 = color.get_hsv_max2()

            # Check if the color range matches the image
            #(color range for some colors may not be representable by a single range in the HSV color space)
            mask1 = cv2.inRange(hsv_img, np.array([hsv_min_1[0], hsv_min_1[1], hsv_min_1[2]]), np.array([hsv_max_1[0], hsv_max_1[1], hsv_max_1[2]]))
            if hsv_min_2 is not None and hsv_max_2 is not None:
                mask2 = cv2.inRange(hsv_img, np.array([hsv_min_2[0], hsv_min_2[1], hsv_min_2[2]]), np.array([hsv_max_2[0], hsv_max_2[1], hsv_max_2[2]]))
                mask1 = cv2.bitwise_or(mask1, mask2)
            pixels = cv2.countNonZero(mask1)
            total_pixels = hsv_img.shape[0] * hsv_img.shape[1]
            color_percentage = (pixels / total_pixels) * 100

            # If the color is found with a match of more than 50%, return the color name
            if color_percentage >= 50:
                return color
        
        # If no color is found with a match less than 50%, return UnknownColor
        return UnknownColor()