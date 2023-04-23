import xml.etree.ElementTree as ET
from .Settings import Settings
from .model.Display import Display
from .model.Led import Led
from .model.Button import Button
import os

class DefineAndFillModel:
    def open_model_xml(M: Settings, name_model, directory):

        files = os.listdir(directory)                                   # files in directory

        xml_files = [file for file in files if file.endswith('.xml')]   # xml files in directory


        for filename in xml_files:
            # check if it is the asked file
            if filename == f'{name_model}.xml':
                # make a model with the xml file
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
                LCD = Display(display_name.text, int(display_x.text), int(display_y.text), int(display_dimx.text), int(display_dimy.text))
                version = model.find('version')
                M.new_model(name.text, int(n_leds.text), int(n_buttons.text), LCD, version.text)
                
                index = M.index_model(name.text)

                leds = model.find('leds')
                for i in range(0, int(n_leds.text)):
                    led_name = leds.find(f'led{i+1}_name')
                    led_nColour = leds.find(f'led{i+1}_nColour')
                    led_x = leds.find(f'led{i+1}_x')
                    led_y = leds.find(f'led{i+1}_y') 
                    led = Led(led_name.text, int(led_nColour.text), int(led_x.text), int(led_y.text))
                    leds_colours = leds.find(f'led{i+1}_colours')
                    for j in range(0, int(led_nColour.text)):   
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

                return 1
            
            else:
                continue
        
        
        return None

    def create_xml(M: Settings, name_model, directory):

        index = M.index_model(name_model)
        aux = M.model[index]

        # create an XML representation of the object
        model = ET.Element(f'{aux.get_name()}')
        name = ET.SubElement(model, 'name')
        name.text = str(aux.get_name())
        n_leds = ET.SubElement(model, 'n_leds')
        n_leds.text = str(aux.get_n_leds())
        n_buttons = ET.SubElement(model, 'n_buttons')
        n_buttons.text = str(aux.get_n_buttons())
        display = ET.SubElement(model, 'display')
        display_name = ET.SubElement(display, 'display_name')
        dsp= aux.get_display()
        display_name.text = str(dsp.get_name())
        display_x = ET.SubElement(display, 'display_x')
        display_x.text = str(dsp.get_pos_x())
        display_y = ET.SubElement(display, 'display_y')
        display_y.text = str(dsp.get_pos_y())
        display_dimx = ET.SubElement(display, 'display_dimx')
        display_dimx.text = str(dsp.get_dim_x())
        display_dimy = ET.SubElement(display, 'display_dimy')
        display_dimy.text = str(dsp.get_dim_y())
        version = ET.SubElement(model, 'version')
        version.text = str(aux.get_version())
        

        leds = ET.SubElement(model, 'leds')
        nLeds = aux.get_n_leds()
        for i in range(0, nLeds):
            aux2 = aux._leds[i]
            led_name = ET.SubElement(leds, f'led{i+1}_name')
            led_name.text = str(aux2.get_name())
            led_nColour = ET.SubElement(leds, f'led{i+1}_nColour')
            led_nColour.text = str(aux2.get_n_Colour())
            led_x = ET.SubElement(leds, f'led{i+1}_x')
            led_x.text = str(aux2.get_pos_x())
            led_y = ET.SubElement(leds, f'led{i+1}_y')
            led_y.text = str(aux2.get_pos_y())
            leds_colours = ET.SubElement(leds, f'led{i+1}_colours')
            for j in range(0, aux2._n_Colour):
                aux3 = aux._leds[i].get_colour()
                led_colour = ET.SubElement(leds_colours, f'led{i+1}_colour{j+1}')
                led_colour.text = str(aux3[j])
        

        buttons = ET.SubElement(model, 'buttons')
        nButtons = aux.get_n_buttons()
        for i in range(0, nButtons):
            aux2 = aux._buttons[i]
            button_name = ET.SubElement(buttons, f'button{i+1}_name')
            button_name.text = str(aux._buttons[i].get_name())
            button_x = ET.SubElement(buttons, f'button{i+1}_x')
            button_x.text = str(aux._buttons[i].get_pos_x())
            button_y = ET.SubElement(buttons, f'button{i+1}_y')
            button_y.text = str(aux._buttons[i].get_pos_y())


        # Create the XML document and write it to a file
        tree = ET.ElementTree(model)
        tree.write(f"{directory}/{name_model}.xml")

    def delete_xml(name_model, directory):
        
        file_path = f"{directory}/{name_model}.xml"

        # check if the file exists
        if os.path.exists(file_path):
            # delete the file
            os.remove(file_path)
            return 1
        else:
            return -1
