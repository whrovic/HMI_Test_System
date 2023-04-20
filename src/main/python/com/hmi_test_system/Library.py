from data.Led import Led
from data.Button import Button
from data.Display import Display
from data.Settings import Settings
import xml.etree.ElementTree as ET
import os

def create_model_manual(M: Settings, name_model):
    
    print("Number of buttons: ")
    n_buttons = int(input())   # number of buttons of model
    
    print("Number of leds: ")
    n_leds= int(input())        # number of leds of model
    
    print("Model version: ")
    version = input()      # version of model

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
            print(f"\nLed {i+1} name: ")
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
            print(f"\nButton {i+1} name: ")
            button_name = input()
            print(f"Select the button {i+1} central position")
            pos_vector = [0, 0]
            M.model[int(index)].set_button(Button(button_name, int(pos_vector[0]), int(pos_vector[1])))
    
    # model doesn't exist
    else:
        print("ERROR - Model creation failed")
        M.delete_model(name_model)

def open_model_xml(M: Settings, name_model):
    # Define the directory to search
    #directory = "/path/to/directory"
    directory = r"C:\Users\asus\ES\HMI_Test_System"

    # List all the files in the directory
    for filename in os.listdir(directory):
        # Check if the file's extension is ".xml"
        if filename.endswith(f"{name_model}.xml"):
            # Do something with the XML file
            xml_file = os.path.join(directory, filename)
            tree = ET.parse(xml_file)
            model = tree.getroot()
            name = model.find('name')
            n_leds = model.find('n_leds')
            n_buttons = model.find('n_buttons')
            display = model.find('display')
            display_name = display.find('display_name')
            display_x = display.find('display_x')
            display_y = display.find('display_y')
            display_dimx = display.find('display_dimx')
            display_dimy = display.find('display_dimy')
            LCD = Display(display_name.text, int(display_x.text), int(display_y.text), int(display_dimx), int(display_dimy))
            version = model.find('version')
            M.new_model(name.text, int(n_leds), int(n_buttons.text), LCD, version.text)
            
            index = M.index_model(name.text)

            leds = model.find('leds')
            for i in range(0, int(n_leds.text)):
                led_name = leds.find(f'led{i+1}_name')
                led_nColour = leds.find(f'led{i+1}_nColour')
                led_x = leds.find(f'led{i+1}_x')
                led_y = leds.find(f'led{i+1}_y') 
                led = Led(led_name.text, int(led_nColour.text), int(led_x.text), int(led_y.text))
                leds_colours = leds.find(f'led{i+1}_colours')
                for j in range(0, led_nColour):   
                    led_colour = leds_colours.find(f'led{i+1}_colour{j+1}')
                    led.new_colour(led_colour.text)
                M.model[index].set_led(led) 

            buttons = model.find('buttons')
            for i in range(0, int(n_buttons.text)):
                button_name = buttons.find(f'button{i+1}_name')
                button_x = buttons.find(f'button{i+1}_x')
                button_y = buttons.find(f'button{i+1}_y')
                button = Button(button_name.text, int(button_x.text), int(button_y.text))
                M.model[index].set_button(button)

        else:
            return None

def create_xml(M: Settings, name_model):

    index = M.index_model(name_model)

    # create an XML representation of the object
    model = ET.Element(f'{M.model[index].name}')
    name = ET.SubElement(model, 'name')
    name.text = str(M.model[index].name)
    n_leds = ET.SubElement(model, 'n_leds')
    n_leds.text = str(M.model[index].n_leds)
    n_buttons = ET.SubElement(model, 'n_buttons')
    n_buttons.text = str(M.model[index].n_buttons)
    display = ET.SubElement(model, 'display')
    display_name = ET.SubElement(display, 'display_name')
    display_name.text = str(M.model[index].display.name)
    display_x = ET.SubElement(display, 'display_x')
    display_x.text = str(M.model[index].display.pos_init_x)
    display_y = ET.SubElement(display, 'display_y')
    display_y.text = str(M.model[index].display.pos_init_y)
    display_dimx = ET.SubElement(display, 'display_dimx')
    display_dimx.text = str(M.model[index].display.dim_x)
    display_dimy = ET.SubElement(display, 'display_dimy')
    display_dimy.text = str(M.model[index].display.dim_y)
    version = ET.SubElement(model, 'version')
    version.text = str(M.model[index].version)
    
    leds = ET.SubElement(model, 'leds')
    for i in range(0, M.model[index].n_leds):
        led_name = ET.SubElement(leds, f'led{i+1}_name')
        led_name.text = str(M.model[index].leds[i].name)
        led_nColour = ET.SubElement(leds, f'led{i+1}_nColour')
        led_nColour.text = str(M.model[index].leds[i].n_Colour)
        led_x = ET.SubElement(leds, f'led{i+1}_x')
        led_x.text = str(M.model[index].leds[i].x)
        led_y = ET.SubElement(leds, f'led{i+1}_y')
        led_y.text = str(M.model[index].leds[i].y)
        leds_colours = ET.SubElement(leds, f'led{i+1}_colours')
        for j in range(0, M.model[index].leds[i].n_Colour):
            led_colour = ET.SubElement(leds_colours, f'led{i+1}_colour{j+1}')
            led_colour.text = str(M.model[index].leds[i].colours[j])
    
    buttons = ET.SubElement(model, 'buttons')
    for i in range(0, M.model[index].n_buttons):
        button_name = ET.SubElement(buttons, f'button{i+1}_name')
        button_name.text = str(M.model[index].buttons[i].name)
        button_x = ET.SubElement(buttons, f'button{i+1}_x')
        button_x.text = str(M.model[index].buttons[i].x)
        button_y = ET.SubElement(buttons, f'button{i+1}_y')
        button_y.text = str(M.model[index].buttons[i].y)


    # Create the XML document and write it to a file
    tree = ET.ElementTree(model)
    tree.write(f"{name_model}.xml")


    
    

