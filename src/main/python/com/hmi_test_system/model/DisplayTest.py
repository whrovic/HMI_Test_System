class DisplayTest:
    def __init__(self, display):
        self.display = display
        self.RGB = 1            
        self.Pixel = 1          
        self.Characters = 1     

    # RGB screen detetado por CV
    def RGB_CV(self, RGB):
        self.RGB = RGB

    def getRGBResult(self):
        return self.RGB
       
    def testRGB(self):
        if(self.RGB == 'imagem de referência'):
            return 1
        else:
            return 0
        

    # Pixel screen detetado por CV
    def Pixel_CV(self, Pixel):
        self.Pixel = Pixel
    
    def getPixelResult(self):
        return self.Pixel

    def testPixel(self):
        if(self.Pixel == 'imagem de referência'):
            return 1
        else:
            return 0
    

    # Characters screen detetado por CV
    def Characters_CV(self, Characters):
        self.Characters = Characters

    def getCharactersResult(self):
        return self.Characters
            
    def testCharacters(self):
        if(self.Characters == 'imagem de referência'):
            return 1
        else:
            return 0