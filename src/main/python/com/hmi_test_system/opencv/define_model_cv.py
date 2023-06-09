import os
from time import sleep, time

import cv2
import numpy as np
from data.hardware_settings.camera_settings import CameraSettings
from data.hardware_settings.test_settings import TestSettings
from data.path import Path
from serial_port.constant_test import *
from serial_port.serial_port import SerialPort
from video.camera import Camera

from .displaycv import Displaycv


class DefineModelCV():

    @staticmethod
    def get_leds_image(use_parameters = False):
        # Get parameters from camera
        settings = TestSettings.get_cam_leds()
        if settings is None: return None
        
        if use_parameters:
            parameters = settings.get_parameters('leds')
            if parameters is None: return None
        else:
            parameters = settings.get_parameters('default')

        camera_id = settings.get_device_id()
        cam = Camera(camera_id)
        cam.set_settings(parameters)

        img = cam.get_frame()
        cam.close()
        return img
    
    @staticmethod
    def get_buttons_image():
        # Get parameters from camera
        settings = TestSettings.get_cam_leds()
        if settings is None: return None
        parameters = settings.get_parameters('default')

        camera_id = settings.get_device_id()
        cam = Camera(camera_id)
        cam.set_settings(parameters)

        img = cam.get_frame()
        cam.close()
        return img

    @staticmethod
    def get_display_image(use_parameters = False):

        settings = TestSettings.get_cam_display()
        if settings is None: return None
        
        if use_parameters:
            parameters = settings.get_parameters('display')
            if parameters is None: return None
        else:
            parameters = settings.get_parameters('default')

        camera_id = settings.get_device_id()
        cam = Camera(camera_id)
        cam.set_settings(parameters)

        img = cam.get_frame()
        cam.close()
        return img

    @staticmethod
    def click_pos(image):

        coordenadas = [0, 0, False]
        cv2.namedWindow("HMI")

        def callback(event, x, y, flags, params):
            if(event == cv2.EVENT_LBUTTONDOWN):
                coordenadas[0] = x
                coordenadas[1] = y
                coordenadas[2] = True

                img_aux = np.copy(image)
                img_aux[y-2:y+2, x-2:x+2] = (0,0,0)
                cv2.imshow("HMI", img_aux)

        while(not coordenadas[2]):
            cv2.imshow("HMI", image)
            cv2.setMouseCallback("HMI", callback)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return coordenadas[:2]

    @staticmethod
    def detect_pos_leds(image):
        # Creates a copy to avoid changing the original one
        img = image.copy()
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Threshold the image to separate circles from the black background
        _, threshold = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

        # Find contours in the edge image
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        led_coordinates = []
        # Iterate over the contours and fit circles to them
        for contour in contours:
            # Fit a minimum enclosing circle to the contour
            (x, y), _ = cv2.minEnclosingCircle(contour)
            led_coordinates.append((int(x), int(y)))

        # Display the image with detected circles
        DefineModelCV.show_coordinates(img, led_coordinates)

        return led_coordinates

    @staticmethod
    def detect_pos_display(image):
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

        # Find contours
        contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        # Get display position
        for contour in contours:
            if cv2.contourArea(contour) > 50000 and cv2.contourArea(contour) < 336700:
                x, y, w, h = cv2.boundingRect(contour)
        if not x or not y or not w or not h:
            print("/nError: could not find display/n")
            return None, None, None, None
        
        # Return display position
        return x, y, w, h
    
    @staticmethod
    def detect_pos_buttons(image):
        pass
    
    @staticmethod
    def write_reference_image_to_file(image, filename):
        
        # Calculate the transformation matrix
        transformation_matrix, coordinates = Displaycv.get_transformation_matrix(image)
        if transformation_matrix is None:
            return False

        # Extract display
        display_image = Displaycv.extract_display(image, transformation_matrix, coordinates)

        ret_val = cv2.imwrite(Path.get_model_images_directory() + '/' + filename + '.png', display_image)

        return ret_val

    @staticmethod
    def show_coordinates(image, coordinates):
        # Copy original image to prevent changes
        img = image.copy()
        
        # Draw circles in the coordinates
        for (x, y) in coordinates:
            print(x, y)
            cv2.circle(img, (int(x), int(y)), 4, (0, 255, 0), 8)

        # Show resulting image
        cv2.imshow("HMI", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def get_reference_display_images():

        TIMEOUT = 10
        
        # Get the display camera parameters
        # TODO: Print error
        camera_settings = TestSettings.get_cam_display()
        if camera_settings is None: return None, None
        camera_parameters = camera_settings.get_parameters('display')
        if camera_parameters is None: return None, None

        # Turn serial port on
        # TODO: Define port
        serial = SerialPort('COM4')
        # TODO: Print error
        if serial.closed(): return None, None

        # Turn display camera on
        # TODO: Define index
        cam = Camera(0)
        # TODO: Print error
        if cam.closed():
            serial.close()
            return None, None
        # Apply display camera parameters
        cam.set_settings(camera_parameters)

        # Start receiving from serial port
        serial.start_receive()

        # TODO: Print instructions to the user

        # Waits for serial port TestKeys begin
        begin_waiting_time = time()
        received_sp = False
        while True:
            now = time()

            # Check if the serial port timed out waiting for the first received data
            if (not received_sp and (now - begin_waiting_time > TIMEOUT)):
                # No data was received from the serial port
                # TODO: Print error
                cam.close()
                serial.close()
                return -1
            
            # Get data from serial port
            data, _ = serial.get_serial()

            if data is not None:
                received_sp = True
                
                data = str(data)
                if data.startswith(TEST_DISPLAY_BEGIN):
                    break
            
            sleep(0.1)

        # Start taking images of the display
        cam.start_capture()

        chr_img_list = []
        pal_img_list = []

        # Initializing the test variables
        test_name = None
        test_start_time = None
        # Variables for the next test
        new_test_name = None
        new_test_start_time = None

        # TODO: Add TIMEOUT
        while True:

            # Get the data from the serial port
            data = data_time = None
            if new_test_name != 'END':
                data, data_time = serial.get_serial()

            # Check if the data is related to the display test
            if data is not None:
                # Determine which type of test is being performed
                if CHAR in data:
                    new_test_name = CHAR
                    new_test_start_time = data_time
                elif COLOR in data:
                    new_test_name = COLOR
                    new_test_start_time = data_time
                elif TEST_DISPLAY_OK in data:
                    new_test_name = TEST_DISPLAY_OK
                    new_test_start_time = data_time

            # Start the first test
            if test_name is None and new_test_name is not None:
                test_name = new_test_name
                test_start_time = new_test_start_time
                new_test_name = None
                new_test_start_time = None
                if test_name == TEST_DISPLAY_OK:
                    break

            # If a test is currently running
            if test_name is not None:
                frame, frame_time = cam.get_image()
                if frame is None: continue

                # Check if the frame is related to the current test
                if frame_time < test_start_time:
                    continue
                elif new_test_start_time is not None and frame_time >= new_test_start_time:
                    # Start the next test
                    test_name = new_test_name
                    test_start_time = new_test_start_time
                    if test_name == TEST_DISPLAY_OK:
                        break
                else:
                    # Perform the appropriate test based on the current test type
                    if test_name == CHAR:
                        chr_img_list.append(frame)
                    elif test_name == COLOR:
                        pal_img_list.append(frame)

        cam.close()
        serial.close()

        # Choose images from the set
        chr_img = DefineModelCV.choose_img(chr_img_list)
        if chr_img is None: return None, None
        pal_img = DefineModelCV.choose_img(pal_img_list)
        if pal_img is None: return None, None

        return chr_img, pal_img

    @staticmethod
    def choose_img(img_list):
        if img_list is None or len(img_list) == 0:
            return None

        os.system('cls')
        print("If the image shown is a higher quality one than the previous choosen one, press Enter")
        print("Otherwise, press Whitespace to continue to the next one")
        print("Press 'q' to skip")

        choosen_img = img_list[0]
        for i, img in enumerate(img_list):
            image = cv2.resize(img, (640, 360))
            choosen_image = cv2.resize(choosen_img, (640, 360))
            
            cv2.imshow("Current Choosen Image", choosen_image)
            cv2.moveWindow("Current Choosen Image", 0, 0)
            if i > 0:
                cv2.destroyWindow(f"{i}/{len(img_list)}")
            cv2.namedWindow(f"{i+1}/{len(img_list)}")
            cv2.moveWindow(f"{i+1}/{len(img_list)}", 650, 0)
            cv2.imshow(f"{i+1}/{len(img_list)}", image)
            
            while True:
                key = cv2.waitKey(0)
                if key == ord('q'):
                    break
                elif key == ord(' '):
                    break
                elif key == 13:
                    choosen_img = img
                    break
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
        return choosen_img
    