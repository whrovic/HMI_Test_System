import json
from .color import Color
from typing import List

class ListOfColors:
    
    _list_of_colors: List[Color]= []

    @staticmethod
    def get_n_colors():
        return len(ListOfColors._list_of_colors)

    @staticmethod
    def get_list_of_colors():
        return ListOfColors._list_of_colors
    
    @staticmethod
    def get_color_index(index: int):
        return ListOfColors._list_of_colors[index]

    @staticmethod
    def get_color(name: str):
        for color in ListOfColors._list_of_colors:
            if color.get_name() == name:
                return color
        return None

    @staticmethod
    def add_color(name, hsv_min1, hsv_max1, hsv_min2=None, hsv_max2=None):
        # Check if color already exists
        color = ListOfColors.get_color(name)
        if color is not None:
            return

        # Create new color object and add to list
        new_color = Color(name, hsv_min1, hsv_max1, hsv_min2, hsv_max2)
        ListOfColors._list_of_colors.append(new_color)

    @staticmethod
    def remove_color(name):
        for color in ListOfColors._list_of_colors:
            if color.get_name() == name:
                ListOfColors._list_of_colors.remove(color)
                return True
        return False

    @staticmethod
    def save_to_file(filename):
        data = []
        for color in ListOfColors._list_of_colors:
            data.append({
                "name": color.get_name(),
                "hsv_min1": color.get_hsv_min1(),
                "hsv_max1": color.get_hsv_max1(),
                "hsv_min2": color.get_hsv_min2(),
                "hsv_max2": color.get_hsv_max2()
            })

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    
    @staticmethod
    def read_from_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        
            for color_data in data:
                name = color_data['name']
                hsv_min1 = tuple(color_data['hsv_min1'])
                hsv_max1 = tuple(color_data['hsv_max1'])
                hsv_min2 = color_data['hsv_min2']
                if (hsv_min2 is not None):
                    hsv_min2 = tuple(hsv_min2)
                hsv_max2 = color_data['hsv_max2']
                if (hsv_max2 is not None):
                    hsv_max2 = tuple(hsv_max2)
                ListOfColors.add_color(name, hsv_min1, hsv_max1, hsv_min2, hsv_max2)