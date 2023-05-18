
exit_code = 0

class ExitCode:
    def __init__(self):
        self.exit_code = 0
    
    def failure_excetution(self):
        self.exit_code = 1
    
    def failure_model(self):
        self.exit_code = 2
    pass