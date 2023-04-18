'''
Make cd to /hmi_test_system.

Then, to execute this file type

> py main_computer_vision.py

To execute a file inside a class

> py -m folder.class_name

'''

import cv2
import time

from video.image_files import ImageFiles
from video.video_file import VideoFile
from video.camera import Camera
from video.video_capture import VideoCapture

def test_image_files():
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
    print(VideoCapture.list_available_cameras())

def test_camera():
    from time import sleep
    camera = Camera()
    camera.start_capture()
    sleep(3)
    camera.stop_capture()

    frame = camera.get_image()
    i = 0

    while(frame is not None):
        cv2.imshow("cam"+str(i), frame)
        cv2.waitKey(0)
        frame = camera.get_image()
        i += 1

if (__name__ == "__main__"):
    #test_image_files()
    #test_video_file()
    #test_camera()
    #test_list_cameras()
    pass