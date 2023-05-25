
exit_code = 0

class ExitCode:
    def __init__(self):
        ExitCode.exit_code = 0
    
    @staticmethod
    def failure_excetution():
        ExitCode.update_value(1)

    @staticmethod
    def failure_model():
        ExitCode.update_value(2)

    def invalid_arguments():
        ExitCode.update_value(3)
        
    def invalid_number_arguments():
        ExitCode.update_value(4)
        
    def failure_camera():
        ExitCode.update_value(5)
    
    def failure_serial_port():
        ExitCode.update_value(6)
    
    def failure_led_test():
        ExitCode.update_value(8)
    
    def failure_display_test():
        ExitCode.update_value(9)
    
    def failure_button_test():
        ExitCode.update_value(10)
    
    @staticmethod
    def update_value(new):
        if ExitCode.exit_code is 0:
            ExitCode.exit_code = new