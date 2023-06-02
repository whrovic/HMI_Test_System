import cv2
import numpy as np


class DefineModelCV():

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

        # Apply a Canny edge detection algorithm to the grayscale image
        #edges = cv2.Canny(threshold, 50, 150, apertureSize=3)

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
