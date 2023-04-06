import numpy as np, cv2, pytesseract
from difflib import SequenceMatcher

# Setup tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# input = 'HMI.png'
input = 'char_test.png'

# Load the input image
img = cv2.imread(input)
if img.size == 0:
   print("\nError: unable to read image\n")
   exit()

# Undistort image
# img = cv2.undistort(img_dist, mtx, dist, None)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary (LCD detection)
binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

# Find contours
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

# Convert to binary (text detection)
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 37, 35)

# Detect LCD
lcd = None
for contour in contours:
    if cv2.contourArea(contour) > 50000 and cv2.contourArea(contour) < 336700:
        x, y, w, h = cv2.boundingRect(contour)
        lcd = binary[y:y+h, x:x+w]
if lcd is None:
    print("\nError: could not find LCD\n")
    exit()

# Resize LCD image if necessary
if lcd.shape[1] < 600 or lcd.shape[0] < 450:
    lcd = cv2.resize(lcd, (lcd.shape[1]*2, lcd.shape[0]*2))

# Read characters on LCD
lcd_text = pytesseract.image_to_string(lcd, lang='eng', config='--psm 6') # psm 6 --> Assume a single uniform block of text
if lcd_text is None:
    print("\nError: could not detect any characters\n")
    exit()
else:
    lcd_text = lcd_text.replace(" ", "").replace("\n\n", "\n")
    print(lcd_text)

# Validation
test = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGH\n' \
        'IJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnop\n' \
        'qrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:\n' \
        ';<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`ab\n' \
        'cdefghijklmnopqrstuvwxyz{]}~!"#$%&\'()*+,\n' \
        '-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRST\n' \
        'UVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}\n' \
        '~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEF\n' \
        'GHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmn\n' \
        'opqrstuvwxyz{|}~!"#$%&\'()*+,-./012345678\n' \
        '9:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^-`\n' \
        'abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*\n' \
        '+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQR\n' \
        'STUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz\n' \
        '{|}~!"#S%&\'()*+,-./0123456789:;<=>?@ABCD\n' \
        'EFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijkl\n'
similarity = SequenceMatcher(None, lcd_text, test).ratio()
percentage = round(similarity * 100, 2)
print("\n", percentage, "%\n") # Best result: 91.42%

# Show LCD image
cv2.imshow('LCD', lcd)
cv2.waitKey(0)
cv2.destroyAllWindows()
