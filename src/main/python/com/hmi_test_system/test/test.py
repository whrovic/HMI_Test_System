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

from time import time

from data.color.color import Color, OffColor
from data.model.button import Button
from data.model.display import Display
from data.model.led import Led
from opencv.hmicv import HMIcv
from report import *
from serial_port.constant_test import *
from serial_port.serial_port import SerialPort
from src.main.python.com.hmi_test_system.opencv import displaycv
from video.camera import Camera
from report.exit_code import ExitCode


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

            print(button.get_name(), "error")
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
                if PIXEL in data:
                    new_test_name = PIXEL
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif CHAR in data:
                    new_test_name = CHAR
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

                elif COLOR in data:
                    new_test_name = COLOR
                    new_test_start_time = data_time
                    log_display.start_test(new_test_name)

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
    def test_boot_loader_info(cam : Camera, serial : SerialPort, version, date):

        if cam is not None: 
        # Start capturing camera feed
            cam.start_capture()

            try:
                # Wait for some time to ensure stable camera feed
                time.sleep(2)

                # Capture a frame from the camera
                frame = cam.get_frame()

                # Read the text from the display
                text = displaycv.read_char(frame)

                # Check if the version and date are present in the extracted text
                if version in text and date in text:
                    print("Display has the correct version of the HMI")
                    if date in text:
                        print("Display has the correct date of the HMI")
                        return 0
                    else: 
                        print("Boot Loader Info failed: Incorrect date of the HMI")
                        return -1
                else:
                    print("Boot Loader Info failed: Incorrect version of the HMI")
                    ExitCode.bootloader_test_not_passed()
                    return -1

            finally:
                # Close the camera
                cam.close()

        
        if cam is None: 
              
        # Wait for the response from the serial port

            response = None
            timeout = 5
            start_time = time.time()
            while time.time() - start_time < timeout:
                response, _ = serial.get_serial()
                if response is not None:
                    break

        # Check if the response is valid
            if response is None:
                print("Error: No response received from the serial port")
                ExitCode.bootloader_test_not_passed()
                return -1

        # Parse the response to extract the version and date
            received_info = response.split('\n')

        # Extract the version from the received info
            received_version = received_info[1].split(':')[1].strip()

        # Compare the received version with the expected version
            if received_version == version:
                print("Serial port has the correct version of the HMI")
            else:
                ExitCode.bootloader_test_not_passed()
                return -1

        # Wait for the response from the serial port for date
            response = None
            start_time = time.time()
            while time.time() - start_time < timeout:
                response, _ = serial.get_serial()
                if response is not None:
                    break

        # Check if the response is valid
            if response is None:
                print("Error: No response received from the serial port")
                ExitCode.bootloader_test_not_passed()
                return -1

        # Extract the date from the received info
            received_date = response.split(':')[1].strip()

        # Compare the received date with the expected date
            if received_date == date:
                print("Serial port has the correct date of the HMI")
                return 0
            else:
                print("Boot Loader Info failed: Incorrect date of the HMI")
                ExitCode.bootloader_test_not_passed()
                return -1

    
    @staticmethod

    def test_board_info(cam: Camera, serial: SerialPort, board, serial_number, manufacture_date, option, revision, edition, lcd_type):

        if cam is None:
        # Check the board information
            board_info, _ = serial.get_serial()
            if not board_info.startswith("TestBoardInfo - Board: " + board):
                print("Board Info Test failed: Incorrect board information")
                ExitCode.board_info_test_not_passed
                return -1
        

        # Check the serial number
            serial_number_info, _ = serial.get_serial()
            if serial_number_info.find("Serial Number: " + serial_number) == -1:
                print("Board Info Test failed: Incorrect serial number")
                ExitCode.board_info_test_not_passed
                return -1

        # Check the manufacture date
            manufacture_date_info, _ = serial.get_serial()
            if manufacture_date_info.find("Manufacture Date: " + manufacture_date) == -1:
                print("Board Info Test failed: Incorrect manufacture date")
                ExitCode.board_info_test_not_passed
                return -1

        # Check the option
            option_info, _ = serial.get_serial()
            if option_info.find("Option: " + option) == -1:
                print("Board Info Test failed: Incorrect option")
                ExitCode.board_info_test_not_passed
                return -1

        # Check the revision
            revision_info, _ = serial.get_serial()
            if revision_info.find("Revision: " + revision) == -1:
                print("Board Info Test failed: Incorrect revision")
                ExitCode.board_info_test_not_passed
                return -1

        # Check the edition
            edition_info, _ = serial.get_serial()
            if edition_info.find("Edition: " + edition) == -1:
                print("Board Info Test failed: Incorrect edition")
                ExitCode.board_info_test_not_passed
                return -1

        # Check the LCD type
            lcd_type_info, _ = serial.get_serial()
            if lcd_type_info.find("LCD Type: " + lcd_type) == -1:
                print("Board Info Test failed: Incorrect LCD type")
                ExitCode.board_info_test_not_passed
                return -1

        # All checks passed
            print("Board Info Test passed")
            return 0

    
    @staticmethod
    def test_alight(cam, serial):

        if cam is None:
    
            alight_info, _ = serial.get_serial()

            if alight_info.startswith("TestALight - ALight"):

                # Extract the ALight sensor value from the received info
                alight_value = float(alight_info.split(':')[1].strip().split('Lux')[0])
                
                # Check if the ALight sensor value is within the expected range
                if alight_value > 1000:
                    print("ALight sensor test passed")
                else:
                    print("ALight sensor test failed: Incorrect ALight value")
                    ExitCode.alight_test_not_passed
                    return -1
            else:
                print("ALight sensor test failed: No ALight value received")
                ExitCode.alight_test_not_passed
                return -1

            # Wait for the 'Cover up the ALight Sensor' 
            cover_prompt, _ = serial.get_serial()
            if cover_prompt.startswith("TestALight - Cover up the ALight Sensor"):

                # Wait for the Enter key press
                enter_press, _ = serial.get_serial()

                if enter_press.startswith("TestALight - Pressed: ENTER"):

                    # Wait for the ALight sensor value after covering
                    covered_alight_info, _ = serial.get_serial()

                    if covered_alight_info.startswith("TestALight - ALight"):

                        # Extract the covered ALight sensor value
                        covered_alight_value = float(covered_alight_info.split(':')[1].strip().split('Lux')[0])

                        if covered_alight_value < alight_value/2:
                            print("ALight sensor test passed (Covered)")
                            return 0
                        else:
                            print("ALight sensor test failed: Incorrect covered ALight value")
                            ExitCode.alight_test_not_passed
                            return -1
                    else:
                        print("ALight sensor test failed: No covered ALight value received")
                        ExitCode.alight_test_not_passed
                        return -1
                else:
                    print("ALight sensor test failed: Enter key press not received")
                    ExitCode.alight_test_not_passed
                    return -1
            else:
                print("ALight sensor test failed: 'Cover up the ALight Sensor' prompt not received")
                ExitCode.alight_test_not_passed
                return -1
            

    @staticmethod
    def test_led(cam: Camera, serial: SerialPort, leds_test: list[Led]):
        
        # TODO: Take this out of here
        TIMEOUT = 10

        # Number of leds
        n_leds_test = len(leds_test)
        # Total number of colours of all the leds
        total_n_colours = sum([l.get_n_Colour() for l in leds_test])
        # Saves the current state of the leds
        vet_cor: list[Color] = [OffColor()] * n_leds_test
        # Saves the expected sequence of colours in each led
        matrix_ref: list[list[Color]] = [[OffColor()] * n_leds_test] * total_n_colours
        
        # Create the reference matrix
        for i in range(0, total_n_colours):
            for j in range(0, n_leds_test):
                matrix_ref[i][j] = OffColor()
        pos = 0
        for i in range(n_leds_test):
            colours = leds_test[i].get_colours()
            for j in range(len(colours)):
                matrix_ref[pos][pos] = colours[j]
                pos += 1

        # Stores the time arrival of the image
        arrive_time_img = None
        # Stores the time arrival of the previous image
        old_arrive_time_img = time()
        # Stores the data and the time from the serialport
        serial_data, serial_data_time = None, None

        # Current state of the FSM
        state = 0
        log_leds = LogLeds()

        sequence_state = 0

        while True:

            # Read new image and call test of colors
            # save the info on a vector
            img, arrive_time_img = cam.get_image()
            if img is None:
                if time() - old_arrive_time_img > TIMEOUT:
                    # TODO: add log
                    ExitCode.camera_timeout_stopped()
                    return -1
                else:
                    continue
            else:
                old_arrive_time_img = arrive_time_img

            for i in range(0, n_leds_test):
                vet_cor[i] = HMIcv.led_test(img, leds_test[i])

            # Read from serial port
            if serial_data is None:
                serial_data, serial_data_time = serial.get_serial()
            # Check for the end of the tests
            if (serial_data == TEST_LEDS_OK) and (serial_data_time < arrive_time_img):
                log_leds.test_leds_sequence_passed()
                log_leds.test_finished()
                return 0
            elif sequence_state == total_n_colours:
                log_leds.test_leds_sequence_passed()
                log_leds.test_finished()
                return 0

            # Test All Leds ON
            if state == 0:
                
                for i in range(0, n_leds_test):
                    if isinstance(vet_cor[i], OffColor):
                        # TODO: log the led name
                        log_leds.test_failed()
                        ExitCode.leds_test_not_turn_all_on()
                        return -1

                log_leds.test_leds_on_passed()
                state = 1

            # Test All Leds OFF
            elif state == 1:
                
                # Counts the number of leds turned off
                n_off = 0
                for i in range(0, n_leds_test):
                    if isinstance(vet_cor[i], OffColor):
                        n_off += 1
                
                # If the leds still are all turned on, ignore this image and retry
                if n_off == 0:
                    continue
                # If all the leds are off procceed to the next state
                elif n_off == n_leds_test:
                    log_leds.test_leds_off_passed()
                    state = 2
                # TODO: Add timeout
                # If at least one led failed, return
                else:
                    log_leds.test_failed()
                    ExitCode.leds_test_not_turn_all_off()
                    return -1

            # Test All Leds ON
            elif state == 2:
                
                n_on = 0
                for i in range(0, n_leds_test):
                    if not isinstance(vet_cor[i], OffColor):
                        n_on += 1
                
                # If the leds still are all turned off, ignore this image and retry
                if n_on == 0:
                    continue
                # If all the leds are on procceed to the next state
                elif n_on == n_leds_test:
                    log_leds.test_leds_off_passed()
                    state = 2
                # TODO: Add timeout
                # If at least one led failed, return
                else:
                    log_leds.test_failed()
                    ExitCode.leds_test_not_turn_all_on()
                    return -1

            # Test the Sequence
            elif state == 3:

                # Check with the current state
                for i in range(n_leds_test):
                    if vet_cor[i].get_name() != matrix_ref[sequence_state+1][i].get_name():
                        break
                else:
                    # The current img matches the current state, so procceed to the next one
                    sequence_state += 1
                    continue

                # The new img is diferent from the expected one
                for i in range(n_leds_test):
                    if vet_cor[i].get_name() != matrix_ref[sequence_state][i].get_name():
                        break
                else:
                    # The current img is still equal to the previous state of the sequence
                    # TODO: Add timeout
                    continue
                
                # The img is not equal to the current state neither to the previous one
                for i in range(n_leds_test):
                    # It was supposed for the led to be turned Off but he is On
                    if isinstance(matrix_ref[sequence_state][i], OffColor) and not isinstance(vet_cor[i], OffColor):
                        log_leds.test_leds_sequence_state_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_state_sequence_error()
                        return -1
                    # It was supposed for the led to be turned On but he is Off
                    elif not isinstance(matrix_ref[sequence_state][i], OffColor) and isinstance(vet_cor[i], OffColor):
                        log_leds.test_leds_sequence_state_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_state_sequence_error()
                        return -1
                    # The colour doesn't match with the sequence
                    elif matrix_ref[sequence_state][i].get_name() != vet_cor[i].get_name():
                        log_leds.test_leds_sequence_colour_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_colour_sequence_error()
                        return -1
                else:
                    log_leds.test_leds_sequence_failed()
                    ExitCode.leds_test_not_passed()
                    return -1

                