#from test.Test import Test
from data.model.button import Button
from data.model.led import Led
from data.model.display import Display
from data.model.model import Model
from .test import Test
from serial.serial_port import SerialPort

class SequenceTest:

    @staticmethod
    def seq_button(model: Model, buttons_test: list[str], sp: bool, dsp: bool):
        
        # TODO: As portas série e camaras não são iniciadas, nem startadas aqui
        # TODO: Isto é código inicial para teste

        try:
            serial1 = SerialPort('COM3')
        except:
            # TODO: Change this
            print("Port COM3 not connected")
            return -1

        serial1.start_receive()

        button_sequence = []
        for button_name in buttons_test:
            button = model.get_button(button_name)
            if button is None:
                # TODO: Change exit code
                return -1

        result = Test.test_button(None, serial1, button_sequence, sp, dsp)

        serial1.stop_receive()
        serial1.clear_queue()

        return result
    
    @staticmethod
    def seq_led(model: Model, leds_test: list[str]):
        return 0
    
    @staticmethod
    def seq_display(model: Model, dsp: Display):
        return 0