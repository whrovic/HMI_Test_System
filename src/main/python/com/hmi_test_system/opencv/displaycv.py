import cv2, pytesseract
from data.model.display import Display

class Displaycv():
    
    @staticmethod
    def read_char(display):

        # Setup tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Convert image to grayscale
        display_gray = cv2.cvtColor(display, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        display_binary = cv2.threshold(display_gray, 140, 255, cv2.THRESH_BINARY)[1]

        # Read text on display
        text = pytesseract.image_to_string(display_binary, lang='eng')
        text = text.replace("\n\n", "\n")

        return text
    
    @staticmethod
    def get_color_pattern(display):
        # Resize display image
        display = cv2.resize(display, (680, 512))

        # Calculate the width and height of each rectangle
        width = display.shape[1] // 40
        height = display.shape[0] // 16

        # Create a list to store the colors
        color_pattern = []
        # Loop over each rectangle and extract the color
        for i in range(40):
            for j in range(16):
                # Calculate the coordinates of the rectangle
                x = i * width
                y = j * height
                # Extract the color of the rectangle by taking the average color value
                color = cv2.mean(display[y:y+height, x:x+width])
                # Add the color to the list of colors
                color_pattern.append(color)

        # Return color pattern
        return color_pattern
    
    @staticmethod
    def cut_display(image, display: Display):
        # Get display position
        x, y, w, h = display.get_pos_x(), display.get_pos_y(), display.get_dim_x(), display.get_dim_y()

        # Return display
        return image[y:y+h, x:x+w]
