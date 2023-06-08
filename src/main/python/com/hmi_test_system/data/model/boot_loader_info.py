class BootLoaderInfo:

    def __init__(self, version: str, date: str):
        self._version = version
        self._date = date

    def get_version(self):
        return self._version
    
    def set_version(self, version):
        self._version = version

    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date
    