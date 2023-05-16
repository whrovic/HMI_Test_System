from report.log_display import LogDisplay
from opencv.hmicv import HMIcv
from video.camera import Camera
from serial.serial_port import SerialPort
import time

from ..data.model.model import Model
from ..model_test.model_test import ModelTest
from ..model_test.led_test import LedTest
from ..model_test.button_test import ButtonTest
from ..model_test.display_test import DisplayTest
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..data.color.color import Color

cam_value: Camera
vet_cor: [37]
vet_cor_bef: [37]


# TODO: complet the start_test and end_test
# with the right functions

class Test:

    @staticmethod
    def test_button_display(button_sequence: list[Button]):
        return -1

    # return 0 - Test passed, -1 not passed
    @staticmethod
    def test_button_serial_port(serial: SerialPort, button_sequence: list[Button]):
        
        for button in button_sequence:
            data, time = serial.get_serial()
            if data.startswith("TestKeys - Pressed:") and data.endswith(button.get_name):
                serial.get_serial()
                continue
            return -1
        
        data, time = serial.get_serial()
        if data != "TestKeys - Test OK":
            return -1
        
        return 0

    @staticmethod
    def test_button(cam: Camera, serial: SerialPort, button_sequence: list[Button], SP = True, DP = False):
        return Test.test_button_serial_port(serial, button_sequence)


    @staticmethod
    def test_display(cam: Camera, serial: SerialPort, display: Display):

        # Initializing the test variables
        test_name = None
        test_start_time = None
        test_failed = False

        # Variables for the next test
        new_test_name = None
        new_test_start_time = None

        # Debug
        log_display = LogDisplay()

        while True:
            # Get the data from the serial port with a timeout
            data, data_time = serial.get_serial(timeout=0.1)

            # Check if the data is related to the display test
            if data is not None:
                # Determine which type of test is being performed
                if "Test PIX" in data:
                    new_test_name = "PIX"
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif "Test CHR" in data:
                    new_test_name = "CHR"
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif "Test PAL" in data:
                    new_test_name = "PAL"
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif "CANCEL" in data:
                    # If the test was canceled, reset the test variables
                    new_test_name = None
                    test_name = None
                    test_start_time = None
                    new_test_start_time = None
                    log_display.test_canceled()

                elif "TestDisplay - Pressed: ENTER" in data:
                    log_display.test_finished()
                    break

            # Start the first test
            if test_name is None and new_test_name is not None:
                test_name = new_test_name
                test_start_time = new_test_start_time
                new_test_name = None
                new_test_start_time = None

            # If a test is currently running
            if test_name is not None:
                frame, frame_time = cam.get_image()

                # Check if the frame is related to the current test
                if frame_time < test_start_time:
                    continue
                elif frame_time >= new_test_start_time:
                    # Start the next test
                    log_display.test_failed(test_name)
                    test_failed = True
                    test_name = new_test_name
                    test_start_time = new_test_start_time
                    if test_name is None:
                        break
                    log_display.start_test(test_name)
                else:
                    # Perform the appropriate test based on the current test type
                    if test_name == "PIX":
                        if HMIcv.display_backlight_test(frame, display):
                            log_display.test_passed(test_name)
                            test_name = None
                            test_start_time = None
                        else:
                            continue

                    elif test_name == "CHR":
                        if HMIcv.display_characters_test(frame, display):
                            log_display.test_passed(test_name)
                            test_name = None
                            test_start_time = None
                        else:
                            continue
                        
                    elif test_name == "PAL":
                        if HMIcv.display_color_pattern_test(frame, display):
                            log_display.test_passed(test_name)
                            test_name = None
                            test_start_time = None
                        else:
                            continue

        # Return 0 if all tests passed, -1 if any test failed
        if test_failed:
            return -1
        else:
            return 0
        

    @staticmethod
    def start_test():
        cam_value.start_capture()

    @staticmethod
    def end_test():
        cam_value.stop_capture()

    def test_button_display(self, buttons_test: list[ButtonTest]):
        # for i in range(0, len(buttons_test)):
        #     result =
        pass

    def test_button_serial_port(self, buttons_test: list[ButtonTest]):
        # for i in range(0, len(buttons_test)):
        pass

    def test_button(self, buttons_test: list[ButtonTest]):
        self.test_button_display()
        self.test_button_serial_port()

    def test_led(self, leds_test: list[LedTest]):
        state = 0
        aux = 0
        while 1:
            cam = cam_value.get_image()
            for i in range(0, len(leds_test)):
                vet_cor[i] = HMIcv.led_test(cam, leds_test[i].get_led())
            if state == 0:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    state = 1
                else:
                    # fazer funçao de escrever no terminal
                    return -1
            if state == 1:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is None:
                        aux = aux + 1
                if aux == len(leds_test):
                    state = 2
                else:
                    # fazer funçao de escrever no terminal
                    return -1
            if state == 2:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    state = 3
                else:
                    # fazer funçao de escrever no terminal
                    return -1
            if state == 3:
                aux = 0
                #for i in range(0, len(leds_test)):
                if vet_cor[0].get_name() == 'green' and vet_cor[0].get_name() != vet_cor_bef[0].get_name():



    def test_display(self, display: DisplayTest, test):
        if test == 1:
            result_blacklight = HMIcv.display_backlight_test(cam_value.get_image(), display.display)
            if result_blacklight:
                display.test_blacklight(result_blacklight)
                return 0
            else:
                return -1

        elif test == 2:
            result_color = HMIcv.display_color_pattern_test(cam_value.get_image(), display.display)
            if result_color:
                display.test_color(result_color)
                return 0
            else:
                return -1

        elif test == 3:
            result_character = HMIcv.display_characters_test(cam_value.get_image(), display.display)
            if result_character:
                display.test_characters(result_character)
                return 0
            else:
                return -1

        elif test == 4:
            result_blacklight = HMIcv.display_backlight_test(cam_value.get_image(), display.display)
            result_color = HMIcv.display_color_pattern_test(cam_value.get_image(), display.display)
            result_character = HMIcv.display_characters_test(cam_value.get_image(), display.display)
            if result_blacklight:
                display.test_blacklight(result_blacklight)
            else:
                return -1
            if result_color:
                display.test_color(result_color)
            else:
                return -1
            if result_character:
                display.test_characters(result_character)
                return 0
            else:
                return -1
