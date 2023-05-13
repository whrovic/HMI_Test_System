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
        
        ''' 
        Não é preciso iniciar/fechar o serial port, pq isso vai ser feito na classe SequenceTest
        O tempo do serial port e do frame vem no get_serial/get_image
        '''

        test_name = None
        test_start_time = None
        test_failed = False

        while True:

            # Get the data from the serial port
            data, data_time = serial.get_serial()
            
            # Check if the data is related to the display test
            if data is not None:
                
                # Determine which type of test is being performed
                if "Test PIX" in data:
                    test_name = "PIX"
                    test_start_time = data_time
                    print("Starting PIX Test")

                elif "Test CHR" in data:
                    test_name = "CHR"
                    test_start_time = data_time
                    print("Starting CHR Test")

                elif "Test PAL" in data:
                    test_name = "PAL"
                    test_start_time = data_time
                    print("Starting PAL Test")

                elif "CANCEL" in data:
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
                
                frame, frame_time = cam.get_image()

                ''' Faltava esta parte para ignorar imagens antigas, que não interessam '''
                # If the frame is older than the beginning of the test, ignore the frame
                if frame_time < test_start_time:
                    continue
                
                # If the test duration has elapsed, the test has passed
                elif frame_time >= test_start_time:
                    ''' 
                    Esta condição será sempre true, pq o tempo da imagem é sempre maior que o tempo de começo do teste.
                    Acho que o que querias era verificar se esta imagem é relativa ao próximo teste.
                    
                    Para fazeres isso podes, em cima, criar outras 2 variáveis, chamadas new_test_name e new_test_start_time que
                    guardam o proximo teste e caso o tempo da imagem seja superior ao tempo do proximo teste, o teste atual
                    falhou e começa o próximo teste (test_name = new_test_name, test_start_time = new_test_start_time). Nos ifs de cima,
                    ao invés de ser test_name = ..., passaria a ser new_test_name =...
                    '''
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None

                # If the data is related to a different test, the current test has failed
                elif data is not None and "TestDisplay" in data and test_name != data.split()[1]:
                    '''
                    Esta condição acho que seria a condição acima
                    '''
                    print(f"{test_name} Test Not Passed")
                    test_failed = True
                    test_name = None
                    test_start_time = None
                
                # Perform the appropriate test based on the current test type
                elif test_name == "PIX" and HMIcv.display_backlight_test(frame, display):
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None

                elif test_name == "CHR" and HMIcv.display_characters_test(frame, display):
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None

                elif test_name == "PAL" and HMIcv.display_color_pattern_test(frame, display):
                    print(f"{test_name} Test Passed")
                    test_name = None
                    test_start_time = None
        
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