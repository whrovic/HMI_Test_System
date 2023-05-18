#from test.Test import Test
from data.model.button import Button
from data.model.led import Led
from data.model.display import Display
from data.model.model import Model
from .test import Test
from serial_port.serial_port import SerialPort

class SequenceTest:

    @staticmethod
    def seq_button(model: Model, buttons_test: list[str], sp: bool, dsp: bool):

        button_sequence = []
        for button_name in buttons_test:
            button = model.get_button(button_name)
            if button is None:
                # TODO: Catch exit code
                return -2
            button_sequence.append(button)

        # TODO: As portas série e camaras não são iniciadas, nem startadas aqui
        # TODO: Isto é código inicial para teste
        serial1 = SerialPort('COM5')
        serial1.start_receive()

        # Waits for serial port TestKeys begin
        while True:
            d, _ = serial1.get_serial()
            d = str(d)
            if d is not None and d.startswith('TestKeys'):
                break

        # Start button test
        result = Test.test_button(None, serial1, button_sequence, sp, dsp)

        # TODO: This has to get away from here
        serial1.stop_receive()
        serial1.clear_queue()

        return result
    
    @staticmethod
    def seq_led(model: Model, leds_test: list[str]):
        return -1
    
    @staticmethod
    def seq_display(model: Model, dsp: Display):
        return -1