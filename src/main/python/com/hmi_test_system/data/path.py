import os

class Path:
    def __init__(self):
        file_path = os.path.dirname(__file__)

        Path.xml_directory = os.path.join(file_path, '../../../../../../xml_files')
        Path.report_directory = os.path.join(file_path, '../../../../../../reports')
        Path.resources_directory = os.path.join(file_path, '../../../../resources')
        Path.settings_directory = os.path.join(file_path, '../../../../../../settings')

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
    
    @staticmethod
    def set_report_direcory(report_direcory):
        Path.report_directory = report_direcory
      
    @staticmethod
    def get_report_directory():
        return Path.report_directory