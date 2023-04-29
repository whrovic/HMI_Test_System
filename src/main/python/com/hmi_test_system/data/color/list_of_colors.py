
class ListOfColors:
    
    _list_of_colors = []

    @staticmethod
    def get_list_of_colors():
        return ListOfColors._list_of_colors


    @staticmethod
    def get_color(name):
        for color in ListOfColors._list_of_colors:
            if color.get_name() == name:
                return color
        return None

    @staticmethod
    def add_color(name, hsv_min1, hsv_max1, hsv_min2=None, hsv_max2=None):
        # Check if color already exists
        color = ListOfColors.get_color(name)
        if color is not None:
            print(f"Color {name} already exists!")
            return

        # Create new color object and add to list
        new_color = color(name, hsv_min1, hsv_max1, hsv_min2, hsv_max2)
        ListOfColors._list_of_colors.append(new_color)
        print(f"Color {name} added successfully!")
    

    @staticmethod
    def remove_color(name):
        for color in ListOfColors._list_of_colors:
            if color.get_name() == name:
                ListOfColors._list_of_colors.remove(color)
                return True
        return False

    '''
    Guarda o vetor de cores, todas as cores e as propriedades para um ficheiro (.txt, .xml, .json, whatever)
    Baixa prioridade
    '''
    @staticmethod
    def save_to_file(filename):
        pass

    '''
    Lê o ficheiro e recupera o vetor com todas as cores
    Baixa prioridade
    '''
    @staticmethod
    def read_from_file(filename):
        pass