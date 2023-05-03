import cv2
import numpy as np

class DefineModelCV():

    '''
    (Ricardo)

    Se conseguires fazer com que não seja preciso o user carregar no ENTER top.
    Mais tarde vamos ter de alterar um pouco, para mostrar ao user só a placa dos leds
    e não a imagem toda, mas isso fica para depois.
    '''
    @staticmethod
    def select_pos_led(image):

        print('Click in the LED and press ENTER')
        coordenadas = DefineModelCV.click_pos_led(image)
        print('Check the position and press ENTER')
        DefineModelCV.print_pos_led(image, coordenadas)

        while (input('Is that the correct position? [Y/N]') != 'Y'):
            print('Click in the LED and press ENTER')
            coordenadas = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, coordenadas)

        print('Fim')

    '''
    (Ricardo)

    É fazer a mesma coisa do de cima, mas para o display. O user carrega no ponto inicial e no final
    e retornas as coordenadas iniciais e as dimensões do display (x, y, largura, altura).
    Tenta aproveitar as funções que já criaste.
    (Alta prioridade)
    '''
    @staticmethod
    def select_pos_display(image):
        pass

    '''
    (Ricardo)

    É igual literalmente igual ao dos leds
    '''
    @staticmethod
    def select_pos_button(image):
        pass

    '''
    (Ricardo)

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
    (Pedro)

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

    '''
    (Ricardo)
    '''
    @staticmethod
    def print_pos_led(image, coordenadas):

        part = np.copy(image)

        for i in range(coordenadas[1] - 2, coordenadas[1] + 2):
            for j in range(coordenadas[0] - 2, coordenadas[0] + 2):
                part[i][j] = (0,0,0)

        cv2.imshow("HMI", part)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    '''
    (Ricardo)
    '''
    @staticmethod
    def click_pos_led(image):

        coordenadas = [0, 0]
        cv2.namedWindow("HMI")

        def callback(event, x, y, flags, params):
            if(event == cv2.EVENT_LBUTTONDOWN):
                coordenadas[0] = x
                coordenadas[1] = y

                img_aux = np.copy(image)
                img_aux[y-2:y+2, x-2:x+2] = (0,0,0)
                cv2.imshow("HMI", img_aux)

        cv2.imshow("HMI", image)
        cv2.setMouseCallback("HMI", callback)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return coordenadas

if(__name__ == "__main__"):
    image = cv2.imread("HMI.png")
    coordenadas = DefineModelCV.select_pos_led(image)
