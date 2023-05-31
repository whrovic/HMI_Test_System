class Info:
    
    def __init__(self, board: str, option: str, revision: str, edition: str):
        self._board = board
        self._option = option
        self._revision = revision
        self._edition = edition

    def get_board(self):
        return self._board
    
    def get_option(self):
        return self._option
    
    def get_revision(self):
        return self._revision
    
    def get_edition(self):
        return self._edition
