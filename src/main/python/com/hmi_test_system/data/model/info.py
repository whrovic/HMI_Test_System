class Info:
    
    def __init__(self, board: str, option: str, revision: str, edition: str, lcd_type: str):
        self._board = board
        self._option = option
        self._revision = revision
        self._edition = edition
        self._lcd_type = lcd_type

    def get_board(self):
        return self._board
    
    def set_board(self, board: str):
        self._board = board
    
    def get_option(self):
        return self._option
    
    def set_option(self, option: str):
        self._option = option
        
    def get_revision(self):
        return self._revision
    
    def set_revision(self, revision: str):
        self._revision = revision
        
    def get_edition(self):
        return self._edition
    
    def set_edition(self, edition: str):
        self._edition = edition
        
    def get_lcd_type(self):
        return self._lcd_type
    
    def set_lcd_type(self, lcd_type: str):
        self._lcd_type = lcd_type