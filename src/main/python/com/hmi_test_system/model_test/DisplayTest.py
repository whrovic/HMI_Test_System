import sys
sys.path.append('../')
from data.Display import Display

class DisplayTest:
    RGB: bool          
    pixel: bool          
    characters: bool

    def __init__(self, display: Display):
        self.display = display
         
    
    # RGB screen detetado por CV
    def RGB_CV(self, RGB):
        self.RGB = RGB
       
    def test_RGB(self):
        return self.RGB
        

    # Pixel screen detetado por CV
    def pixel_CV(self, pixel):
        self.pixel = pixel
    
    def test_pixel(self):
        return self.pixel
    

    # Characters screen detetado por CV
    def characters_CV(self, characters):
        self.characters = characters
            
    def test_characters(self):
        return self.characters