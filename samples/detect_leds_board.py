import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
_, image = cam.read()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(image_gray, 45, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    
    if len(approx) == 4:  # L-shaped objects typically have four vertices
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        
        if aspect_ratio >= 0.8 and aspect_ratio <= 1.2:
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)  # Draw the contour on the original image

cv2.imshow("L-Shaped Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
