import cv2

# Load the image
img = cv2.imread("HMI.png")

# Get the total number of pixels
# The shape attribute of the image numpy array is used to get the height and width of the image
pixel_count = img.shape[0] * img.shape[1]  

print("The image contains", pixel_count, "pixels where,", img.shape[0], "is the height and", img.shape[1], "is the width.")

# Define the pixel size
pixel_size = 5

# Resize the image to a smaller size
small_img = cv2.resize(img, None, fx=1/pixel_size, fy=1/pixel_size, interpolation=cv2.INTER_NEAREST)

# Resize the small image back to its original
pixelated_img = cv2.resize(small_img, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# Display the original and pixelated images
cv2.imshow("Original Image", img)
cv2.imshow("Pixelated Image", pixelated_img)
cv2.waitKey(0)

#Close all windows
cv2.destroyAllWindows()
