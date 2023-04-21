import xml.etree.ElementTree as ET
from .Settings import Settings
from .model.Display import Display
from .model.Led import Led
from .model.Button import Button
import os

class DefineAndFillModel:
    def open_model_xml(M: Settings, name_model, directory):
        # Define the directory to search

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
        model = ET.Element(f'{M.model[index].get_name}')
        name = ET.SubElement(model, 'name')
        name.text = str(M.model[index].get_name)
        n_leds = ET.SubElement(model, 'n_leds')
        n_leds.text = str(M.model[index].get_n_leds)
        n_buttons = ET.SubElement(model, 'n_buttons')
        n_buttons.text = str(M.model[index].get_n_buttons)
        display = ET.SubElement(model, 'display')
        display_name = ET.SubElement(display, 'display_name')
        dsp=M.model[index]._display
        display_name.text = str(dsp.get_name)
        display_x = ET.SubElement(display, 'display_x')
        display_x.text = str(dsp.get_dim_x)
        display_y = ET.SubElement(display, 'display_y')
        display_y.text = str(dsp.get_dim_y)
        display_dimx = ET.SubElement(display, 'display_dimx')
        display_dimx.text = str(dsp.get_dim_x)
        display_dimy = ET.SubElement(display, 'display_dimy')
        display_dimy.text = str(dsp.get_dim_y)
        version = ET.SubElement(model, 'version')
        version.text = str(M.model[index].get_version)
        
        leds = ET.SubElement(model, 'leds')
        aux = M.model[index]._n_leds
        print (aux)
        #for i in M.model[index].get_leds:
        for i in range(0, aux):
            aux=M.model[index]._leds[i]
            led_name = ET.SubElement(leds, f'led{i+1}_name')
            led_name.text = str(aux._name)
            led_nColour = ET.SubElement(leds, f'led{i+1}_nColour')
            led_nColour.text = str(aux._n_Colour)
            led_x = ET.SubElement(leds, f'led{i+1}_x')
            led_x.text = str(aux.x)
            led_y = ET.SubElement(leds, f'led{i+1}_y')
            led_y.text = str(aux.y)
            leds_colours = ET.SubElement(leds, f'led{i+1}_colours')
            for j in range(0, M.model[index]._leds[i]._n_Colour):
                led_colour = ET.SubElement(leds_colours, f'led{i+1}_colour{j+1}')
                led_colour.text = str(M.model[index]._leds[i]._colours[j])
        
        buttons = ET.SubElement(model, 'buttons')
        for i in range(0, M.model[index]._n_buttons):
            button_name = ET.SubElement(buttons, f'button{i+1}_name')
            button_name.text = str(M.model[index]._buttons[i]._name)
            button_x = ET.SubElement(buttons, f'button{i+1}_x')
            button_x.text = str(M.model[index]._buttons[i].get_pos_x)
            button_y = ET.SubElement(buttons, f'button{i+1}_y')
            button_y.text = str(M.model[index]._buttons[i].get_pos_y)


        # Create the XML document and write it to a file
        tree = ET.ElementTree(model)
        tree.write(f"{name_model}.xml")

