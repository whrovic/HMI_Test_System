import cv2

# Load the image
img = cv2.imread("HMI.png")

#Extract a rectangular region from the image
x, y, w, h = 83, 97, 3, 3 # x, y are top-left coordinates and 2*w, 2*h are width and height respectively
part = img[y-h:y+h, x-w:x+w]

# Display the original and part of the image using OpenCV
cv2.imshow("Original Image", img)
cv2.imshow('Part of the Image', part)
cv2.waitKey(0)
cv2.destroyAllWindows()
