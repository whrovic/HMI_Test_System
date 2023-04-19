from data.Led import Led
from data.Button import Button
from data.Display import Display
from data.Settings import Settings
import xml.etree.ElementTree as ET

def create_model(M: Settings, name_model):
    
    print("Number of buttons: ")
    n_buttons = int(input())   # number of buttons of model
    """ while(n_buttons is not int):
        print("Please write a number")
        n_buttons = input() """
    
    print("Number of leds: ")
    n_leds= int(input())
    """ while(n_leds is not int):
        print("Please write a number")
        n_leds = input()   """     # number of leds of model

    
    print("Model version: ")
    version = int(input())
    """ while(version is not int):
        print("Please write a number")
        version = input()    """  # version of model

    # LCD configuration
    print("\n\nLCD CONFIGURATION\n")
    print("Select the LCD initial position")
    pos_vector_init = [0, 0]
    print("Select the LCD final position")
    pos_vector_final = [0, 0]
    dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
    dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
    display = Display('display', int(pos_vector_init[0]) , int(pos_vector_init[1]) , dim_x, dim_y)

    # add model 
    M.new_model(name_model, n_leds, n_buttons, display, version)

    index = M.index_model(name_model)

    # model exists 
    if(index != -1):

        # leds configuration
        print("\n\nLEDS CONFIGURATION\n")
        for i in range(0, n_leds):
            print(f"Led {i+1} name: ")
            led_name = input()
            print(f"How many colours have the led {i+1}?")
            n_colours = int(input())
            print(f"Select the led {i+1} central position")
            pos_vector = [0, 0]
            led = Led(led_name, n_colours, int(pos_vector[0]), int(pos_vector[1]))
            for j in range(0, n_colours):
                print(f"Colour {j+1} of led {i+1}:")
                new_colour = input()
                led.new_colour(new_colour)

            M.model[int(index)].set_led(led)

        # buttons configuration
        print("\n\nBUTTONS CONFIGURATION\n")
        for i in range(0, n_buttons):
            print(f"Button {i+1} name: ")
            button_name = input()
            print(f"Select the button {i+1} central position")
            pos_vector = [0, 0]
            M.model[int(index)].set_button(Button(button_name, int(pos_vector[0]), int(pos_vector[1])))
    
    # model doesn't exist
    else:
        print("ERROR - Model creation failed")
        M.delete_model(name_model)

    

def create_xml(M: Settings, name_model):

    index = M.index_model(name_model)


    # create an XML representation of the object
    root = ET.Element(f'Model {M.model[index].name}')
    name = ET.SubElement(root, 'name')
    name.text = str(M.model[index].name)
    n_leds = ET.SubElement(root, 'n_leds')
    n_leds.text = str(M.model[index].n_leds)
    n_buttons = ET.SubElement(root, 'n_buttons')
    n_buttons.text = str(M.model[index].n_buttons)
    version = ET.SubElement(root, 'version')
    version.text = str(M.model[index].version)
    display = ET.SubElement(root, 'display')
    display_name = ET.SubElement(display, 'display')
    display_name.text = str(M.model[index].display.name)
    display_x = ET.SubElement(display, 'display_x')
    display_x.text = str(M.model[index].display.x)
    display_y = ET.SubElement(display, 'display_y')
    display_y.text = str(M.model[index].display.y)
    display_dimx = ET.SubElement(display, 'display_dimx')
    display_dimx.text = str(M.model[index].display.dim_x)
    display_dimy = ET.SubElement(display, 'display_dimy')
    display_dimy.text = str(M.model[index].display.dim_y) 
    leds = ET.SubElement(root, 'leds')
    for i in range(0, M.model[index].n_leds):
        led_name = ET.SubElement(leds, f'led{i+1}_name')
        led_name.text = str(M.model[index].leds[i].name)
        led_nColour = ET.SubElement(leds, f'led{i+1}_nColour')
        led_nColour.text = str(M.model[index].leds[i].n_Colour)
        led_x = ET.SubElement(leds, f'led{i+1}_x')
        led_x.text = str(M.model[index].leds[i].x)
        led_y = ET.SubElement(leds, f'led{i+1}_y')
        led_y.text = str(M.model[index].leds[i].y)
        leds_colours = ET.SubElement(root, f'led{i+1}_colours')
        for j in range(0, M.model[index].leds[i].n_Colour):
            led_colour = ET.SubElement(leds_colours, f'led{i+1}_colour{j+1}')
            led_colour.text = str(M.model[index].leds[i].colours[j])
    buttons = ET.SubElement(root, 'buttons')
    for i in range(0, M.model[index].n_buttons):
        button_name = ET.SubElement(buttons, f'button{i+1}_name')
        button_name.text = str(M.model[index].buttons[i].name)
        button_x = ET.SubElement(buttons, f'button{i+1}_x')
        button_x.text = str(M.model[index].buttons[i].x)
        button_y = ET.SubElement(buttons, f'button{i+1}_y')
        button_y.text = str(M.model[index].buttons[i].y)


    # Create the XML document and write it to a file
    tree = ET.ElementTree(root)
    tree.write(f"{name_model}.xml")


    
    

