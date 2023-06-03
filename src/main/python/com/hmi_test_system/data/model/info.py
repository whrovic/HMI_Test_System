class Info:
    
    def __init__(self, board: str, serial_number: str, manufacture_date: str, option: str, revision: str, edition: str, lcd_type: str):
        self._board = board
        self.serial_number = serial_number
        self.manufacture_date = manufacture_date
        self._option = option
        self._revision = revision
        self._edition = edition
        self.lcd_type = lcd_type

    def get_board(self):
        return self._board
    
    def get_serial_number(self):
        return self.serial_number
    
    def get_manufacture_date(self):
        return self.manufacture_date
    
    def get_option(self):
        return self._option
    
    def get_revision(self):
        return self._revision
    
    def get_edition(self):
        return self._edition
    
    def get_lcd_type(self):
        return self.lcd_type
