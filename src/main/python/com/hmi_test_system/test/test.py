'''from .. import serial_port
from ..report.log_display import LogDisplay
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..serial_port.serial_port import SerialPort
import time
from ..report.exit_code import ExitCode
from ..report.log_leds import LogLeds

from ..data.model.button import Button
from ..data.model.display import Display
from ..data.model.led import Led
from ..data.model.model import Model
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..data.color.color import Color
from ..serial_port.constant_test import *'''

from report.log_display import LogDisplay
from report.log_leds import LogLeds
from report.exit_code import ExitCode
from opencv.hmicv import HMIcv
from video.camera import Camera

from data.model.button import Button
from data.model.display import Display
from data.model.led import Led
from data.color.color import Color
from serial_port.constant_test import *
from serial_port.serial_port import SerialPort

cam_value: Camera


# TODO: complet the start_test and end_test
# with the right functions

class Test:

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
    def test_button(cam: Camera, serial: SerialPort, button_sequence: list[Button], dsp = False):
        # TODO: Make this for camara as well
        if serial is not None:
            return Test.test_button_serial_port(serial, button_sequence)
        return -1


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

    @staticmethod
    def test_boot_loader_info(cam, serial, version, date):
        return -1
    
    @staticmethod
    def test_board_info(cam, serial, board, serial_number, manufacture_date, option, revision, edition, lcd_type):
        return -1
    
    @staticmethod
    def test_alight(cam, serial):
        return -1


    def test_led(self, leds_test: list[Led], seriall: SerialPort):
        N = len(leds_test)
        NN = 56
        vet_cor: list[N]
        vet_cor_bef: list[NN][N]
        leds_on: list[N]
        matrix_ref: list[NN][N]
        cam_bef = None
        error = 0
        arrive_time_cam = None
        arrive_serial, arrive_time_serial = None, None

        # N = 37   - > 3 leds control + 16 leds alarms + 9*2 leds buttons
        # NN = 56  - > 3*2 (2 colors) + 16*2 (2 colors) + 18
        # TODO: N = len of list leds

        state = 0
        log_leds = LogLeds()

        while 1:
            cam, arrive_time_cam = cam_value.get_image()

            for i in range(0, N):
                vet_cor[i] = HMIcv.led_test(cam, leds_test[i])

            # Test All Leds ON
            if state == 0:
                aux = 0

                for i in range(0, N):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == N:
                    log_leds.test_leds_on_passed()
                    state = 1
                else:
                    log_leds.test_failed()
                    return -1

            # Test All Leds OFF
            if state == 1:
                aux = 0
                for i in range(0, N):
                    if vet_cor[i] is None:
                        aux = aux + 1
                if aux == len(leds_test):
                    log_leds.test_leds_off_passed()
                    state = 2
                else:
                    log_leds.test_failed()
                    return -1

            # Test All Leds ON
            if state == 2:
                aux = 0
                for i in range(0, N):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == N:
                    log_leds.test_leds_on_passed()
                    state = 3
                else:
                    log_leds.test_failed()
                    return -1

            if state == 3:
                aux_led = 0
                x = 0
                y = 0

                for i in range(0, NN):
                    for j in range(0, N):
                        matrix_ref[i][j] = "OFF"
                # TODO: for can be upgraded to take in to account more colors in a single LED
                for i in range(0, NN):
                    if (aux_led == 0) and (len(leds_test[y].get_colours()) == 2):
                        matrix_ref[x][y] = leds_test[y].get_colours()[aux_led]
                        x = x + 1
                        aux_led = 1
                    if (aux_led == 1) and (len(leds_test[y].get_colours()) == 2):
                        matrix_ref[x][y] = leds_test[y].get_colours()[aux_led]
                        x = x + 1
                        y = y + 1
                        aux_led = 0
                    if (aux_led == 0) and (len(leds_test[y].get_colours()) != 2):
                        matrix_ref[x][y] = leds_test[y].get_colours()[aux_led]
                        x = x + 1
                        y = y + 1
                        aux_led = 1

                x = 0
                arrive_serial, arrive_time_serial = seriall.get_serial()

                while 1: 
                    if arrive_serial is None:
                        arrive_serial, arrive_time_serial = seriall.get_serial()

                    for j in range(0, N):
                        if cam != cam_bef:
                            vet_cor_bef[x][j] = HMIcv.led_test(cam, leds_test[j])
                    cam_bef = cam
                    cam, arrive_time_cam = cam_value.get_image()

                    x = x + 1
                    if (arrive_serial == TEST_LEDS_OK) and (arrive_time_serial < arrive_time_cam):
                        break
                    if arrive_serial == TEST_LEDS_CANCEL:
                        log_leds.test_canceled()
                        ExitCode.leds_test_not_passed()
                        return -1

                for i in range(0, NN):
                    if matrix_ref[i] != vet_cor_bef[i]:
                        for j in range(0, N):
                            if matrix_ref[i][j] == "OFF":
                                if matrix_ref[i][j] != vet_cor_bef[i][j]:
                                    log_leds.test_leds_sequence_colour_failed(leds_test[j].get_name(), matrix_ref[i][j],
                                                                              vet_cor_bef[i][j])
                                    ExitCode.leds_test_colour_sequence_error()
                                    error = error + 1
                            else:
                                if matrix_ref[i][j] != vet_cor_bef[i][j]:
                                    log_leds.test_leds_sequence_state_failed(leds_test[j].get_name(), matrix_ref[i][j], 
                                                                             vet_cor_bef[i][j])
                                    ExitCode.leds_test_state_sequence_error()
                                    error = error + 1
                if error == 0:
                    log_leds.test_leds_sequence_passed()
                    log_leds.test_finished()
                    return 0
                else:
                    log_leds.test_leds_sequence_failed()
                    ExitCode.leds_test_not_passed()
                    return -1




