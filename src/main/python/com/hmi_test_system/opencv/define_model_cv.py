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

    '''
    Recebe uma imagem e retorna um vetor de coordenadas com todos os leds automaticamente detetados.
    Podes assumir que a imagem já vem recortada e só recebes a parte da placa dos leds
    (o recorte depois vai ter de ser feito aqui, mas ainda é preciso definir outras classes antes).
    Se for mais fácil, podes assumir que os leds estão todos ligados.

    O objetivo por agora será pesquisar soluções e tentar implementá-las.
    (Baixa prioridade)
    '''
    @staticmethod
    def detect_pos_leds(image):
        pass

    '''
    Mais tarde talvez tenhamos de alterar para inicialmente cortar a imagem para obter só a parte da placa do lcd,
    mas fica para depois.
    '''
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
            print("\nError: could not find display\n")
            return None, None, None, None
        
        # Return display position
        return x, y, w, h
    
    '''
    Recebe uma imagem e retorna um vetor de coordenadas com todos os botões automaticamente detetados.
    Assume-se que a imagem já vem recortada e só recebe a parte da placa dos leds e botões
    (o recorte depois vai ter de ser feito aqui, mas ainda é preciso definir outras classes antes).
    No futuro, talvez também seja útil ler o texto que está dentro do botão.
    '''
    @staticmethod
    def detect_pos_buttons(image):
        pass