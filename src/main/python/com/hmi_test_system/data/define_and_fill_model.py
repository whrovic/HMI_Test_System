import os
import xml.etree.ElementTree as ET

from data.color.list_of_colors import ListOfColors
from data.model.model import Model

from .model.boot_loader_info import BootLoaderInfo
from .model.button import Button
from .model.display import Display
from .model.info import Info
from .model.led import Led
from .settings import Settings


class DefineAndFillModel:

    @staticmethod
    def open_model_xml(name_model):

        # Get all the xml filenames from the xml files folder                
        xml_filenames = DefineAndFillModel.get_all_xml_file_names()
        if xml_filenames is None:
            print("Error path don't exist")
            input('Write anything to back to menu')
            return -1

        filename = name_model + '.xml'
        if  name_model in xml_filenames:
            # open a model with the xml file
            xml_file = os.path.join(Settings.path.get_xml_directory(), filename)
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
            info = model.find('info')
            info_board = info.find('board')
            info_option = info.find('option')
            info_revision = info.find('revision')
            info_edition = info.find('edition')
            info_lcd_type = info.find('lcd_type')
            INFO = Info(info_board.text, info_option.text, info_revision.text, info_edition.text, info_lcd_type.text)
            boot_info = model.find('boot_loader_info')
            boot_version = boot_info.find('version')
            boot_date = boot_info.find('date')
            BOOT_INFO = BootLoaderInfo(boot_version.text, boot_date.text)
            Settings.new_model(name.text, int(n_leds.text), int(n_buttons.text), LCD, INFO, BOOT_INFO)
            
            index = Settings.index_model(name.text)

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
                    led.new_colour(ListOfColors.get_color(led_colour.text))
                Settings.model[index].set_led(led) 

            buttons = model.find('buttons')
            for i in range(0, int(n_buttons.text)):
                button_name = buttons.find(f'button{i+1}_name')
                button_x = buttons.find(f'button{i+1}_x')
                button_y = buttons.find(f'button{i+1}_y')
                button = Button(button_name.text, int(button_x.text), int(button_y.text))
                Settings.model[index].set_button(button)

            return 1
        else:
            return None

    @staticmethod
    def create_xml(model: Model):

        if model is None:
            return -1
        
        name_model = model.get_name()
        
        # create an XML representation of the object
        model_root = ET.Element(f'{model.get_name()}')
        name = ET.SubElement(model_root, 'name')
        name.text = str(model.get_name())
        n_leds = ET.SubElement(model_root, 'n_leds')
        n_leds.text = str(model.get_n_leds())
        n_buttons = ET.SubElement(model_root, 'n_buttons')
        n_buttons.text = str(model.get_n_buttons())
        display = ET.SubElement(model_root, 'display')
        display_name = ET.SubElement(display, 'display_name')
        dsp= model.get_display()
        display_name.text = str(dsp.get_name())
        display_x = ET.SubElement(display, 'display_x')
        display_x.text = str(dsp.get_pos_x())
        display_y = ET.SubElement(display, 'display_y')
        display_y.text = str(dsp.get_pos_y())
        display_dimx = ET.SubElement(display, 'display_dimx')
        display_dimx.text = str(dsp.get_dim_x())
        display_dimy = ET.SubElement(display, 'display_dimy')
        display_dimy.text = str(dsp.get_dim_y())
        info = ET.SubElement(model_root, 'info')
        inf = model.get_info()
        info_board = ET.SubElement(info, 'board')
        info_board.text = str(inf.get_board())
        info_option = ET.SubElement(info, 'option')
        info_option.text = str(inf.get_option())
        info_revision = ET.SubElement(info, 'revision')
        info_revision.text = str(inf.get_revision())
        info_edition = ET.SubElement(info, 'edition')
        info_edition.text = str(inf.get_edition())
        info_lcd_type = ET.SubElement(info, 'lcd_type')
        info_lcd_type.text = str(inf.get_lcd_type())
        boot_info = ET.SubElement(model_root, 'boot_loader_info')
        boot = model.get_boot_loader_info()
        boot_version = ET.SubElement(boot_info, 'version')
        boot_version.text = str(boot.get_version())
        boot_date = ET.SubElement(boot_info, 'date')
        boot_date.text = str(boot.get_date())
        
        leds = ET.SubElement(model_root, 'leds')
        nLeds = model.get_n_leds()
        for i in range(0, nLeds):
            aux2 = model._leds[i]
            led_name = ET.SubElement(leds, f'led{i+1}_name')
            led_name.text = str(aux2.get_name())
            led_nColour = ET.SubElement(leds, f'led{i+1}_nColour')
            led_nColour.text = str(aux2.get_n_Colour())
            led_x = ET.SubElement(leds, f'led{i+1}_x')
            led_x.text = str(aux2.get_pos_x())
            led_y = ET.SubElement(leds, f'led{i+1}_y')
            led_y.text = str(aux2.get_pos_y())
            leds_colours = ET.SubElement(leds, f'led{i+1}_colours')
            for j in range(0, aux2._n_colour):
                aux3 = model._leds[i].get_colours()
                led_colour = ET.SubElement(leds_colours, f'led{i+1}_colour{j+1}')
                led_colour.text = str(aux3[j].get_name())
        

        buttons = ET.SubElement(model_root, 'buttons')
        nButtons = model.get_n_buttons()
        for i in range(0, nButtons):
            aux2 = model._buttons[i]
            button_name = ET.SubElement(buttons, f'button{i+1}_name')
            button_name.text = str(model._buttons[i].get_name())
            button_x = ET.SubElement(buttons, f'button{i+1}_x')
            button_x.text = str(model._buttons[i].get_pos_x())
            button_y = ET.SubElement(buttons, f'button{i+1}_y')
            button_y.text = str(model._buttons[i].get_pos_y())

        # Create the XML document and write it to a file
        tree = ET.ElementTree(model_root)
        ET.indent(tree, '  ')
        tree.write(f"{Settings.path.get_xml_directory()}/{name_model}.xml")

    @staticmethod
    def delete_xml(name_model):
        
        file_path = f"{Settings.path.get_xml_directory()}/{name_model}.xml"

        # check if the file exists
        if os.path.exists(file_path):
            # delete the file
            os.remove(file_path)
            return 1
        else:
            return -1

    @staticmethod
    def get_all_xml_file_names():
        try:
            files = os.listdir(Settings.path.get_xml_directory())   # files in directory
        except:
            return None
                
        xml_files = [file[:-4] for file in files if file.endswith('.xml')]   # xml files in directory

        return xml_files
