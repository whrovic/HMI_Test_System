from time import time

import cv2
from data.color.color import Color, OffColor
from data.model.button import Button
from data.model.led import Led
from opencv.displaycv import Displaycv
from opencv.hmicv import HMIcv
from report import *
from report.exit_code import ExitCode
from serial_port.constant_test import *
from serial_port.serial_port import SerialPort
from video.camera import Camera


class Test:

    @staticmethod
    def test_button(cam: Camera, serial: SerialPort, button_sequence: list[Button]):

        n_buttons = len(button_sequence)
        end_test_sp = False
        end_test_dsp = (cam is None)
        end_time_sp = None
        old_data_time = old_frame_time = time()
        sequence_no_sp = sequence_no_dsp = 0
        previous_button_dsp = None
        button_sequence_name = [b.get_name() for b in button_sequence]

        while True:

            if not end_test_sp:
                data, data_time = serial.get_serial()
                if data is not None:
                    old_data_time = data_time
                    data = str(data)

                    # Received Test OK before receiving all the buttons
                    if data.startswith(TEST_BUTTONS_OK):
                        if sequence_no_sp == n_buttons:
                            end_test_sp = True
                            end_time_sp = data_time
                            LogButton.button_test_serial_pass('SP')
                        else:
                            LogButton.button_test_serial_error_final('SP', button_sequence_name[sequence_no_sp])
                            ExitCode.keys_test_not_passed('SP')
                            return -1
                    elif data.startswith(TEST_BUTTONS_CANCEL):
                        LogButton.button_tests_canceled('SP')
                        ExitCode.keys_test_not_passed()
                        return -1
                    elif data.startswith(TEST_BUTTONS_PRESSED):
                        button_name = data.split()[-1]
                        if sequence_no_sp >= n_buttons:
                            LogButton.button_test_detected_button_after_end('SP', button_name)
                            ExitCode.keys_test_not_passed()
                            return -1
                        if button_name == button_sequence_name[sequence_no_sp]:
                            sequence_no_sp += 1
                            LogButton.button_test_received('SP', button_name)
                        else:
                            # Check if the button was detected consectivelly
                            if sequence_no_sp > 0 and (button_name == button_sequence_name[sequence_no_sp - 1]):
                                LogButton.button_test_detected_consecutivelly('SP', button_name, button_sequence_name[sequence_no_sp])
                                ExitCode.keys_test_key_detected_consecutivelly()
                                return -1
                            # Check if the button was detected before
                            elif button_name in button_sequence_name[:sequence_no_sp]:
                                LogButton.button_test_detected_two_times('SP', button_name, button_sequence_name[sequence_no_sp])
                                ExitCode.keys_test_key_detect_two_times()
                                return -1
                            else:
                                LogButton.button_test_sequence_failed('SP', button_name, button_sequence_name[sequence_no_sp])
                                ExitCode.keys_test_sequence_error()
                                return -1
                    elif not data.startswith(TEST_BUTTONS):
                        LogButton.button_test_unrelated_data('SP')
                        ExitCode.keys_test_not_passed()
                        return -1
                # If no data is received for the timeout, return
                elif (time() - old_data_time > TIMEOUT_SP_BUTTON_NO_CHANGE):
                    LogButton.button_test_sp_timeout('SP')
                    ExitCode.serialport_timeout_reception()
                    return -1
                
            # Test with cam
            if not end_test_dsp:
                # Read from camera until tests are finished
                frame, frame_time = cam.get_image()
                if frame is not None:
                    Displaycv.get_transformation_matrix(frame)

                    old_frame_time = frame_time
                    # Check if the time of the image is higher than the end of the tests
                    if end_time_sp is not None and frame_time > end_time_sp + TIMEOUT_DISPLAY_READING_WAITING:
                        Log.generic("Keys Test [DSP]: The serial port ended and the camera didn't")
                        ExitCode.keys_test_not_passed()
                        return -1
                    
                    text = str(HMIcv.read_characters(frame))

                    lines = text.splitlines()
                    for line in lines:
                        if line.startswith('Pressed:'):
                            line = line.replace('|', '').strip()
                            button_name = line.split()[-1]
                            if button_name not in button_sequence_name:
                                button_name = button_name.replace('l', '1')
                                if button_name not in button_sequence_name:
                                    break
                            
                            if button_name == button_sequence_name[sequence_no_dsp]:
                                LogButton.button_test_received('DSP', button_name)
                                sequence_no_dsp += 1
                                previous_button_dsp = button_name
                                if sequence_no_dsp >= n_buttons:
                                    end_test_dsp = True
                                    LogButton.button_test_serial_pass('DSP')
                            # No changes in the display
                            elif not (previous_button_dsp is not None and button_name == previous_button_dsp):
                                LogButton.button_test_sequence_failed('DSP', button_name, button_sequence_name[sequence_no_sp])
                                ExitCode.keys_test_sequence_error()
                                return -1
                            break
                # Check for timeout
                elif (time() - old_frame_time > TIMEOUT_LAST_RECEIVED_CAM):
                        Log.generic("Keys Test [DSP]: Timeout unavailable cam")
                        ExitCode.camera_timeout_stopped()
                        return -1
            
            if end_test_sp and end_test_dsp:
                LogButton.button_test_serial_pass('DSP')
                return 0

    @staticmethod
    def test_display(cam: Camera, serial: SerialPort, chr_ref_img, pal_ref_img):

        # Initializing the test variables
        test_name = test_start_time = None
        # Variables for the next test
        new_test_name = new_test_start_time = None
        old_data_time = old_frame_time = time()
        ret_value = 0

        while True:
            # Get the data from the serial port
            if new_test_name != TEST_DISPLAY_OK:
                data, data_time = serial.get_serial()
                # Check if the data is related to the display test
                if data is not None:
                    old_data_time = data_time
                    # Determine which type of test is the next one
                    if PIXEL in data:
                        new_test_name = PIXEL
                    elif CHAR in data:
                        new_test_name = CHAR
                    elif COLOR in data:
                        new_test_name = COLOR
                    elif TEST_DISPLAY_OK in data:
                        new_test_name = TEST_DISPLAY_OK
                    else:
                        new_test_name = None
                    new_test_start_time = data_time
                elif (time() - old_data_time > TIMEOUT_DISPLAY_TEST_CHANGE):
                    Log.generic("Timeout SP")
                    ExitCode.camera_timeout_stopped()
                    return -1

            # Start the first test
            if test_name is None and new_test_name is not None:
                if new_test_name == TEST_DISPLAY_OK:
                    LogDisplay.test_finished()
                    break
                else:
                    test_name, test_start_time = new_test_name, new_test_start_time
                    new_test_name, new_test_start_time = None, None
                    LogDisplay.start_test(test_name)

            # If a test is currently running
            if test_name is not None:
                frame, frame_time = cam.get_image()
                if frame is not None:
                    
                    Displaycv.get_transformation_matrix(frame)

                    old_frame_time = frame_time
                    
                    # Check if the frame is related to the current test
                    if frame_time < test_start_time:
                        continue
                    elif new_test_start_time is not None and frame_time >= new_test_start_time:
                        # Start the next test and the current one failed
                        LogDisplay.test_failed(test_name)
                        if test_name == PIXEL:
                            ExitCode.display_test_pix_not_passed()
                        elif test_name == CHAR:
                            ExitCode.display_test_chr_not_passed()
                        elif test_name == COLOR:
                            ExitCode.display_test_pal_not_passed()
                        
                        # TODO: Check if it's suposed to return here, or after all the tests end
                        ret_value = -1
                        if new_test_name == TEST_DISPLAY_OK:
                            LogDisplay.test_finished()
                            break
                        else:
                            test_name, test_start_time = new_test_name, new_test_start_time
                            new_test_name, new_test_start_time = None, None
                            if test_name is not None:
                                LogDisplay.start_test(test_name)
                    else:
                        # Perform the appropriate test based on the current test type
                        if test_name == PIXEL:
                            if HMIcv.display_backlight_test(frame):
                                LogDisplay.test_passed(test_name)
                                test_name = test_start_time = None
                            else:
                                continue
                        elif test_name == CHAR:
                            if HMIcv.display_characters_test(frame, chr_ref_img):
                                LogDisplay.test_passed(test_name)
                                test_name = test_start_time = None
                            else:
                                continue
                        elif test_name == COLOR:
                            if HMIcv.display_color_pattern_test(frame, pal_ref_img):
                                LogDisplay.test_passed(test_name)
                                test_name = test_start_time = None
                            else:
                                continue
                # Check for camera timeout
                elif (time() - old_frame_time > TIMEOUT_LAST_RECEIVED_CAM):
                    Log.generic("Cam timeout")
                    ExitCode.camera_timeout_stopped()
                    return -1

        # Return 0 if all tests passed, -1 if any test failed
        return ret_value

    @staticmethod
    def test_boot_loader_info(cam : Camera, serial : SerialPort, version, date):

        version_info = date_info = None
        version_dsp = date_dsp = None
        end_test_sp = False
        end_test_dsp = (cam is None)
        end_time_sp = None
        old_data_time = old_frame_time = time()

        while True:
            
            # Test with serial port
            if not end_test_sp:
                data, data_time = serial.get_serial()
                if data is not None:
                    old_data_time = data_time
                    data = str(data)

                    # Check the board information
                    if data.startswith(TEST_BOOT_LOADER_INFO_OK):
                        if (version_info and date_info) is None:
                            Log.generic("BootLoader Info Test [SP]: Received Test OK before the remaining information")
                            ExitCode.bootloader_test_not_passed()
                            return -1
                        else:
                            Log.generic("BBootLoader Info Test [SP]: Serial port succeeded")
                            end_test_sp = True
                            end_time_sp = data_time
                    elif version_info is None:
                        if data.startswith(TEST_BOOT_LOADER_INFO_VERSION + version):
                            version_info = version
                            Log.generic(f"BootLoader Info Test [SP]: Version {version} correctly received")
                        else:
                            Log.generic("BootLoader Info Test [SP]: Incorrect version information")
                            ExitCode.bootloader_test_not_passed()
                            return -1
                    # Check the serial number
                    elif date_info is None:
                        if data.startswith(TEST_BOOT_LOADER_INFO_DATE + date):
                            date_info = date
                            Log.generic(f"BootLoader Info Test [SP]: Date {date} correctly received")
                        else:
                            Log.generic("BootLoader Info Test [SP]: Incorrect date")
                            ExitCode.bootloader_test_not_passed()
                            return -1
                # If no info is received for the timeout, return
                elif (time() - old_data_time > TIMEOUT_ALIGHT_NO_INFO):
                    Log.generic("BootLoader Info Test [SP]: SP timeout")
                    ExitCode.serialport_timeout_reception()
                    return -1

            # Test with cam
            if not end_test_dsp:
                # Read from camera until tests are finished
                frame, frame_time = cam.get_image()
                if frame is not None:

                    Displaycv.get_transformation_matrix(frame)

                    old_frame_time = frame_time
                    # Check if the time of the image is higher than the end of the tests
                    if end_time_sp is not None and frame_time > end_time_sp + TIMEOUT_DISPLAY_READING_WAITING:
                        Log.generic("BootLoader Info Test [DSP]: The serial port ended and the camera didn't")
                        ExitCode.bootloader_test_not_passed()
                        return -1
                    
                    # Read the text from the display
                    text = str(HMIcv.read_characters(frame))

                    for line in text.splitlines():
                        info_recv = Test.split_double_dot(line)
                        if version_dsp is None and line.startswith('Version:'):
                            if Test.compare_strings(version, info_recv):
                                Log.generic(f"BootLoader Info Test [DSP]: Version {version} correctly received")
                                version_dsp = version
                        elif date_dsp is None and line.startswith('Date:'):
                            if Test.compare_strings(date, info_recv):
                                Log.generic(f"BootLoader Info Test [DSP]: Date {date} correctly received")
                                date_dsp = date
                    end_test_dsp = bool(version_dsp and date_dsp)
                    if end_test_dsp:
                        Log.generic("BootLoader Info Test [DSP]: Display succeeded")
                # Check for timeout
                elif (time() - old_frame_time > TIMEOUT_LAST_RECEIVED_CAM):
                        Log.generic("BootLoader Info Test [DSP]: Timeout unavailable cam")
                        ExitCode.camera_timeout_stopped()
                        return -1

            # Return when all the tests have succeeded
            if end_test_sp and end_test_dsp:
                Log.generic("BootLoader Info Test: Success")
                return 0

    @staticmethod
    def test_board_info(cam: Camera, serial: SerialPort, board, serial_number, manufacture_date, option, revision, edition, lcd_type):
         
        board_info = serial_number_info = manufacture_date_info = option_info = revision_info = edition_info = lcd_type_info = None
        board_dsp = serial_number_dsp = manufacture_date_dsp = option_dsp = revision_dsp = edition_dsp = lcd_type_dsp = None

        end_test_sp = False
        end_test_dsp = (cam is None)
        end_time_sp = None
        old_data_time = old_frame_time = time()

        while True:
            
            # Test with serial port
            if not end_test_sp:
                data, data_time = serial.get_serial()
                if data is not None:
                    old_data_time = data_time
                    data = str(data)

                    # Check the board information
                    if data.startswith(TEST_BOARD_INFO_OK):
                        if (board_info and serial_number_info and manufacture_date_info and option_info and revision_info and edition_info and lcd_type_info) is None:
                            Log.generic("Board Info Test: Received Test OK before the remaining information")
                            ExitCode.board_info_test_not_passed()
                            return -1
                        else:
                            Log.generic("Board Info Test: Serial port succeeded")
                            end_test_sp = True
                            end_time_sp = data_time
                    elif board_info is None:
                        if data.startswith(TEST_BOARD_INFO_BOARD + board):
                            board_info = board
                            Log.generic(f"Board Info Test [SP]: Board {board} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect board information")
                            ExitCode.board_info_test_not_passed()
                            return -1
                    # Check the serial number
                    elif serial_number_info is None:
                        if data.startswith(TEST_BOARD_INFO_SERIAL_NUMBER + serial_number):
                            serial_number_info = serial_number
                            Log.generic(f"Board Info Test [SP]: Serial number {serial_number} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect serial number")
                            ExitCode.board_info_test_not_passed()
                            return -1
                    # Check the manufacture date
                    elif manufacture_date_info is None:
                        if data.startswith(TEST_BOARD_INFO_MANUFACTURE_DATE + manufacture_date):
                            manufacture_date_info = manufacture_date
                            Log.generic(f"Board Info Test [SP]: Manufacture data {manufacture_date} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect manufacture date")
                            ExitCode.board_info_test_not_passed()
                            return -1
                    # Check the option
                    elif option_info is None:
                        if data.startswith(TEST_BOARD_INFO_OPTION + option):
                            option_info = option
                            Log.generic(f"Board Info Test [SP]: Option {option} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect option")
                            ExitCode.board_info_test_not_passed()
                            return -1
                    # Check the revision
                    elif revision_info is None:
                        if data.startswith(TEST_BOARD_INFO_REVISON + revision):
                            revision_info = revision
                            Log.generic(f"Board Info Test [SP]: Revision {revision} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect revision")
                            ExitCode.board_info_test_not_passed()
                            return -1
                    # Check the edition
                    elif edition_info is None:
                        if data.startswith(TEST_BOARD_INFO_EDITON + edition):
                            edition_info = edition
                            Log.generic(f"Board Info Test [SP]: Edition {edition} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect edition")
                            ExitCode.board_info_test_not_passed()
                            return -1
                    # Check the LCD type
                    elif lcd_type_info is None:
                        if data.startswith(TEST_BOARD_INFO_LCD_TYPE + lcd_type):
                            lcd_type_info = lcd_type
                            Log.generic(f"Board Info Test [SP]: LCD Type {lcd_type} correctly received")
                        else:
                            Log.generic("Board Info Test [SP]: Incorrect LCD type")
                            ExitCode.board_info_test_not_passed()
                            return -1
                # If no info is received for the timeout, return
                elif (time() - old_data_time > TIMEOUT_ALIGHT_NO_INFO):
                    Log.generic("Board Info Test [SP]: SP timeout")
                    ExitCode.serialport_timeout_reception()
                    return -1

            # Test with cam
            if not end_test_dsp:
                # Read from camera until tests are finished
                frame, frame_time = cam.get_image()
                if frame is not None:

                    Displaycv.get_transformation_matrix(frame)

                    old_frame_time = frame_time
                    # Check if the time of the image is higher than the end of the tests
                    if end_time_sp is not None and frame_time > end_time_sp + TIMEOUT_DISPLAY_READING_WAITING:
                        Log.generic("Board Info Test [DSP]: The serial port ended and the camera didn't")
                        ExitCode.board_info_test_not_passed()
                        return -1
                    
                    # Read the text from the display
                    text = str(HMIcv.read_characters(frame))

                    for line in text.splitlines():
                        info_recv = Test.split_double_dot(line)
                        if board_dsp is None and line.startswith('Board:'):
                            if Test.compare_strings(board, info_recv):
                                Log.generic(f"Board Info Test [DSP]: Board {board} correctly received")
                                board_dsp = board
                        elif serial_number_dsp is None and line.startswith('Serial Number:'):
                            if Test.compare_strings(serial_number, info_recv):
                                Log.generic(f"Board Info Test [DSP]: Serial number {serial_number} correctly received")
                                serial_number_dsp = serial_number
                        elif manufacture_date_dsp is None and line.startswith('Manufacture Date:'):
                            if Test.compare_strings(manufacture_date, info_recv):
                                Log.generic(f"Board Info Test [DSP]: Manufacture data {manufacture_date} correctly received")
                                manufacture_date_dsp = manufacture_date
                        elif option_dsp is None and line.startswith('Option:'):
                            if Test.compare_strings(option, info_recv):
                                Log.generic(f"Board Info Test [DSP]: Option {option} correctly received")
                                option_dsp = option
                        elif revision_dsp is None and line.startswith('Revision:'):
                            if Test.compare_strings(revision, info_recv):
                                Log.generic(f"Board Info Test [DSP]: Revision {revision} correctly received")
                                revision_dsp = revision
                        elif edition_dsp is None and line.startswith('Edition:'):
                            if Test.compare_strings(edition, info_recv):
                                Log.generic(f"Board Info Test [DSP]: Edition {edition} correctly received")
                                edition_dsp = edition
                        elif lcd_type_dsp is None and line.startswith('LCD Type:'):
                            if Test.compare_strings(lcd_type, info_recv):
                                Log.generic(f"Board Info Test [DSP]: LCD Type {lcd_type} correctly received")
                                lcd_type_dsp = lcd_type
                    end_test_dsp = bool(board_dsp and serial_number_dsp and manufacture_date_dsp and option_dsp and revision_dsp and edition_dsp and lcd_type_dsp)
                    if end_test_dsp:
                        Log.generic("Board Info Test [DSP]: Display succeeded")
                # Check for timeout
                elif (time() - old_frame_time > TIMEOUT_LAST_RECEIVED_CAM):
                        Log.generic("Board Info Test [DSP]: Timeout unavailable cam")
                        ExitCode.camera_timeout_stopped()
                        return -1

            # Return when all the tests have succeeded
            if end_test_sp and end_test_dsp:
                Log.generic("Board Info Test: Success")
                return 0

    @staticmethod
    def test_alight(cam: Camera, serial: SerialPort):
        
        alight_value_sp = covered_alight_value_sp = end_time_sp = None
        alight_value_dsp = covered_alight_value_dsp = None
        end_test_sp = False
        end_test_dsp = (cam is None)
        old_data_time = old_frame_time = time()

        while True:
            
            # Read from serial port until tests are finished
            if not end_test_sp:
                data, data_time = serial.get_serial()
                if data is not None:
                    old_data_time = data_time
                    data = str(data)

                    # When OK is received, the tests should stop
                    if data.startswith(TEST_ALIGHT_OK):
                        if (alight_value_sp and covered_alight_value_sp) is None:
                            Log.generic("Received Test OK before info")
                            ExitCode.alight_test_not_passed()
                        else:
                            Log.generic("Alight Test [SP]: Serial port succeeded")
                            end_test_sp = True
                            end_time_sp = data_time
                    # If the 1st value wasn't yet received
                    elif alight_value_sp is None:
                        # Received the alight uncovered value
                        if data.startswith(TEST_ALIGHT_ALIGHT):
                            # Extract the ALight sensor value from the received info
                            # Get last word '13669.36Lux'
                            info_words = data.split()
                            if len(info_words) == 0:
                                Log.generic("Didn't find any words")
                                ExitCode.alight_test_not_passed()
                                return -1
                            alight_info = info_words[-1]
                            # Get the index of the word 'Lux'
                            end_index = alight_info.find('Lux')
                            # The string was not found, so return
                            if end_index == -1:
                                Log.generic("Didn't find the lux sting")
                                ExitCode.alight_test_not_passed()
                                return -1

                            alight_info = alight_info[:end_index]
                            try:
                                alight_value_sp = float(alight_info)
                            except:
                                # The value isn't a float value
                                Log.generic("Didn't find any the float value")
                                ExitCode.alight_test_not_passed()
                                return -1

                            # Check if the ALight sensor value is within the expected range
                            if alight_value_sp > 1000:
                                Log.generic(f"ALight Test [SP]: Received {alight_value_sp}Lux uncovered")
                            else:
                                Log.generic(f"ALight Test [SP]: Incorrect uncovered ALight value ({alight_value_sp}Lux)")
                                ExitCode.alight_test_not_passed()
                                return -1
                        else:
                            Log.generic("The first data received wasn't related")
                            ExitCode.alight_test_not_passed()
                            return -1
                    elif covered_alight_value_sp is None:

                        if data.startswith(TEST_ALIGHT_ALIGHT):
                            # Extract the ALight sensor value from the received info
                            # Get last word (13669.36Lux)
                            info_words = data.split()
                            if len(info_words) <= 1:
                                Log.generic("Didn't find enough words")
                                ExitCode.alight_test_not_passed()
                                return -1
                            alight_info = info_words[-2]
                            # Get the index of the word 'Lux'
                            end_index = alight_info.find('Lux')
                            # The string was not found, so return
                            if end_index == -1:
                                Log.generic("Didn't find the lux sting")
                                ExitCode.alight_test_not_passed()
                                return -1
                            alight_info = alight_info[:end_index]
                            try:
                                covered_alight_value_sp = float(alight_info)
                            except:
                                # The value isn't a float value
                                Log.generic("Didn't find any the float value")
                                ExitCode.alight_test_not_passed()
                                return -1
                            
                            if covered_alight_value_sp < alight_value_sp / 2:
                                Log.generic(f"ALight Test [SP]: Received {covered_alight_value_sp}Lux covered")
                            else:
                                Log.generic(f"ALight Test [SP]: Incorrect covered ALight value {covered_alight_value_sp}")
                                ExitCode.alight_test_not_passed()
                                return -1
                        # The received data is related to the instructions
                        elif not data.startswith(TEST_ALIGHT):
                            Log.generic("The received data is not related to the current tests")
                            ExitCode.alight_test_not_passed()
                            return -1
                # If no info is received for the timeout, return
                elif (time() - old_data_time > TIMEOUT_ALIGHT_NO_INFO):
                    Log.generic("SP timeout")
                    ExitCode.serialport_timeout_reception()
                    return -1

            # Test with camera
            if not end_test_dsp:
                # Read from camera until tests are finished
                frame, frame_time = cam.get_image()
                if frame is not None:

                    Displaycv.get_transformation_matrix(frame)

                    old_frame_time = frame_time
                    # The time of the image is higher than the end of the tests
                    if end_time_sp is not None and frame_time > end_time_sp + TIMEOUT_DISPLAY_READING_WAITING:
                        Log.generic("The serial port ended and the camera didn't")
                        ExitCode.alight_test_not_passed()
                        return -1
                    
                    # Read the text from the display
                    text = str(HMIcv.read_characters(frame))

                    # Extract the lines from the text
                    for line in text.splitlines():
                        if 'ALight' in line:
                            # Covered value
                            if covered_alight_value_dsp is None and '(Covered)' in line and covered_alight_value_sp is not None:
                                # Extract the ALight sensor value from the received info
                                # Get last word (13669.36Lux)
                                info_words = line.split()
                                if len(info_words) > 1:
                                    alight_info = ''.join(info_words[1:]).replace(' ', '')
                                    c_index = alight_info.find('(Covered)')
                                    alight_info = alight_info[:c_index]
                                    # Get the index of the word 'Lux'
                                    end_index = alight_info.find('Lux')
                                    # The string was not found, so return
                                    if end_index != -1:
                                        alight_info = alight_info[:end_index]
                                        try:
                                            covered_alight_value_dsp = float(alight_info)
                                            if covered_alight_value_dsp < alight_value_dsp / 2:
                                                Log.generic(f"ALight Test [DSP]: Received {covered_alight_value_dsp}Lux covered")
                                            else:
                                                Log.generic(f"ALight Test [DSP]: Incorrect covered ALight value ({covered_alight_value_dsp}Lux)")
                                                ExitCode.alight_test_not_passed()
                                                return -1
                                        except:
                                            pass    
                            # Uncovered value
                            elif alight_value_dsp is None and 'Covered' not in line and alight_value_sp is not None:
                                # Extract the ALight sensor value from the received info
                                # Get last word '13669.36Lux'
                                info_words = line.split()
                                if len(info_words) > 0:
                                    alight_info = ''.join(info_words[1:]).replace(' ', '')
                                    # Get the index of the word 'Lux'
                                    end_index = alight_info.find('Lux')
                                    if end_index != -1:
                                        alight_info = alight_info[:end_index]
                                        try:
                                            alight_value_dsp = float(alight_info)
                                            # Check if the ALight sensor value is within the expected range
                                            if alight_value_dsp > 1000:
                                                Log.generic(f"ALight Test [DSP]: Received {alight_value_dsp}Lux uncovered")
                                            else:
                                                print(alight_value_dsp)
                                                Log.generic(f"ALight Test [DSP]: Incorrect uncovered ALight value ({alight_value_dsp}Lux)")
                                                ExitCode.alight_test_not_passed()
                                                return -1
                                        except:
                                            pass
                        
                    end_test_dsp = bool(alight_value_dsp and covered_alight_value_dsp)
                    if end_test_dsp:
                        Log.generic("Alight dsp test passed")
                # Check for camera timeout
                elif (time() - old_frame_time > TIMEOUT_LAST_RECEIVED_CAM):
                    Log.generic("Timeout unavailable cam")
                    ExitCode.camera_timeout_stopped()
                    return -1

            if end_test_dsp and end_test_sp:
                Log.generic("Alight tests passed")
                return 0
    
    @staticmethod
    def test_led(cam: Camera, serial: SerialPort, leds_test: list[Led]):

        # TODO: Check all the logs and make them more informative (which leds failed and at which step)

        # Number of leds
        n_leds_test = len(leds_test)
        # Total number of colours of all the leds
        total_n_colours = sum([l.get_n_Colour() for l in leds_test])
        # Saves the current state of the leds
        vet_cor: list[Color] = [OffColor()] * n_leds_test
        # Saves the old state of the leds
        old_vet_cor: list[Color] = vet_cor.copy()
        # Saves the expected sequence of colours in each led
        matrix_ref: list[list[Color]] = [[OffColor()] * n_leds_test] * total_n_colours

        matrix_ref = []
        for i in range(total_n_colours):
            matrix_ref.append([])
            for j in range(n_leds_test):
                matrix_ref[i].append(OffColor())

        pos = 0
        for i in range(n_leds_test):
            colours = leds_test[i].get_colours()
            for j in range(len(colours)):
                matrix_ref[pos][i] = colours[j]
                pos += 1

        # Stores the time arrival of the image
        cur_img_time = None
        # Stores the time arrival of the previous image
        old_img_time = time()
        # Stores the data and the time from the serialport
        serial_data = serial_data_time = None

        # Current state of the FSM
        state = 0
        sequence_state = 0
        entry_state_img_time = old_img_time

        while True:

            # Read new image and call test of colors
            img, cur_img_time = cam.get_image()
            if img is None:
                if (time() - old_img_time > TIMEOUT_LAST_RECEIVED_CAM):
                    LogLeds.test_leds_timeout()
                    ExitCode.camera_timeout_stopped()
                    return -1
                else:
                    continue
            else:
                old_img_time = cur_img_time
            
            old_vet_cor = vet_cor.copy()
            for i in range(n_leds_test):
                vet_cor[i] = HMIcv.led_test(img, leds_test[i])

            # Read from serial port
            if serial_data is None:
                serial_data, serial_data_time = serial.get_serial()
            
            # Check for the end of the tests
            if sequence_state >= total_n_colours:
                LogLeds.test_leds_sequence_passed()
                LogLeds.test_leds_finished()
                return 0
            elif (serial_data == TEST_LEDS_OK) and (serial_data_time <= cur_img_time):
                LogLeds.test_leds_finished()
                LogLeds.test_leds_sequence_not_completed()
                ExitCode.leds_test_not_passed()
                return 0
            
            # Test All Leds ON
            if state == 0:
                
                # If at least one of the leds are turned off, return
                for i in range(n_leds_test):
                    if isinstance(vet_cor[i], OffColor):
                        LogLeds.test_failed(leds_test[i].get_name())
                        ExitCode.leds_test_not_turn_all_on()
                        return -1
                # All leds are turned on
                LogLeds.test_leds_on_passed()
                state = 1
                entry_state_img_time = cur_img_time
            # Test All Leds OFF
            elif state == 1:
                
                # Counts the number of leds turned off
                n_off = 0
                for i in range(n_leds_test):
                    if isinstance(vet_cor[i], OffColor):
                        n_off += 1
                    else:
                        # If one of the leds was turned off and now is turned on
                        if isinstance(old_vet_cor[i], OffColor):
                            LogLeds.test_failed_off()
                            ExitCode.leds_test_not_turn_all_off()
                            return -1
                
                # If all the leds are off procceed to the next state
                if n_off == n_leds_test:
                    LogLeds.test_leds_off_passed()
                    state = 2
                    entry_state_img_time = cur_img_time
                # If the leds still are all turned on and it didn't timed out, ignore this image and retry
                elif n_off == 0:
                    if (cur_img_time - entry_state_img_time > TIMEOUT_LEDS_START_TURNING_OFF):
                        print("None turned off")
                        LogLeds.test_failed_off()
                        ExitCode.leds_test_not_turn_all_off()
                        return -1
                    else:
                        continue
                # If at least one led is still on
                else:
                    # If in the previous step, all the leds were off and now at least one is on
                    # Then it means that the leds are starting turning off
                    # If they are turning off and one of them turns on again, the statment above retuns
                    # Otherwise, only if it times out when the leds are turning on, it happens
                    old_n_off = 0
                    for i in range(n_leds_test):
                        if isinstance(old_vet_cor[i], OffColor):
                            old_n_off += 1
                            break
                    if old_n_off == 0:
                        entry_state_img_time = cur_img_time
                    elif (cur_img_time - entry_state_img_time > TIMEOUT_LEDS_TURNING):
                        LogLeds.test_failed_off()
                        ExitCode.leds_test_not_turn_all_off()
                        return -1
            # Test All Leds ON
            elif state == 2:
                
                n_on = 0
                for i in range(n_leds_test):
                    if not isinstance(vet_cor[i], OffColor):
                        n_on += 1
                    else:
                        # If one of the leds was turned on and now is turned off
                        if not isinstance(old_vet_cor[i], OffColor):
                            LogLeds.test_failed_on()
                            ExitCode.leds_test_not_turn_all_on()
                            return -1
                
                # If all the leds are on procceed to the next state
                if n_on == n_leds_test:
                    LogLeds.test_leds_on_passed()
                    state = 3
                    entry_state_img_time = cur_img_time
                # If all the leds still are turned off and didn't timed out, proceed
                elif n_on == 0:
                    if (cur_img_time - entry_state_img_time > TIMEOUT_LEDS_START_TURNING_ON):
                        print("None turned off")
                        LogLeds.test_failed_on()
                        ExitCode.leds_test_not_turn_all_on()
                        return -1
                    else:
                        continue
                # If at least one led failed, return
                else:
                    # Same logic as above
                    old_n_on = 0
                    for i in range(n_leds_test):
                        if not isinstance(old_vet_cor[i], OffColor):
                            old_n_on += 1
                            break
                    if old_n_on == 0:
                        # Started turning on
                        entry_state_img_time = cur_img_time
                    elif (cur_img_time - entry_state_img_time > TIMEOUT_LEDS_TURNING):
                        LogLeds.test_failed_on()
                        ExitCode.leds_test_not_turn_all_on()
                        return -1
            # LEDS Off
            elif state == 3:
                
                # Counts the number of leds turned off
                n_off = 0
                for i in range(n_leds_test):
                    if isinstance(vet_cor[i], OffColor):
                        n_off += 1
                    else:
                        # If one of the leds was turned off and now is turned on
                        if isinstance(old_vet_cor[i], OffColor):
                            LogLeds.test_failed_off()
                            ExitCode.leds_test_not_turn_all_off()
                            return -1
                
                # If all the leds are off procceed to the next state
                if n_off == n_leds_test:
                    LogLeds.test_leds_off_passed()
                    state = 4
                    entry_state_img_time = cur_img_time
                # If the leds still are all turned on and it didn't timed out, ignore this image and retry
                elif n_off == 0:
                    if (cur_img_time - entry_state_img_time > TIMEOUT_LEDS_START_TURNING_OFF):
                        print("None turned off")
                        LogLeds.test_failed_off()
                        ExitCode.leds_test_not_turn_all_off()
                        return -1
                    else:
                        continue
            # Test the Sequence
            elif state == 4:

                # Check the current state with the reference state
                for i in range(n_leds_test):
                    if vet_cor[i].get_name() != matrix_ref[sequence_state][i].get_name():
                        break
                else:
                    # The current img matches the current state, so procceed to the next one
                    #LogLeds.test_leds_detected(leds_test[sequence_state//2].get_name(), vet_cor[sequence_state//2].get_name())
                    sequence_state += 1
                    entry_state_img_time = cur_img_time
                    continue

                # The current state is diferent from the expected one

                # Check the current state with the previous state
                for i in range(n_leds_test):
                    if vet_cor[i].get_name() != old_vet_cor[i].get_name():
                        break
                else:
                    # The current state is still equal to the previous state
                    if (cur_img_time - entry_state_img_time > TIMEOUT_LEDS_SEQUENCE_CHANGE):
                        LogLeds.test_leds_sequence_state_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_no_changes_timeout()
                        return -1
                    else:
                        continue

                for i in range(n_leds_test):
                    if not isinstance(vet_cor[i], OffColor):
                        break
                else:
                    # TODO: Add timeout
                    continue
                
                # The current state is different from the expected one and the previous one, so a error happens
                for i in range(n_leds_test):
                    # It was supposed for the led to be turned Off but he is On
                    if isinstance(matrix_ref[sequence_state][i], OffColor) and not isinstance(vet_cor[i], OffColor):
                        LogLeds.test_leds_sequence_state_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_state_sequence_error()
                        return -1
                    # It was supposed for the led to be turned On but he is Off
                    elif not isinstance(matrix_ref[sequence_state][i], OffColor) and isinstance(vet_cor[i], OffColor):
                        LogLeds.test_leds_sequence_state_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_state_sequence_error()
                        return -1
                    # The colour doesn't match with the sequence
                    elif matrix_ref[sequence_state][i].get_name() != vet_cor[i].get_name():
                        LogLeds.test_leds_sequence_colour_failed(leds_test[i].get_name(), matrix_ref[sequence_state][i].get_name(),
                                                                    vet_cor[i].get_name())
                        ExitCode.leds_test_colour_sequence_error()
                        return -1
                else:
                    # Unknown error
                    LogLeds.test_leds_sequence_failed()
                    ExitCode.leds_test_not_passed()
                    return -1

    @staticmethod
    def compare_strings(orig, string):
        if len(orig) == len(string):
            diff_ind = [i for i in range(len(orig)) if orig[i] != string[i]]
            for i in diff_ind:
                if orig[i] == '0' or orig[i] == 'O':
                    if orig[i] == '0' and string[i] != 'O':
                        return False
                    elif orig[i] == 'O' and string[i] != '0':
                        return False
                else:
                    return False
            return True
        else:
            return False
        
    @staticmethod
    def split_double_dot(string: str):
        splited = string.split(':')
        if len(splited) != 2:
            return ''
        else:
            return splited[1].strip()
    