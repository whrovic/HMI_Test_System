
import cv2
import numpy as np
from data.model import Led

class LEDcv:
    
    '''
    (Ricardo)
    '''
    def cut_led(image, led: Led):
        return image[led.get_pos_y()-2:led.get_pos_y()+2, led.get_pos_x()-2:led.get_pos_x()+2]


    '''
    (Mariana)
    
    Novo formato:
    def read_color(image) -> Color

    Os parâmetros desta função passaram a ser só a imagem e a única função dela é analisar a cor de uma imagem.
    A imagem já vem recortada e é só ver a cor.
    Basicamente tens de apagar aquele for e o cut_led e retornas so 1 cor.

    Também é preciso adaptar a função para, ao invés de ter aqui definidas as cores,
    percorre o vetor da classe ListOfColors e verifica cada cor. Se a percentagem de "match"
    for acima de 50% (ou um threshold que podemos definir depois) retorna.
    Se chegar ao fim do ciclo e nenhuma cor for detetada retorna a class OffColor.
    (aqui se conseguires, verifica antes de retornar OffColor que o led está garantidamente apagado,
    senão retorna UnknownColor - se não der não tem mal)

    (Alta prioridade)
    '''
    def read_color(image):
        color 
        # Convert the image from BGR to HSV color space
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

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
        total_pixels = hsv_img.shape[0] * hsv_img.shape[1]
        red_pixels = cv2.countNonZero(mask_red)
        yellow_pixels = cv2.countNonZero(mask_yellow)
        green_pixels = cv2.countNonZero(mask_green)

        # Calculate the percentage of pixels for each color
        red_percentage = (red_pixels / total_pixels) * 100
        yellow_percentage = (yellow_pixels / total_pixels) * 100
        green_percentage = (green_pixels / total_pixels) * 100

        # Determine the dominant color
        if red_percentage > yellow_percentage and red_percentage > green_percentage:
            color = "Red"
        elif yellow_percentage > red_percentage and yellow_percentage > green_percentage:
            color = "Yellow"
        elif green_percentage > red_percentage and green_percentage > yellow_percentage:
            color = "Green"
        else:
            color = "Unknown"
    
        return color
