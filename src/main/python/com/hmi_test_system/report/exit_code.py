class ExitCode:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        ExitCode.exit_code = 0
    
    @staticmethod
    def failure_excetution():
        ExitCode.update_value(1)

    @staticmethod
    def failure_model():
        ExitCode.update_value(2)

    @staticmethod
    def invalid_arguments():
        ExitCode.update_value(3)
    
    @staticmethod
    def invalid_number_arguments():
        ExitCode.update_value(4)
    
    @staticmethod
    def failure_camera():
        ExitCode.update_value(5)
    
    @staticmethod
    def failure_serial_port():
        ExitCode.update_value(6)
    
    @staticmethod
    def failure_led_test():
        ExitCode.update_value(8)
    
    @staticmethod
    def failure_display_test():
        ExitCode.update_value(9)
    
    @staticmethod
    def failure_button_test():
        ExitCode.update_value(10)
    
    @staticmethod
    def update_value(new):
        if ExitCode.exit_code is 0:
            ExitCode.exit_code = new