import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Default all the camara parameters
# Enable auto focus
cam.set(cv2.CAP_PROP_AUTOFOCUS, 1)
# Enable auto exposure
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
# Enable auto white balance
cam.set(cv2.CAP_PROP_AUTO_WB, 1)
# Default Brightness
cam.set(cv2.CAP_PROP_BRIGHTNESS, 128)
# Default Contrast
cam.set(cv2.CAP_PROP_CONTRAST, 128)
# Default Saturation
cam.set(cv2.CAP_PROP_SATURATION, 128)
# Default Sharpness
cam.set(cv2.CAP_PROP_SHARPNESS, 128)

# Take a picture and show

_, img = cam.read()
print(img)

cv2.imshow("Original Image", img)
cv2.waitKey(0)

cam.release()
cam = None
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Changes parameters for the display settings

# Disable auto focus
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# Set manually focus [0:255, step=5]
cam.set(cv2.CAP_PROP_FOCUS, 15)
# Disable auto exposure
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
# Set manually exposure
cam.set(cv2.CAP_PROP_EXPOSURE, -8)
# Set manually exposure gain
cam.set(cv2.CAP_PROP_GAIN, 3)

# (Default other parameters)
# Enable auto white balance
cam.set(cv2.CAP_PROP_AUTO_WB, 1)
# Default Brightness
cam.set(cv2.CAP_PROP_BRIGHTNESS, 128)
# Default Contrast
cam.set(cv2.CAP_PROP_CONTRAST, 128)
# Default Saturation
cam.set(cv2.CAP_PROP_SATURATION, 128)
# Default Sharpness
cam.set(cv2.CAP_PROP_SHARPNESS, 128)

# Take a picture and show
_, img2 = cam.read()
cv2.imshow("Imagem Final", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()

cam.release()