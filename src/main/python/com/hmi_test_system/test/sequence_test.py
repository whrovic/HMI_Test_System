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
        
        for b in buttons_test:
            print(b)

        button_sequence = []
        for button_name in buttons_test:
            button = model.get_button(button_name)
            if button is None:
                # TODO: Catch exit code
                return -2
            button_sequence.append(button)

        print("Opening serial port communication")

        # TODO: As portas série e camaras não são iniciadas, nem startadas aqui
        # TODO: Isto é código inicial para teste
        serial1 = SerialPort('COM3')
        serial1.start_receive()

        print("Serial Port communication openned")

        # Waits for serial port TestKeys begin
        while True:
            d, _ = serial1.get_serial()
            if d is not None and d.startswith('TestKeys'):
                break

        print("Buttons Tests started")

        # Start button test
        result = Test.test_button(None, serial1, button_sequence, sp, dsp)

        print(result)

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