import os

class path:
    def __init__(self):
        self.xml_directory: str
        self.report_directory: str
    
    def set_xml_direcory(self, xml_direcory):
        self.xml_directory = xml_direcory
        #if os.path.exists(xml_direcory):
        
    def get_xml_directory(self):
        return self.xml_directory
    
    def set_report_direcory(self, report_direcory):
        self.report_directory = report_direcory
      
    def get_report_directory(self):
        return self.report_directory