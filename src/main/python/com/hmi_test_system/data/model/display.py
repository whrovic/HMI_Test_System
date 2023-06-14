from .position import Position


class Display():
    
    def __init__(self, name: str, chr_reference_path: str = None, pal_reference_path: str = None):
        self._name = name
        self._chr_reference_path = chr_reference_path
        self._pal_reference_path = pal_reference_path

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name

    def get_chr_reference_path(self):
        return self._chr_reference_path
    
    def set_chr_reference_path(self, chr_reference_path):
        self._chr_reference_path = chr_reference_path

    def get_pal_reference_path(self):
        return self._pal_reference_path
    
    def set_pal_reference_path(self, pal_reference_path):
        self._pal_reference_path = pal_reference_path
    