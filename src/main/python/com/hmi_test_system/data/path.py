import os


class Path:
    
    file_path = os.path.dirname(__file__)
    xml_directory = os.path.join(file_path, '../../../../../../xml_files')
    resources_directory = os.path.join(file_path, '../../../../resources')
    settings_directory = os.path.join(file_path, '../../../../../../settings')

    @staticmethod
    def set_settings_directory(settings_directory):
        Path.settings_directory = settings_directory

    @staticmethod
    def get_settings_directory():
        return Path.settings_directory

    @staticmethod
    def set_resources_directory(resources_directory):
        Path.resources_directory = resources_directory

    @staticmethod
    def get_resources_directory():
        return Path.resources_directory

    @staticmethod
    def set_xml_direcory(xml_direcory):
        Path.xml_directory = xml_direcory
    
    @staticmethod
    def get_xml_directory():
        return Path.xml_directory
    