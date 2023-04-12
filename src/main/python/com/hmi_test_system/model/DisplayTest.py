from Display import Display

class DisplayTest:
    RGB: bool          
    Pixel: bool          
    Characters: bool

    def __init__(self, display: Display):
        self.display = display
         
    
    # RGB screen detetado por CV
    def RGB_CV(self, RGB):
        self.RGB = RGB
       
    def testRGB(self):
        return self.RGB
        

    # Pixel screen detetado por CV
    def Pixel_CV(self, Pixel):
        self.Pixel = Pixel
    
    def testPixel(self):
        return self.Pixel
    

    # Characters screen detetado por CV
    def Characters_CV(self, Characters):
        self.Characters = Characters
            
    def testCharacters(self):
        return self.Characters