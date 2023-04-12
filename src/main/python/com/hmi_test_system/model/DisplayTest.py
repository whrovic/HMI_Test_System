class DisplayTest:
    RGB: bool          
    Pixel: bool          
    Characters: bool

    def __init__(self, display):
        self.display = display
         
    
    # RGB screen detetado por CV
    def RGB_CV(self, RGB):
        self.RGB = RGB

    def getRGBResult(self):
        return self.RGB
       
    def testRGB(self):
        if(self.RGB):
            return 1
        else:
            return 0
        

    # Pixel screen detetado por CV
    def Pixel_CV(self, Pixel):
        self.Pixel = Pixel
    
    def getPixelResult(self):
        return self.Pixel

    def testPixel(self):
        if(self.Pixel):
            return 1
        else:
            return 0
    

    # Characters screen detetado por CV
    def Characters_CV(self, Characters):
        self.Characters = Characters

    def getCharactersResult(self):
        return self.Characters
            
    def testCharacters(self):
        if(self.Characters):
            return 1
        else:
            return 0