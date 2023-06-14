import cv2
from time import sleep

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Default all the camara parameters
# Enable auto focus
print(cam.set(cv2.CAP_PROP_AUTOFOCUS, 1.0))
# Enable auto exposure
print(cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1.0))
# Enable auto white balance
print(cam.set(cv2.CAP_PROP_AUTO_WB, 1.0))
# Default Brightness
print(cam.set(cv2.CAP_PROP_BRIGHTNESS, 128))
# Default Contrast
print(cam.set(cv2.CAP_PROP_CONTRAST, 32))
# Default Saturation
print(cam.set(cv2.CAP_PROP_SATURATION, 32))
# Default Sharpness
print(cam.set(cv2.CAP_PROP_SHARPNESS, 22))

# Take a picture and show
cam.release()
cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

_, img = cam.read()

cv2.imshow("Original Image", img)

cam.release()
cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

print("n")

# Changes parameters for the display settings

# Disable auto focus
print(cam.set(cv2.CAP_PROP_AUTOFOCUS, 0))
# Set manually focus [0:255, step=5]
print(cam.set(cv2.CAP_PROP_FOCUS, 102))
# Disable auto exposure
print(cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0))
# Set manually exposure
print(cam.set(cv2.CAP_PROP_EXPOSURE, -11))
# Set manually exposure gain
print(cam.set(cv2.CAP_PROP_GAIN, 0))

# (Default other parameters)
# Enable auto white balance
print(cam.set(cv2.CAP_PROP_AUTO_WB, 0))

print(cam.set(cv2.CAP_PROP_WB_TEMPERATURE, 6500))
# Default Brightness
print(cam.set(cv2.CAP_PROP_BRIGHTNESS, 80))
# Default Contrast
print(cam.set(cv2.CAP_PROP_CONTRAST, 128))
# Default Saturation
print(cam.set(cv2.CAP_PROP_SATURATION, 255))
# Default Sharpness
print(cam.set(cv2.CAP_PROP_SHARPNESS, 128))

cam.release()
cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_SETTINGS, 1.0)

# Take a picture and show
_, img2 = cam.read()
cv2.imshow("Imagem Final", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()

cam.release()