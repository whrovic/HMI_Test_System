from time import sleep, time

from data.model.button import Button
from data.model.display import Display
from data.model.led import Led
from data.model.model import Model
from opencv.displaycv import Displaycv
from report import *
from serial_port.constant_test import *
from serial_port.serial_port import SerialPort

from .setup_test import SetupTest
from .test import Test


class SequenceTest:

    @staticmethod
    def seq_button(model: Model, buttons_test = None, dsp = False):

        # TODO: This shouldn't be defined here
        TIMEOUT = 10

        # Gets the buttons to test
        if buttons_test is None:
            # If no button names are provided, get everyone from the model
            button_sequence = model.get_buttons()
        else:
            button_sequence = []
            for button_name in buttons_test:
                button = model.get_button(button_name)
                if button is None:
                    # If the button name was not found in the model, return
                    ExitCode.key_name_not_found()
                    return -1
                # Add the button to the sequence
                button_sequence.append(button)

        # Open the needed connections
        SetupTest.setup(False, dsp, True, False)

        # Check connections status
        serial_port = SetupTest.__sp_main
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            ExitCode.serialport_connection_failure()
            return -1
        cam = SetupTest.__cam_display
        if dsp and cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            ExitCode.camera_connection_failure()
            return -1
        
        # Start receiving data from serial port
        serial_port.start_receive()

        print("Serial Port communication openned")

        # Waits for serial port TestKeys begin
        begin_waiting_time = time()
        received_sp = False
        while True:
            now = time()

            # Check if the serial port timed out waiting for the first received data
            if (not received_sp and (now - begin_waiting_time > TIMEOUT)):
                # No data was received from the serial port
                # TODO: Catch this error
                SetupTest.close()
                ExitCode.serialport_timeout_reception()
                return -1
            
            # Get data from serial port
            data, _ = serial_port.get_serial()

            if data is not None:
                received_sp = True
                
                data = str(data)
                if data.startswith(TEST_BUTTONS_BEGIN):
                    break
            
            sleep(0.1)

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        print("Buttons Tests started")

        # Start button test
        result = Test.test_button(cam, serial_port, button_sequence)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_boot_loader_info(model: Model, dsp = False):
        return -1
    
    @staticmethod
    def seq_board_info(model: Model, dsp = False):
        return -1
    
    @staticmethod
    def seq_alight(dsp = False):
        return -1

    @staticmethod
    def seq_led(model: Model, leds_test = None):
        
        # TODO: This shouldn't be defined here
        TIMEOUT = 10

        # Gets the leds to test
        if leds_test is None:
            # If no led names are provided, get everyone from the model
            leds_sequence = model.get_leds
        else:
            leds_sequence = []
            for led_name in leds_test:
                led = model.get_led(led_name)
                if led is None:
                    # If the led name was not found in the model, return
                    ExitCode.key_name_not_found()
                    return -1
                # Add the led to the sequence
                leds_sequence.append(led)

        # Open the needed connections
        SetupTest.setup(True, False, True, False)

        # Check connections status
        serial_port = SetupTest.__sp_main
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            ExitCode.serialport_connection_failure()
            return -1
        cam = SetupTest.__cam_display
        if cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            ExitCode.camera_connection_failure()
            return -1
        
        # Start receiving data from serial port
        serial_port.start_receive()

        # Waits for serial port TestKeys begin
        begin_waiting_time = time()
        received_sp = False
        while True:
            now = time()

            # Check if the serial port timed out waiting for the first received data
            if (not received_sp and (now - begin_waiting_time > TIMEOUT)):
                # No data was received from the serial port
                # TODO: Catch this error
                SetupTest.close()
                ExitCode.serialport_timeout_reception()
                return -1
            
            # Get data from serial port
            data, _ = serial_port.get_serial()

            if data is not None:
                received_sp = True
                
                data = str(data)
                if data.startswith(TEST_LEDS_BEGIN):
                    break
            
            sleep(0.1)

        # Start recording images
        cam.start_capture()

        # Start led test
        result = Test.test_led(cam, serial_port, leds_sequence)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_display(model: Model):
        return -1