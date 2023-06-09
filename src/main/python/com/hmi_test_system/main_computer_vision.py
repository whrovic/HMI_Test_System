'''
Make cd to /hmi_test_system.

Then, to execute this file type

> python main_computer_vision.py

To execute a file inside a class

> python -m folder.class_name

If py gives an error try py or python3 instead

'''

def test_image_files():
    from video.image_files import ImageFiles
    import cv2

    img1 = "test_images/char_test.png"
    img2 = "test_images/HMI.png"

    Img = ImageFiles([img1,img2])

    Img.start_capture()

    Img.stop_capture()

    cv2.imshow("img1", Img.get_image())
    cv2.waitKey(0)

    cv2.imshow("img2", Img.get_image())
    cv2.waitKey(0)

    cv2.destroyAllWindows()

def test_video_file():
    from video.video_file import VideoFile
    import time
    import cv2

    path = "Vídeo Display.MOV"

    video = VideoFile(str(path), 1)

    video.start_capture()

    time.sleep(14)

    video.stop_capture()

    frame = video.get_image()
    i = 0

    while(frame is not None):
        cv2.imshow("vid"+str(i), frame)
        cv2.waitKey(0)
        frame = video.get_image()
        i += 1

def test_list_cameras():
    from video.video_capture import VideoCapture

    print(VideoCapture.list_available_cameras())

def test_camera():
    from video.camera import Camera
    import cv2
    from time import sleep

    camera = Camera(0)
    camera.start_capture()
    
    sleep(3)

    camera.stop_capture()

    frame = camera.get_image()
    i = 0

    while(frame is not None):
        cv2.imshow("cam"+str(i+1), frame)
        cv2.waitKey(0)
        frame = camera.get_image()
        i += 1
    cv2.destroyAllWindows()

def test_read_color_pattern():

    from opencv.displaycv import Displaycv
    from opencv.define_model_cv import DefineModelCV
    from video.image_files import ImageFiles
    import cv2
    import numpy as np

    img_path = "test_images/color_pattern.png"
    cap = ImageFiles([img_path,])
    cap.start_capture()

    img = cap.get_image()

    cap.stop_capture()
    cap.clear_queue()

    x, y, w, h = DefineModelCV.detect_pos_display(img)

    lcd = img[y:y+h, x:x+w]
    lcd = cv2.resize(lcd, (680, 512))

    color_pat = np.array(Displaycv.__get_color_pattern(lcd))

    image = np.zeros((512, 680, 3))

    r_x = 40
    r_y = 16
    width = image.shape[1] // r_x
    height = image.shape[0] // r_y

    k = 0
    for i in range(r_x):
        for j in range(r_y):
            x = i * width
            y = j * height

            image[y:y+height, x:x+width] = color_pat[k]/255

            k += 1

    cv2.imshow("Original image", img)
    cv2.imshow("Reconstructed image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_char():
    from video.image_files import ImageFiles
    import numpy as np, cv2, pytesseract
    from difflib import SequenceMatcher

    # Setup tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img_path = "test_images/char_test.png"
    cap = ImageFiles([img_path,])
    cap.start_capture()

    img = cap.get_image()

    cap.stop_capture()
    cap.clear_queue()

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
    test =  '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGH\n' \
            'IJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnop\n' \
            'qrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:\n' \
            ';<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`ab\n' \
            'cdefghijklmnopqrstuvwxyz{]}~!"#$%&\'()*+,\n' \
            '-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRST\n' \
            'UVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|\n' \
            '}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEF\n' \
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

def test_find_folder():
    import os
    
    def find_folder(name):
        # Get the directory of the script file
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Go up the directory tree until the folder with the specified name is found
        while script_dir != os.path.dirname(script_dir):
            for file_or_dir in os.listdir(script_dir):
                if file_or_dir == name and os.path.isdir(os.path.join(script_dir, file_or_dir)):
                    return os.path.join(script_dir, file_or_dir)
            script_dir = os.path.dirname(script_dir)

        # Return None if the folder was not found
        return None
    
    folder_path = find_folder("HMI_Test_System")
    print(repr(folder_path))

def test_read_colours():
    from video.image_files import ImageFiles
    from opencv.define_model_cv import DefineModelCV
    from opencv.hmicv import HMIcv
    from data.model.led import Led
    from data.color.list_of_colors import ListOfColors
    import cv2

    img1 = "test_images/img_leds_1.png"

    Img = ImageFiles([img1,])

    Img.start_capture()
    Img.stop_capture()

    img = Img.get_image()

    coordinates = DefineModelCV.detect_pos_leds(img)

    for c in coordinates:
        led = Led('L1', 0, int(c[0]), int(c[1]))

        print(HMIcv.led_test(img, led).get_name())
        DefineModelCV.show_coordinates(img, [c,])

    cv2.imshow("img1", img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if (__name__ == "__main__"):
    #test_image_files()
    #test_video_file()
    #test_list_cameras()
    
    from data.path import Path
    from data.color.list_of_colors import ListOfColors
    Path()

    ListOfColors.read_from_file()
    
    #test_read_colours()

    from video.camera import Camera

    cam = Camera(0)

    cam.set_settings(None)

    pass
    