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

        print("Serial Port communication opened")

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

        # TODO: This shouldn't be defined here
        TIMEOUT = 10

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

        print("Serial Port communication opened")

        # Waits for serial port TestBootloaderInfo begin
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
                if data.startswith(TEST_BOOT_LOADER_INFO_BEGIN):
                    break
            
            sleep(0.1)

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        print("Bootloader Test started")

        # Start bootloader test
        result = Test.test_boot_loader_info(cam, serial_port, model.get_boot_loader_info().get_version(), model.get_boot_loader_info().get_date())

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_board_info(model: Model, serial_number : str, manufacture_date : str, dsp = False):
        
        # TODO: This shouldn't be defined here
        TIMEOUT = 10

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

        print("Serial Port communication opened")

        # Waits for serial port TestBoardInfo begin
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
                if data.startswith(TEST_BOARD_INFO_BEGIN):
                    break
            
            sleep(0.1)

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        print("Board Info Test started")

        # Start board info test
        result = Test.test_board_info(cam, serial_port, model.get_info().get_board(), serial_number, manufacture_date, model.get_info().get_option(), model.get_info().get_revision(), model.get_info().get_edition(), model.get_info().get_lcd_type)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_alight(dsp = False):
        
        # TODO: This shouldn't be defined here
        TIMEOUT = 10

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

        print("Serial Port communication opened")

        # Waits for serial port TestALight begin
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
                if data.startswith(TEST_ALIGHT_BEGIN):
                    break
            
            sleep(0.1)

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        print("Light Test started")

        # Start light test
        result = Test.test_alight(cam, serial_port)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_led(model: Model, leds_test = None):
        
        # TODO: This shouldn't be defined here
        TIMEOUT = 10

        # Gets the leds to test
        if leds_test is None:
            # If no led names are provided, get everyone from the model
            leds_sequence = model.get_leds()
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
        cam = SetupTest.__cam_leds
        if cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            ExitCode.camera_connection_failure()
            return -1
        
        # Start receiving data from serial port
        serial_port.start_receive()

        print("Serial Port communication opened")

        # Waits for serial port TestLeds begin
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

        print("Leds Tests started")

        # Start led test
        result = Test.test_led(cam, serial_port, leds_sequence)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_display(model: Model):
    
        # TODO: This shouldn't be defined here
        TIMEOUT = 10

        # Open the needed connections
        SetupTest.setup(False, True, True, False)

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

        print("Serial Port communication opened")

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
                if data.startswith(TEST_DISPLAY_BEGIN):
                    break
            
            sleep(0.1)

        # Start recording images
        cam.start_capture()

        print("Display Tests started")

        # Start led test
        result = Test.test_display(cam, serial_port, model.get_display())

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    def seq_all(model: Model, serial_number : str, manufacture_date : str):
        
        # TODO: This shouldn't be defined here
        TIMEOUT = 10

        # Open the needed connections
        SetupTest.setup(True, True, True, False)

        # Check connections status
        serial_port = SetupTest.__sp_main
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            ExitCode.serialport_connection_failure()
            return -1
        cam_leds = SetupTest.__cam_leds
        if cam_leds.closed():
            # Couldn't open camera connection
            SetupTest.close()
            ExitCode.camera_connection_failure()
            return -1
        cam_display = SetupTest.__cam_display
        if cam_display.closed():
            # Couldn't open camera connection
            SetupTest.close()
            ExitCode.camera_connection_failure()
            return -1
        
        # Start receiving data from serial port
        serial_port.start_receive()

        print("Serial Port communication opened")

        i = 0

        while i < 5:
            # Waits for serial port Test begin
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
                    elif data.startswith(TEST_BOOT_LOADER_INFO_BEGIN):
                        break
                    elif data.startswith(TEST_BOARD_INFO_BEGIN):
                        break
                    elif data.startswith(TEST_ALIGHT_BEGIN):
                        break
                    elif data.startswith(TEST_LEDS_BEGIN):
                        break
                    elif data.startswith(TEST_DISPLAY_BEGIN):
                        break

                sleep(0.1)
            
            # Start recording images
            cam_leds.start_capture()
            cam_display.start_capture()

            if data.startswith(TEST_BUTTONS_BEGIN):
                # Gets the buttons to test
                button_sequence = model.get_buttons()
                print("Buttons Tests started")
                # Start button test
                result = Test.test_button(cam_display, serial_port, button_sequence)

            elif data.startswith(TEST_BOOT_LOADER_INFO_BEGIN):
                print("Bootloader Test started")
                # Start bootloader test
                result = Test.test_boot_loader_info(cam_display, serial_port, model.get_boot_loader_info().get_version(), model.get_boot_loader_info().get_date())

            elif data.startswith(TEST_BOARD_INFO_BEGIN):
                print("Board Info Test started")
                # Start board info test
                result = Test.test_board_info(cam_display, serial_port, model.get_info().get_board(), serial_number, manufacture_date, model.get_info().get_option(), model.get_info().get_revision(), model.get_info().get_edition(), model.get_info().get_lcd_type)

            elif data.startswith(TEST_ALIGHT_BEGIN):
                print("Light Test started")
                # Start light test
                result = Test.test_alight(cam_display, serial_port)

            elif data.startswith(TEST_LEDS_BEGIN):
                # Gets the leds to test
                leds_sequence = model.get_leds()
                print("Leds Tests started")
                # Start led test
                result = Test.test_led(cam_leds, serial_port, leds_sequence)

            elif data.startswith(TEST_DISPLAY_BEGIN):
                print("Display Tests started")
                # Start led test
                result = Test.test_display(cam_display, serial_port, model.get_display())
            
            if result == -1:
                break

            i += 1

        SetupTest.close()
        
        # Return -1 in case of error or 0 if success
        return result