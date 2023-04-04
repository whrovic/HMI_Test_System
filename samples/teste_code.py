import cv2
import numpy as np

#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#if (cap.isOpened()):
#    print("Working")

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#ret, frame = cap.read()

#cap.release()

#cv2.imshow("Frame", frame)
#cv2.waitKey(0)

# Load the image
img = cv2.imread("HMI.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Canny edge detection algorithm to the grayscale image
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find contours in the edge image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

iBlues = 0
iGreens = 0
iReds = 0

# Iterate over each contour
for contour in contours:
    # Approximate the contour to a polygon
    polygon = cv2.approxPolyDP(contour, 0.05 * cv2.arcLength(contour, True), True)

    area = cv2.contourArea(polygon)

    if (area < 500):
        continue

    x,y,w,h = cv2.boundingRect(contour)
    roi = img[y:y+h, x:x+w]
    hsv_roi = hsv[y:y+h, x:x+w]
    
    total_pixels = w*h

    mask_blue = cv2.inRange(hsv_roi, (100, 50, 50), (130, 255, 255))
    blue_pixels = cv2.countNonZero(mask_blue)
    blue_ration = blue_pixels / total_pixels

    mask_green = cv2.inRange(hsv_roi, (40, 50, 50), (80, 255, 255))
    green_pixels = cv2.countNonZero(mask_green)
    green_ration = green_pixels / total_pixels

    mask_red1 = cv2.inRange(hsv_roi, (0,50,50), (10,255,255))
    mask_red2 = cv2.inRange(hsv_roi, (170,50,50), (180,255,255))
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    red_pixels = cv2.countNonZero(mask_red)
    red_ration = red_pixels / total_pixels

    if (area > 2000):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    elif (blue_ration > 0.5):
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        iBlues += 1
    elif (green_ration > 0.5):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        iGreens += 1
    elif (red_ration > 0.5):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        iReds += 1

print("Azuis = ", iBlues)
print("Verdes = ", iGreens)
print("Vermelhos = ", iReds)


# Display the image with detected rectangles
cv2.imshow("Rectangles", img)

def callback(event, x, y, flags, params):
    if (event == cv2.EVENT_LBUTTONDOWN):
        print(f"Coordenada = ({y}, {x}) | RGB = ({np.flip(img[y,x])}) | HSV = ({hsv[y,x]})")

cv2.setMouseCallback('Rectangles', callback)


cv2.waitKey(0)
cv2.destroyAllWindows()
