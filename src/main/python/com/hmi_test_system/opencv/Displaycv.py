import cv2, pytesseract

class Displaycv:
    
    @staticmethod
    def read_char(lcd):
        # Setup tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Convert LCD image to grayscale
        gray = cv2.cvtColor(lcd, cv2.COLOR_BGR2GRAY)

        # Convert to binary with adaptive threshold
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 37, 35)
        
        # Read characters on LCD
        char_pattern = pytesseract.image_to_string(binary, lang='eng', config='--psm 6') # psm 6 --> Assume a single uniform block of text
        if char_pattern is None:
            print("\nError: could not detect any character\n")
            return None
        
        # Remove unnecessary whitespaces and new lines
        char_pattern = char_pattern.replace(" ", "").replace("\n\n", "\n")
        
        # Return characters pattern
        return char_pattern
    
    @staticmethod
    def get_color_pattern(lcd):
        # Resize LCD image
        lcd = cv2.resize(lcd, (680, 512))

        # Calculate the width and height of each rectangle
        width = lcd.shape[1] // 40
        height = lcd.shape[0] // 16

        # Create a list to store the colors
        colors = []
        # Loop over each rectangle and extract the color
        for i in range(40):
            for j in range(16):
                # Calculate the coordinates of the rectangle
                x = i * width
                y = j * height
                # Extract the color of the rectangle by taking the average color value
                color = cv2.mean(lcd[y:y+height, x:x+width])
                # Add the color to the list of colors
                colors.append(color)

        # Return the color pattern
        return colors

    @staticmethod
    def cut_lcd(img, x, y, w, h):
        # Cut LCD
        lcd = img[y:y+h, x:x+w]
        
        # Resize LCD image
        lcd = cv2.resize(lcd, (701, 530))

        # Return LCD
        return lcd
