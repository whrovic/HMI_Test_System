import cv2

class DefineModelCV():
    
    @staticmethod
    def detectPosLed(image):

        coordenadas = []

        def callback(event, x, y, flags, params):
            if(event == cv2.EVENT_LBUTTONDOWN):
                coordenadas.append(x)
                coordenadas.append(y)
                
        cv2.imshow("HMI", image)
        cv2.setMouseCallback('HMI', callback)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return coordenadas
    
    @staticmethod
    def printLed(image, coordenadas):
        for i in range(coordenadas[1]-2,coordenadas[1]+2):
            for j in range(coordenadas[0]-2,coordenadas[0]+2):
                image[i][j] = (0,0,0)

        cv2.imshow("HMI", image)
        cv2.waitKey(0)
        
image = cv2.imread("HMI.png")

coordenadas = DefineModelCV.detectPosLed(image)

print(coordenadas)

DefineModelCV.printLed(image, coordenadas)
