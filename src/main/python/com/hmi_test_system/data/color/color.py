'''
(Mariana)

A class color deve ter um nome(string) e todas as propriedades (ranges hsv) que precisares para
a função de leitura dos leds.
Esta classe só precisa de adicionar getters e setters
'''
class Color:

    def __init__(self, name, hsv_min_1, hsv_max_1, hsv_min2 = None, hsv_max2 = None):
        self._name = name
        self._hsv_min_1 = hsv_min_1
        self._hsv_max_1 = hsv_max_1
        self._hsv_min2 = hsv_min2
        self._hsv_max2 = hsv_max2 
        

class OffColor(Color):

    def __init__(self):
        super().__init__("Off", None, None)

class UnknownColor(Color):
    
    def __init__(self):
        super().__init__("Unknown", None, None)