from time import sleep, time

from data.hardware_settings.test_settings import TestSettings
from data.model.model import Model
from opencv.hmicv import HMIcv
from report import *
from serial_port.constant_test import *
from serial_port.serial_port import SerialPort

from .setup_test import SetupTest
from .test import Test


class SequenceTest:

    #Log_sequencetest =
    @staticmethod
    def seq_button(model: Model, buttons_test = None, dsp = False):

        # Get camera parameters if needed
        if dsp:
            parameters = SequenceTest._get_display_camera_parameters('display')
            if parameters is None:
                # TODO: Log this
                print("Parameters is None")
                # TODO: Error Code
                return -1

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
                    # TODO: Log this
                    print("Button not found")
                    ExitCode.key_name_not_found()
                    return -1
                # Add the button to the sequence
                button_sequence.append(button)

        # Open the needed connections
        SetupTest.setup(False, dsp, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            LogButton.serial_port_connected()

        cam = SetupTest.get_cam_display()
        if dsp and cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Cam closed")
            ExitCode.camera_connection_failure()
            return -1
        if dsp:
            cam.set_settings(parameters)
            LogButton.display_camera_connected()
        
        # Start receiving data from serial port
        serial_port.start_receive()
        # Wait for button tests to begin
        if SequenceTest.wait_start_test(serial_port, TEST_BUTTONS_BEGIN) == -1:
            # TODO: Log this
            print("Timeout tests didn't start")
            # TODO: Error code
            return -1

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        # TODO: Log this
        print("Buttons Tests started")

        # Start button test
        result = Test.test_button(cam, serial_port, button_sequence)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_board_info(model: Model, serial_number : str, manufacture_date : str, dsp = False):

        # Get camera parameters if needed
        if dsp:
            parameters = SequenceTest._get_display_camera_parameters('display')
            if parameters is None:
                # TODO: Log this
                print("Parameters is None")
                # TODO: Error Code
                return -1

        # Open the needed connections
        SetupTest.setup(False, dsp, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            Log.serial_port_connected()

        cam = SetupTest.get_cam_display()
        if dsp and cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Cam closed")
            ExitCode.camera_connection_failure()
            return -1
        if dsp:
            cam.set_settings(parameters)
            Log.display_camera_connected()
        
        # Start receiving data from serial port
        serial_port.start_receive()

        # Waits for serial port TestBoardInfo begin
        if SequenceTest.wait_start_test(serial_port, TEST_BOARD_INFO_BEGIN) == -1:
            # TODO: Log this
            print("Timeout tests didn't start")
            # TODO: Error code
            return -1

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        # TODO: Log this
        print("Board Info Test started")

        # Start board info test
        result = Test.test_board_info(cam, serial_port, model.get_info().get_board(), serial_number, manufacture_date, model.get_info().get_option(), model.get_info().get_revision(), model.get_info().get_edition(), model.get_info().get_lcd_type)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_boot_loader_info(model: Model, dsp = False):

        # Get camera parameters if needed
        if dsp:
            parameters = SequenceTest._get_display_camera_parameters('display')
            if parameters is None:
                # TODO: Log this
                print("Parameters is None")
                # TODO: Error Code
                return -1

        # Open the needed connections
        SetupTest.setup(False, dsp, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            Log.serial_port_connected()

        cam = SetupTest.get_cam_display()
        if dsp and cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Cam closed")
            ExitCode.camera_connection_failure()
            return -1
        if dsp:
            cam.set_settings(parameters)
            Log.display_camera_connected()
        
        # Start receiving data from serial port
        serial_port.start_receive()
        # Waits for serial port TestBootloaderInfo begin
        if SequenceTest.wait_start_test(serial_port, TEST_BOOT_LOADER_INFO_BEGIN) == -1:
            # TODO: Log this
            print("Timeout tests didn't start")
            # TODO: Error code
            return -1

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        # TODO: Log this
        print("Bootloader Test started")

        # Start bootloader test
        result = Test.test_boot_loader_info(cam, serial_port, model.get_boot_loader_info().get_version(), model.get_boot_loader_info().get_date())

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_alight(dsp = False):

        # Get camera parameters if needed
        if dsp:
            parameters = SequenceTest._get_display_camera_parameters('display')
            if parameters is None:
                # TODO: Log this
                print("Parameters is None")
                # TODO: Error Code
                return -1

        # Open the needed connections
        SetupTest.setup(False, dsp, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            Log.serial_port_connected()

        cam = SetupTest.get_cam_display()
        if dsp and cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Cam closed")
            ExitCode.camera_connection_failure()
            return -1
        if dsp:
            cam.set_settings(parameters)
            Log.display_camera_connected()
        
        # Start receiving data from serial port
        serial_port.start_receive()
        # Waits for serial port TestALight begin
        if SequenceTest.wait_start_test(serial_port, TEST_ALIGHT_BEGIN) == -1:
            # TODO: Log this
            print("Timeout tests didn't start")
            # TODO: Error code
            return -1

        # If the test will use both serial port and display, start recording images
        if dsp:
            cam.start_capture()

        # TODO: Log this
        print("Light Test started")

        # Start light test
        result = Test.test_alight(cam, serial_port)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_led(model: Model, leds_test = None):

        # Get camera parameters
        parameters = SequenceTest._get_leds_camera_parameters('leds')
        if parameters is None:
            # TODO: Log this
            print("Parameters is None")
            # TODO: Error Code
            return -1

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
                    # TODO: Log this
                    print("Led name not found")
                    ExitCode.key_name_not_found()
                    return -1
                # Add the led to the sequence
                leds_sequence.append(led)

        # Open the needed connections
        SetupTest.setup(True, False, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            Log.serial_port_connected()

        cam = SetupTest.get_cam_leds()
        if cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Cam closed")
            ExitCode.camera_connection_failure()
            return -1
        else:
            cam.set_settings(parameters)
            Log.leds_camera_connected()       

        # Start receiving data from serial port
        serial_port.start_receive()
        # Waits for serial port TestLeds begin
        if SequenceTest.wait_start_test(serial_port, TEST_LEDS_BEGIN) == -1:
            # TODO: Log this
            print("Timeout tests didn't start")
            # TODO: Error code
            return -1

        # Start recording images
        cam.start_capture()

        # TODO: Log this
        print("Leds Tests started")

        # Start led test
        result = Test.test_led(cam, serial_port, leds_sequence)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_display(model: Model):

        # Get camera parameters if needed
        parameters = SequenceTest._get_display_camera_parameters('display')
        if parameters is None:
            # TODO: Log this
            print("Parameters is None")
            # TODO: Error Code
            return -1

        # Get reference images from local files
        chr_ref_img, pal_ref_img = HMIcv.read_ref_images_from_file(model.get_name())
        if chr_ref_img is None or pal_ref_img is None:
            # TODO: Log this
            print("Images Ref is None")
            # TODO: Error code
            return -1

        # Open the needed connections
        SetupTest.setup(False, True, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            Log.serial_port_connected()
        
        cam = SetupTest.get_cam_display()
        if cam.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Cam closed")
            ExitCode.camera_connection_failure()
            return -1
        else:
            cam.set_settings(parameters)
            Log.display_camera_connected()
        
        # Start receiving data from serial port
        serial_port.start_receive()
        # Waits for serial port DisplayTest begin
        if SequenceTest.wait_start_test(serial_port, TEST_DISPLAY_BEGIN) == -1:
            # TODO: Log this
            print("Timeout tests didn't start")
            # TODO: Error code
            return -1
        
        # Start recording images
        cam.start_capture()

        # TODO: Log this
        print("Display Tests started")

        # Start led test
        result = Test.test_display(cam, serial_port, chr_ref_img, pal_ref_img)

        # Close all the opened connections
        SetupTest.close()

        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def seq_all(model: Model, serial_number : str, manufacture_date : str):
        # TODO: add option of sp only

        # Get leds camera parameters
        led_parameters = SequenceTest._get_leds_camera_parameters('leds')
        if led_parameters is None:
            # TODO: Log this
            print("Parameters is None")
            # TODO: Error Code
            return -1
        # Get display camera parameters
        dsp_parameters = SequenceTest._get_display_camera_parameters('display')
        if dsp_parameters is None:
            # TODO: Log this
            print("Parameters is None")
            # TODO: Error Code
            return -1
        # Get reference images from local files
        chr_ref_img, pal_ref_img = HMIcv.read_ref_images_from_file(model.get_name())
        if chr_ref_img is None or pal_ref_img is None:
            # TODO: Log this
            print("Ref imgs is None")
            # TODO: Error code
            return -1

        # Open the needed connections
        SetupTest.setup(True, True, True, False)

        # Check connections status
        serial_port = SetupTest.get_sp_main()
        if serial_port.closed():
            # Couldn't open serial port connection
            SetupTest.close()
            # TODO: Log this
            print("SP closed")
            ExitCode.serialport_connection_failure()
            return -1
        else:
            Log.serial_port_connected()
        
        cam_leds = SetupTest.get_cam_leds()
        if cam_leds.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Leds cam closed")
            ExitCode.camera_connection_failure()
            return -1
        else:
            cam_leds.set_settings(led_parameters)
            Log.leds_camera_connected()

        cam_display = SetupTest.get_cam_display()
        if cam_display.closed():
            # Couldn't open camera connection
            SetupTest.close()
            # TODO: Log this
            print("Dsp cam closed")
            ExitCode.camera_connection_failure()
            return -1
        else:
            cam_display.set_settings(dsp_parameters)
            Log.display_camera_connected()
        
        # Start receiving data from serial port
        serial_port.start_receive()

        i = 0
        while i < 5:
            # Waits for serial port Test begin
            begin_waiting_time = time()
            received_sp = False
            while True:
                # Check if the serial port timed out waiting for the first received data
                if (not received_sp and (time() - begin_waiting_time > TIMEOUT_SP_BEGIN)):
                    # No data was received from the serial port
                    SetupTest.close()
                    # TODO: Log this
                    print("Timeout never received anything in sp")
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
                # TODO: Log this
                print("Buttons Tests started")
                # Start button test
                result = Test.test_button(cam_display, serial_port, button_sequence)
            elif data.startswith(TEST_BOOT_LOADER_INFO_BEGIN):
                # TODO: Log this
                print("Bootloader Test started")
                # Start bootloader test
                result = Test.test_boot_loader_info(cam_display, serial_port, model.get_boot_loader_info().get_version(), model.get_boot_loader_info().get_date())
            elif data.startswith(TEST_BOARD_INFO_BEGIN):
                # TODO: Log this
                print("Board Info Test started")
                # Start board info test
                result = Test.test_board_info(cam_display, serial_port, model.get_info().get_board(), serial_number, manufacture_date, model.get_info().get_option(), model.get_info().get_revision(), model.get_info().get_edition(), model.get_info().get_lcd_type)
            elif data.startswith(TEST_ALIGHT_BEGIN):
                # TODO: Log this
                print("Light Test started")
                # Start light test
                result = Test.test_alight(cam_display, serial_port)
            elif data.startswith(TEST_LEDS_BEGIN):
                # Gets the leds to test
                leds_sequence = model.get_leds()
                # TODO: Log this
                print("Leds Tests started")
                # Start led test
                result = Test.test_led(cam_leds, serial_port, leds_sequence)
            elif data.startswith(TEST_DISPLAY_BEGIN):
                # TODO: Log this
                print("Display Tests started")
                # Start led test
                result = Test.test_display(cam_display, serial_port, chr_ref_img, pal_ref_img)
            if result == -1:
                break

            i += 1

        SetupTest.close()
        
        # Return -1 in case of error or 0 if success
        return result
    
    @staticmethod
    def _get_display_camera_parameters(position):
        settings = TestSettings.get_cam_display()
        if settings is None:
            return None
        parameters = settings.get_parameters(position)
        if parameters is None:
            return None
        return parameters

    @staticmethod
    def _get_leds_camera_parameters(position):
        settings = TestSettings.get_cam_leds()
        if settings is None:
            return None
        parameters = settings.get_parameters(position)
        if parameters is None:
            return None
        return parameters
    
    @staticmethod
    def wait_start_test(serial_port: SerialPort, TEST_BEGIN):
        # Waits for serial port TestKeys begin
        begin_waiting_time = time()
        received_sp = False
        while True:
            # Check if the serial port timed out waiting for the first received data
            if (not received_sp and (time() - begin_waiting_time > TIMEOUT_SP_BEGIN)):
                # No data was received from the serial port
                SetupTest.close()
                # TODO: Log this
                ExitCode.serialport_timeout_reception()
                return -1
            
            # Get data from serial port
            data, _ = serial_port.get_serial()

            if data is not None:
                received_sp = True
                
                data = str(data)
                if data.startswith(TEST_BEGIN):
                    return 0
            
            sleep(0.1)
    