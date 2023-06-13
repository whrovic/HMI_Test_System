class SerialPortSettings:

    def __init__(self, name: str, port: str, baudrate: int):
        self._name = name
        self._baudrate = baudrate
        self._port = port

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def get_port(self):
        return self._port
    
    def set_port(self, port):
        self._port = port

    def get_baudrate(self):
        return self._baudrate
    
    def set_baudrate(self, baudrate):
        self._baudrate = baudrate
        