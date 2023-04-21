import cv2
import numpy as np

class DefineModelCV():

    @staticmethod
    def definePosLed(image):

        print('Click in the LED and press ENTER')
        coordenadas = DefineModelCV.clickPosLed(image)
        print('Check the position and press ENTER')
        DefineModelCV.printPosLed(image, coordenadas)

        while (input('Is that the correct position? [Y/N]') != 'Y'):
            print('Click in the LED and press ENTER')
            coordenadas = DefineModelCV.clickPosLed(image)
            print('Check the position and press ENTER')
            DefineModelCV.printPosLed(image, coordenadas)

        print('Fim')

    @staticmethod
    def clickPosLed(image):

        coordenadas = [0, 0]

        def callback(event, x, y, flags, params):
            if(event == cv2.EVENT_LBUTTONDOWN):
                coordenadas[0] = x
                coordenadas[1] = y
                
        cv2.imshow("HMI", image)
        cv2.setMouseCallback("HMI", callback)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return coordenadas
    
    @staticmethod
    def printPosLed(image, coordenadas):

        part = np.copy(image)

        for i in range(coordenadas[1] - 2, coordenadas[1] + 2):
            for j in range(coordenadas[0] - 2, coordenadas[0] + 2):
                part[i][j] = (0,0,0)

        cv2.imshow("HMI", part)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def detect_pos_display(image):
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

        # Find contours
        contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        # Get LCD position
        lcd = None
        for contour in contours:
            if cv2.contourArea(contour) > 50000 and cv2.contourArea(contour) < 336700:
                x, y, w, h = cv2.boundingRect(contour)
        if not x or  not y or not w or not h:
            print("\nError: could not find LCD\n")
            return None
        
        # Return LCD position
        return x, y, w, h

if(__name__ == "__main__"):
    image = cv2.imread("HMI.png")
    coordenadas = DefineModelCV.definePosLed(image)
