'''def open_xml_settings(): 
    while True:
        try:
            files = os.listdir(Settings.path.get_settings_directory())   # files in directory
            break
        except:
            print("Error path don't exist")
            print("To go to the menu insert anything\n")
            c = input()
            return -1
            
    xml_files = [file for file in files if file.endswith('.xml')]   # xml files in directory


    for filename in xml_files:
        # check if it is the asked file
        if filename == f'{"ADICIONAR"}.xml': 
            #...
            pass
            
def create_xml_settings():
    # Create the XML document and write it to a file
    tree = ET.ElementTree("")
    ET.indent(tree, '  ')
    tree.write(f"{Settings.path.get_settings_directory()}/{"ADICIONAR"}.xml")


def delete_xml_settings():
    file_path = f"{Settings.path.get_settings_directory()}/{"ADICIONAR"}.xml"

    # check if the file exists
    if os.path.exists(file_path):
        # delete the file
        os.remove(file_path)
        return 1
    else:
        return -1'''
    