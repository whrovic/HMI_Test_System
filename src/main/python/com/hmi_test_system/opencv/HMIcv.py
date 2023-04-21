import numpy as np
from LEDcv import LEDcv

class HMIcv():

    '''
    Novo formato:
    def led_test(img, led) -> Color

    Esta função recebe a foto inteira e apenas 1 led. É só recortar, chamar a função read_led_color e retornar a cor lida.
    '''
    def led_test(img, led):
        return False # deve retornar a cor
    
        #get the colors read on the led imagd
        led_colors = LEDcv.read_led_color(img, leds)
        #compare the colors obtained with the expected ones
        if np.array_equal(led_colors, expected):
            return True
        else:
            return False
    
    '''
    Esta função recebe a imagem do sistema inteiro e o display a testar.
    Deve recortar a imagem (cut_lcd), ler os caracteres que lá estão (chamar a função read_char),
    comparar com o esperado, que vem dentro do lcd (lcd.get_char()).
    A função lcd.get_char() retorna uma string com o que é suposto resultar do teste.
    '''
    def display_characters_test(img, lcd):
        return False
    
    def display_backlight_test(img, lcd):
        return False
    
    def display_color_pattern_test(img, lcd):
        return False