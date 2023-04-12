import sys
sys.path.append('../')
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