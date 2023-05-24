
exit_code = 0

class ExitCode:
    def __init__(self):
        ExitCode.exit_code = 0
    
    @staticmethod
    def failure_excetution():
        ExitCode.exit_code = 1
        
    @staticmethod
    def failure_model():
        ExitCode.exit_code = 2
    pass