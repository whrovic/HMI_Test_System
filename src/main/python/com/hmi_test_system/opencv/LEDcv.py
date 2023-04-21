
import cv2
import numpy as np
from ..data.Led import Led

class LEDcv:
    
    def cut_led(image, led: Led):
        return image[led.get_pos_y()-2:led.get_pos_y()+2, led.get_pos_x()-2:led.get_pos_x()+2]


    def read_led_color(self, image, ledTest):
        colors = []

        for led in ledTest:
            img = self.cut_led(image, led)

            # Convert the image from BGR to HSV color space
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # Define the color ranges to detect
            # (red is a more complex color to detect
            # because it can vary significantly in hue 
            # depending on the lighting conditions so it
            # has 4 ranges)
            lower_red1 = np.array([0, 50, 50])
            upper_red1 = np.array([10, 255, 255])
            lower_red2 = np.array([170, 50, 50])
            upper_red2 = np.array([180, 255, 255])
            lower_yellow = np.array([20, 50, 50])
            upper_yellow = np.array([45, 255, 255])
            lower_green = np.array([60, 50, 50])
            upper_green = np.array([90, 255, 255])

            # Threshold the image to isolate the dominant color
            mask_red1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
            mask_red2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
            mask_red = cv2.bitwise_or(mask_red1, mask_red2)
            mask_yellow = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
            mask_green = cv2.inRange(hsv_img, lower_green, upper_green)

            # Calculate the number of pixels for each color
            red_pixels = cv2.countNonZero(mask_red)
            yellow_pixels = cv2.countNonZero(mask_yellow)
            green_pixels = cv2.countNonZero(mask_green)

            for i in colors:

                # Determine the dominant color
                if red_pixels > yellow_pixels and red_pixels > green_pixels:
                    colors[i] = "Red"
                elif yellow_pixels > red_pixels and yellow_pixels > green_pixels:
                    colors[i] = "Yellow"
                elif green_pixels > red_pixels and green_pixels > yellow_pixels:
                    colors[i] = "Green"
                else:
                    colors[i] = "Unknown"
        
        return colors
    










