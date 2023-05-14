from opencv.hmicv import HMIcv
from video.camera import Camera
from serial.serial_port import SerialPort
import time

from data.model.display import Display
from data.model.button import Button
from data.model.led import Led


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

        while True:
            # Get the data from the serial port with a timeout
            data, data_time = serial.get_serial(timeout=0.1)

            # Check if the data is related to the display test
            if data is not None:
                # Determine which type of test is being performed
                if "Test PIX" in data:
                    new_test_name = "PIX"
                    new_test_start_time = data_time

                elif "Test CHR" in data:
                    new_test_name = "CHR"
                    new_test_start_time = data_time

                elif "Test PAL" in data:
                    new_test_name = "PAL"
                    new_test_start_time = data_time

                elif "CANCEL" in data:
                    # If the test was canceled, reset the test variables
                    new_test_name = None
                    test_name = None
                    test_start_time = None
                    new_test_start_time = None

                elif "TestDisplay - Pressed: ENTER" in data:
                    break

            # If a test is currently running
            if test_name is not None:
                frame, frame_time = cam.get_image()

                # Check if the frame is related to the current test
                if frame_time < test_start_time:
                    continue
                elif frame_time >= new_test_start_time:
                    # Start the next test
                    print(f"{test_name} Test Failed")
                    test_failed = True
                    test_name = new_test_name
                    test_start_time = new_test_start_time
                    if test_name is None:
                        break
                else:
                    # Perform the appropriate test based on the current test type
                    if test_name == "PIX":
                        if HMIcv.display_backlight_test(frame, display):
                            print(f"{test_name} Test Passed")
                            test_name = None
                            test_start_time = None
                        else:
                            continue

                    elif test_name == "CHR":
                        if HMIcv.display_characters_test(frame, display):
                            print(f"{test_name} Test Passed")
                            test_name = None
                            test_start_time = None
                        else:
                            continue
                        
                    elif test_name == "PAL":
                        if HMIcv.display_color_pattern_test(frame, display):
                            print(f"{test_name} Test Passed")
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
        pass

    @staticmethod
    def end_test():
        pass

    @staticmethod
    def test_led(cam: Camera, led_sequence: list[Led]):
        return -1