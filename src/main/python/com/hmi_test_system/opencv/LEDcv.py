import cv2

class LEDcv:
    def cut_led(image, led):
        return image[led.get_pos_x-2:led.get_pos_x+2, led.get_pos_y-2:led.get_pos_y+2]




