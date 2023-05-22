from .. import serial
from ..report.log_display import LogDisplay
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..serial.serial_port import SerialPort
import time

from ..data.model.button import Button
from ..data.model.display import Display
from ..data.model.led import Led
from ..data.model.model import Model
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..data.color.color import Color
from ..serial_port.constants import *

'''from report.log_display import LogDisplay
from opencv.hmicv import HMIcv
from video.camera import Camera
from serial_port.serial_port import SerialPort

from data.model.button import Button
from data.model.display import Display
from data.model.led import Led
from opencv.hmicv import HMIcv
from video.camera import Camera
from data.color.color import Color
from serial_port.constants import *'''


cam_value: Camera

N = 37
NN = 56
vet_cor: list[N]
vet_cor_bef: list[NN][N]
leds_on: list[N]


# TODO: complet the start_test and end_test
# with the right functions

class Test:

    @staticmethod
    def start_test():
        cam_value.start_capture()

    @staticmethod
    def end_test():
        cam_value.stop_capture()

    @staticmethod
    def test_button_display(button_sequence: list[Button]):
        return -1

    # return: 0 - Test passed, -1 not passed
    @staticmethod
    def test_button_serial_port(serial: SerialPort, button_sequence: list[Button]):

        for button in button_sequence:
            data = None
            while data is None:
                data, time = serial.get_serial()

            data = str(data)
            if data.startswith(TEST_BUTTONS) and data.endswith(button.get_name()):
                d = None
                while d is None:
                    d, _ = serial.get_serial()
                continue
            return -1

        data, time = serial.get_serial()
        if data != TEST_BUTTONS_OK:
            return -1

        return 0

    @staticmethod
    def test_button(cam: Camera, serial: SerialPort, button_sequence: list[Button], SP=True, DP=False):
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
                    new_test_name = PIXEL
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif "Test CHR" in data:
                    new_test_name = CHAR
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif "Test PAL" in data:
                    new_test_name = COLOR
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif "CANCEL" in data:
                    # If the test was canceled, reset the test variables
                    new_test_name = None
                    test_name = None
                    test_start_time = None
                    new_test_start_time = None
                    log_display.test_canceled()

                elif TEST_DISPLAY_ENTER in data:
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
                    if test_name == PIXEL:
                        if HMIcv.display_backlight_test(frame, display):
                            log_display.test_passed(test_name)
                            test_name = None
                            test_start_time = None
                        else:
                            continue

                    elif test_name == CHAR:
                        if HMIcv.display_characters_test(frame, display):
                            log_display.test_passed(test_name)
                            test_name = None
                            test_start_time = None
                        else:
                            continue
                        
                    elif test_name == COLOR:
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

    def test_led(self, leds_test: list[Led], seriall: SerialPort):
        #N = 37   - > 3 leds control + 16 leds alarms + 9*2 leds buttons 
        #NN = 56  - > 3*2 (2 colors) + 16*2 (2 colors) + 18 
        #TODO: N = len of list leds
        state = 0
        while 1:
            cam = cam_value.get_image()

            for i in range(0, len(leds_test)):
                vet_cor[i] = HMIcv.led_test(cam, leds_test[i])
                
            #Test All Leds ON
            if state == 0:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    led_test_pass_terminal(state)
                    state = 1
                else:
                    led_test_error_terminal(state)
                    return -1

            #Test All Leds OFF
            if state == 1:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is None:
                        aux = aux + 1
                if aux == len(leds_test):
                    led_test_pass_terminal(state)
                    state = 2
                else:
                    led_test_error_terminal(state)
                    return -1

            #Test All Leds ON
            if state == 2:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    led_test_pass_terminal(state)
                    state = 3
                else:
                    led_test_error_terminal(state)
                    return -1

            if state == 3:
                aux = 0
                errors = []
                error_counter = 0
                cam_bef = None
                chegada = None #bad names XD
                chegada_serial, chegada_time = None, None #bad names XD
                while(chegada_serial != "TestLeds - Test OK") and (chegada_time != chegada):
                    #TODO: for not necessary, better while, while SP_time < dsp_time
                    #Just update SP when equal to null
                    #Exit if SP = 'cancel' or timeout
                    for i in range(0, 56):
                        for j in range(0, len(leds_test)):
                            if cam != cam_bef:
                                vet_cor_bef[i][j] = HMIcv.led_test(cam, leds_test[i])
                        cam_bef = cam 
                        chegada_bef = chegada
                        cam, chegada = cam_value.get_image()
                        if chegada_serial != TEST_LEDS_OK:
                            chegada_serial, chegada_time = seriall.get_serial()

                    #Confirm if sequence is right (??)
                    for i in range(0, 56):
                        for j in range(0, len(leds_test)):
                            if vet_cor_bef[i][j] != "OFF":
                                if leds_on[i] is None:
                                    leds_on[i] = vet_cor_bef[i][j]
                                    vet_cor_bef[i][j] = "OFF"

                    for i in range(0, 56):
                        for j in range(0, len(leds_test)):
                            if vet_cor_bef[i][j] != "OFF":
                                errors[error_counter] = j
                                error_counter = error_counter + 1

                    if error_counter != 0:
                        led_test_error_terminal(4)
                        return -1
                    else:
                        led_test_pass_terminal(4)

                    for j in range(0, 56):
                        for k in range(0, len(leds_test[j].get_colours())):
                            if leds_on[j] == leds_test[j].get_colours()[k] and k == 0:
                                aux = aux + 1
                                break
                            elif leds_on[j] == leds_test[j].get_colours()[k] and k == 1:
                                aux = aux + 1
                                break
                    if aux == 56:
                        led_test_pass_terminal(3)
                        return 0
                    else:
                        led_test_error_terminal(3)
                        return -1


def led_test_error_terminal(code):
    if code == 0 or code == 2:
        print("Error on turned on LED's\n")
    elif code == 1:
        print("Error on turned off LED's\n")
    elif code == 3:
        print("Error in sequence LED's test\n")
    elif code == 4:
        print("Error: LED ON when OFF\n")


def led_test_pass_terminal(code):
    if code == 0 or code == 2:
        print("All the LED's Turn ON\n")
    elif code == 1:
        print("All the LED's Turn OFF\n")
    elif code == 3:
        print("Sequence LED test passed\n")
    elif code == 4:
        print("All LED's OFF when OFF\n")
