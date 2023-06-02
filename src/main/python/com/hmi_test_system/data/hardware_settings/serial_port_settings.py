class SerialPortSettings:

    def __init__(self, name: str, baudrate: int, port: str):
        self._name = name
        self._baudrate = baudrate
        self._port = port

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name