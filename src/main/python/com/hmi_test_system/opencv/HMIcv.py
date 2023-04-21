import numpy as np
from LEDcv import LEDcv
from data.color.color import OffColor

class HMIcv():

    '''
    (Mariana)

    Novo formato:
    def led_test(img, led) -> Color

    Esta função recebe a foto inteira e apenas 1 led. É só recortar, chamar a função read_led_color e retornar a cor lida.
    (Alta prioridade)
    '''
    def led_test(img, led):
        return OffColor() # deve retornar a cor
    
        #get the colors read on the led imagd
        led_colors = LEDcv.read_led_color(img, leds)
        #compare the colors obtained with the expected ones
        if np.array_equal(led_colors, expected):
            return True
        else:
            return False
    
    '''
    (Pedro)

    Esta função recebe a imagem do sistema inteiro e o display a testar.
    Deve recortar a imagem (cut_lcd), ler os caracteres que lá estão (chamar a função read_char),
    comparar com o esperado, que vem dentro do lcd (lcd.get_char()).
    A função lcd.get_char() retorna uma string com o que é suposto resultar do teste.
    '''
    def display_characters_test(img, lcd):
        return False
    
    def display_backlight_test(img, lcd):
        return False
    
    '''
    (Pedro)

    Esta função recebe a imagem do sistema inteiro e o display a testar.
    Deve recortar a imagem (cut_lcd), ler o padrão de cores e comparar com o esperado. Retorna um booleano.

    Vê a melhor maneira da comparação, se quiseres ter já os resultados da função get_color_pattern para
    uma imagem de referência, estás à vontade, ou então receberes a imagem de referência, como quiseres.
    Esses resultados viriam dentro da variavel lcd (get_color_pattern() ou algo assim).
    Também podemos guardar essas informações dentro de um ficheiro, associado ao display e liamos o ficheiro
    (esta parte da leitura pode estar fora desta função).
    Procura o que achas ser a melhor maneira para isto.

    Se conseguires começar a implementar top.
    '''
    def display_color_pattern_test(img, lcd):
        return False