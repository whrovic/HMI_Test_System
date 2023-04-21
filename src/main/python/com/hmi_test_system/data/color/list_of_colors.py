'''
(Mariana)

Esta classe deve guardar todas as classes que sejam necessárias. Não é para guardar OffColor e UnknownColor.

As cores devem ser guardadas num ficheiro (.txt, .properties, whatever) e quando a classe é criada (no __init__),
lê todas as cores e as propriedades desse ficheiro.

Devem haver funções para criar nova cor ou remover.

As funções de ler e escrever para o ficheiro deixa para último. Primeiro, no __init__ crias um vetor vazio e 
adiciona-se sempre manualmente com a função add_color todas as cores.
A prioridade é integrar estas novas classes com as funções de teste dos leds.
'''

class ListOfColors:
    
    _list_of_colors = []

    @staticmethod
    def get_list_of_colors():
        return ListOfColors._list_of_colors

    '''
    Deve percorrer o vetor e retornar a cor com o nome indicado (ou None se nao encontrar)
    '''
    @staticmethod
    def get_color(name):
        return None

    '''
    Deve verificar se a cor existe. Se não existir adiciona uma nova cor
    '''
    @staticmethod
    def add_color(name, hsv_min1, hsv_max1, hsv_min2=None, hsv_max2=None):
        pass
    
    '''
    Remove a cor com este nome
    '''
    @staticmethod
    def remove_color(name):
        pass

    '''
    Guarda o vetor de cores, todas as cores e as propriedades para um ficheiro (.txt, .xml, .json, whatever)
    '''
    @staticmethod
    def save_to_file(filename):
        pass

    '''
    Lê o ficheiro e recupera o vetor com todas as cores
    '''
    @staticmethod
    def read_from_file(filename):
        pass