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
        # Start receiving from the serial port   
        serial.start_receive() 

        test_name = None
        test_start_time = None
        test_failed = False

        while True:

            # Get the data from the serial port
            data, _ = serial.get_serial() 
            
            # Check if the data is related to the display test
            if data is not None:
                if "TestDisplay - Testing..." in data: # Check if the data is related to the display test
                    # Determine which type of test is being performed
                    if "Test PIX" in data:
                        test_name = "PIX"
                        test_start_time = float(data.split(":")[1])
                        print("Starting PIX Test")

                    elif "Test CHR" in data:
                        test_name = "CHR"
                        test_start_time = float(data.split(":")[1])
                        print("Starting CHR Test")

                    elif "Test PAL" in data:
                        test_name = "PAL"
                        test_start_time = float(data.split(":")[1])
                        print("Starting PAL Test")

                    elif "Cancel" in data:
                        # If the test was canceled, reset the test variables
                        if test_name is not None:
                            print("TestDisplay Canceled")
                        test_name = None
                        test_start_time = None

                    elif "TestDisplay - Pressed: ENTER" in data:
                        if test_name is not None:
                            print("TestDisplay Finished")
                        break

            # If a test is currently running
            if test_name is not None:
                frame_time = time.time()
                frame = cam.get_frame()

                # If the test duration has elapsed, the test has passed
                if frame_time >= test_start_time:
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None

                # If the data is related to a different test, the current test has failed
                elif data is not None and "TestDisplay" in data and test_name != data.split()[1]:
                    print(f"{test_name} Test Not Passed")
                    test_failed = True
                    test_name = None
                    test_start_time = None
                
                # Perform the appropriate test based on the current test type
                elif HMIcv.display_backlight_test(frame, display) and test_name == "PIX":
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None

                elif HMIcv.display_characters_test(frame, display) and test_name == "CHR":
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None

                elif HMIcv.display_color_pattern_test(frame, display) and test_name == "PAL":
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None
        
        # Stop receiving from the serial port
        serial.stop_receive() 

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