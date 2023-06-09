from data.color.list_of_colors import ListOfColors
from main.constant_main import *
from main.library import Library as L
from data.color.color import Color

from .menu_prints import MenuPrints as MP


class LibraryColor:

    @staticmethod
    def edit_color_edit_color():
        
        # Print current available colors
        LibraryColor._print_available_colors()
        color_name = L.get_name_or_index("Insert the index or the name of the color you want to delete", [c.get_name() for c in ListOfColors.get_list_of_colors()])
        if color_name is None: return -1

        color = ListOfColors.get_color(color_name)
        
        count = 0
        while True:
            
            MP.edit_color()
            menu_choice = input().strip()

            if len(menu_choice) == 0:
                continue

            match (menu_choice):
                # Edit name
                case '1':
                    LibraryColor.edit_color_edit_color_edit_name(color)
                # Edit 1st range
                case '2':
                    LibraryColor.edit_color_edit_color_edit_1st_range(color)
                # Edit 2nd range
                case '3':
                    LibraryColor.edit_color_edit_color_edit_2nd_range(color)
                # Delete
                case '4':
                    remove = L.get_yes_no_confirmation(f"Are you really sure you want to delete color {color.get_name()} [y|n] ? ")
                    if remove:
                        ListOfColors.remove_color(color_name)
                        ListOfColors.save_to_file()
                        L.exit_input(f"Color {color_name} deleted successfully")
                        break
                # Back
                case '5':
                    break
                case _:
                    count += 1
                    if (count >= NTIMEOUT_LIBRARY_SETTINGS): return -1
                    L.exit_input("Invalid input")
                    continue
        return 0

    @staticmethod
    def edit_color_edit_color_edit_name(color: Color):
        # Get the name of the new color
        new_color_name = L.get_input_str("Write the new name of the color: ")
        if new_color_name is None: return -1
        
        # Check if the name is already in use
        for c in ListOfColors.get_list_of_colors():
            if c is color:
                continue
            elif new_color_name == c.get_name():
                L.exit_input("Invalid color name! This name is already in use")
                return -1
        color.set_name(new_color_name)
        ListOfColors.save_to_file()
        L.exit_input("Name changed successfully")
        return 0

    @staticmethod
    def edit_color_edit_color_edit_1st_range(color: Color):
        # Get the hsv values for the 1st range
        hsv_min1 = L.get_hsv_values("Write the minimum HSV values of the new color [h s v]: ")
        if len(hsv_min1) != 3: return -1

        hsv_max1 = L.get_hsv_values("Write the maximum HSV values of the new color [h s v]: ")
        if len(hsv_max1) != 3: return -1

        # Check for range consistency
        if hsv_min1[0] >= hsv_max1[0]:
            L.exit_input("Invalid hsv range! The minimum value is higher than the maximum value")
            return -1
        # Check if the 1st range overlaps the second
        elif not LibraryColor.check_hsv_ranges(hsv_min1, hsv_max1, color.get_hsv_min2(), color.get_hsv_max2()):
            L.exit_input("Invalid hsv range! The ranges cannot overlap inside the color")
            return -1

        # Check if the range overlaps
        for c in ListOfColors.get_list_of_colors():
            if c is color:
                continue
            # Check with 1st range
            elif not LibraryColor.check_hsv_ranges(hsv_min1, hsv_max1, c.get_hsv_min1(), c.get_hsv_max1()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1
            # Check with 2nd range
            elif not LibraryColor.check_hsv_ranges(hsv_min1, hsv_max1, c.get_hsv_min2(), c.get_hsv_max2()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1
            
        color.set_hsv_min1(hsv_min1)
        color.set_hsv_max1(hsv_max1)
        ListOfColors.save_to_file()
        L.exit_input("1st HSV range changed successfully")
        return 0

    @staticmethod
    def edit_color_edit_color_edit_2nd_range(color: Color):

        # Check if the user wants to delete the 2nd range
        if color.get_hsv_min2() is not None:
            remove = L.get_yes_no_confirmation("Do you want to remove the 2nd HSV range [y|n]?")
            if remove is None: return -1

            if remove:
                color.set_hsv_min2(None)
                color.set_hsv_max2(None)
                L.exit_input("2nd HSV range deleted successfully")
                return 0

        # Get the hsv values for the 1st range
        hsv_min2 = L.get_hsv_values("Write the minimum HSV values of the new color [h s v]: ")
        if len(hsv_min2) != 3: return -1

        hsv_max2 = L.get_hsv_values("Write the maximum HSV values of the new color [h s v]: ")
        if len(hsv_max2) != 3: return -1

        # Check for range consistency
        if hsv_min2[0] >= hsv_max2[0]:
            L.exit_input("Invalid hsv range! The minimum value is higher than the maximum value")
            return -1
        # Check if the 1st range overlaps the second
        elif not LibraryColor.check_hsv_ranges(hsv_min2, hsv_max2, color.get_hsv_min1(), color.get_hsv_max1()):
            L.exit_input("Invalid hsv range! The ranges cannot overlap inside the color")
            return -1

        # Check if the range overlaps
        for c in ListOfColors.get_list_of_colors():
            if c is color:
                continue
            # Check with 1st range
            elif not LibraryColor.check_hsv_ranges(hsv_min2, hsv_max2, c.get_hsv_min1(), c.get_hsv_max1()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1
            # Check with 2nd range
            elif not LibraryColor.check_hsv_ranges(hsv_min2, hsv_max2, c.get_hsv_min2(), c.get_hsv_max2()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1
            
        color.set_hsv_min2(hsv_min2)
        color.set_hsv_max2(hsv_max2)
        ListOfColors.save_to_file()
        L.exit_input("2st HSV range changed successfully")
        return 0

    @staticmethod
    def edit_color_new_color():
        
        # Print current available colors
        LibraryColor._print_available_colors()

        # Get the name of the new color
        new_color_name = L.get_input_str("Write the name of the new color: ")
        if new_color_name is None: return -1

        # Check if the name is already in use
        for color in ListOfColors.get_list_of_colors():
            if new_color_name == color.get_name():
                L.exit_input("Invalid color name! This name is already in use")
                return -1

        # Get the hsv values for the 1st range
        hsv_min1 = L.get_hsv_values("Write the minimum HSV values of the new color [h s v]: ")
        if len(hsv_min1) != 3: return -1

        hsv_max1 = L.get_hsv_values("Write the maximum HSV values of the new color [h s v]: ")
        if len(hsv_max1) != 3: return -1

        # Check for range consistency
        if hsv_min1[0] >= hsv_max1[0]:
            L.exit_input("Invalid hsv range! The minimum value is higher than the maximum value")
            return -1

        # Check if the range overlaps
        for color in ListOfColors.get_list_of_colors():
            # Check with 1st range
            if not LibraryColor.check_hsv_ranges(hsv_min1, hsv_max1, color.get_hsv_min1(), color.get_hsv_max1()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1
            # Check with 2nd range
            elif not LibraryColor.check_hsv_ranges(hsv_min1, hsv_max1, color.get_hsv_min2(), color.get_hsv_max2()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1

        # Check if there is a second range of hsv values
        is_there_a_second_range = L.get_yes_no_confirmation("Is there a second range of hsv values [y|n]? ")
        if is_there_a_second_range is None: return -1

        # Get the hsv values for the 2nd range
        if is_there_a_second_range:
            hsv_min2 = L.get_hsv_values("Write the minimum HSV values of the new color: ")
            if len(hsv_min2) != 3: return -1

            hsv_max2 = L.get_hsv_values("Write the maximum HSV values of the new color: ")
            if len(hsv_max2) != 3: return -1

            # Check for range consistency
            if hsv_min2[0] >= hsv_max2[0]:
                L.exit_input("Invalid hsv range! The minimum value is higher than the maximum value")
                return -1
        else:
            hsv_min2 = hsv_max2 = None
        
        # Check with the 1st range of the new color
        if not LibraryColor.check_hsv_ranges(hsv_min2, hsv_max2, hsv_min1, hsv_max1):
            L.exit_input("Invalid hsv range! The ranges cannot overlap inside the color")
            return -1
        
        # Check if the ranges don't overlap
        for color in ListOfColors.get_list_of_colors():
            # Check with 1st range
            if not LibraryColor.check_hsv_ranges(hsv_min2, hsv_max2, color.get_hsv_min1(), color.get_hsv_max1()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1
            # Check with 2nd range
            elif not LibraryColor.check_hsv_ranges(hsv_min2, hsv_max2, color.get_hsv_min2(), color.get_hsv_max2()):
                L.exit_input("Invalid hsv range! The ranges cannot overlap between different colors")
                return -1

        ListOfColors.add_color(new_color_name, hsv_min1, hsv_max1, hsv_min2, hsv_max2)
        ListOfColors.save_to_file()

        L.exit_input(f"Color {new_color_name} added successfully")
        return 0

    @staticmethod
    def edit_color_delete_color():
        # Print current available colors
        LibraryColor._print_available_colors()
        color_name = L.get_name_or_index("Insert the index or the name of the color you want to delete", [c.get_name() for c in ListOfColors.get_list_of_colors()])
        if color_name is None: return -1

        remove = L.get_yes_no_confirmation(f"Are you really sure you want to delete color {color_name} [y|n]? ")
        if remove is None: return -1

        if remove:
            ListOfColors.remove_color(color_name)
            ListOfColors.save_to_file()
            L.exit_input(f"Color {color_name} deleted successfully")
        
        return 0

    @staticmethod
    def check_hsv_ranges(hsv_min1, hsv_max1, hsv_min2, hsv_max2):
        if hsv_min1 is None or hsv_max1 is None or hsv_min2 is None or hsv_max2 is None:
            return True
        elif (hsv_min2[0] <= hsv_min1[0] <= hsv_max2[0]) or (hsv_min2[0] <= hsv_max1[0] <= hsv_max2[0]):
            return False
        else:
            return True

    @staticmethod
    def _print_available_colors():
        print("List of current available colors:")
        for i, color in enumerate(ListOfColors.get_list_of_colors()):
            print(str(i+1) + ' - ' + color.get_name(), end='')
            print(f" - {color.get_hsv_min1()} {color.get_hsv_max1()}", end='')
            if color.get_hsv_min2() is not None:
                print(f" - {color.get_hsv_min2()} {color.get_hsv_max2()}", end='')
            print()
        print()
    