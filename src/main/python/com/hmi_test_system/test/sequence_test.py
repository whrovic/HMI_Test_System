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
    def seq_button(model: Model, buttons_test, sp: bool, dsp: bool):
        
        # If no test configuration is provided return immediatly
        if not sp and not dsp:
            return 0

        # TODO: This shouldn't be defined here
        TIMEOUT = 10

        # Gets the buttons to test
        if buttons_test is None:
            # If no button names are provided, get everyone from the model
            button_sequence = model.get_buttons()
        else:
            button_sequence = [model.get_button(button_name) for button_name in buttons_test]
            if None in button_sequence:
                # Invalid button names
                ExitCode.invalid_argument()
                return -1

        # Open the needed connections
        SetupTest.setup(False, dsp, sp, False)

        # Check connections status
        serial_port = SetupTest.__sp_main
        if sp and serial_port.closed():
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
        
        # Start receiving data from serial port and/or display
        if sp:
            serial_port.start_receive()
        if dsp:
            cam.start_capture()

        # Waits for serial port and/or display TestKeys begin
        # If both are active, it should only start the tests when both are syncronized
        # TODO: Also wait for the camara if needed
        begin_waiting_time = time()
        received_sp = received_dsp = False
        ready_sp = ready_dsp = False
        while True:
            now = time()

            # Check if the serial port timed out waiting for the first received data
            if (sp and not received_sp and (now - begin_waiting_time > TIMEOUT)):
                # No data was received from the serial port
                # TODO: Catch this error
                SetupTest.close()
                ExitCode.serialport_timeout_reception()
                return -1
            # Check if the camara timed out waiting for the first received data
            if (dsp and not received_dsp and (now - begin_waiting_time > TIMEOUT)):
                # No data was received from the camara
                # TODO: Catch this error
                SetupTest.close()
                ExitCode.camera_timeout_reception()
                return -1
            
            # Get data from serial port
            if sp and not ready_sp:
                data, _ = serial_port.get_serial()
            
                if data is not None:
                    received_sp = True
                    
                    data = str(data)
                    if data.startswith(TEST_BUTTONS_BEGIN):
                        ready_sp = True
            
            # Get data from camara
            if dsp and not ready_dsp:
                img, _ = cam.get_image()

                if img is not None:
                    received_dsp = True

                    text = Displaycv.read_char(img)
                    if text is not None and TEST_BUTTONS_BEGIN in text:
                        ready_dsp = True

            # If the tests have began, stop waiting
            if (ready_sp == sp and ready_dsp == dsp):
                break

            sleep(0.1)

        # Start button test
        result = Test.test_button(cam, serial_port, button_sequence)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_boot_loader_info(model: Model):
        return -1
    
    @staticmethod
    def seq_board_info(model: Model):
        return -1
    
    @staticmethod
    def seq_alight(model: Model):
        return -1

    @staticmethod
    def seq_led(model: Model, leds_test: list[str]):
        return -1
    
    @staticmethod
    def seq_display(model: Model):
        return -1