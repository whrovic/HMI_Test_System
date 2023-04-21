import numpy as np
import cv2
import glob

# Define the size of the chessboard pattern used for calibration
pattern_size = (4, 7)

# Create arrays to store object points (3D points) and image points (2D points)
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Define the real world coordinates of the chessboard pattern
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

# Load calibration images
calibration_images = glob.glob('./IntrinsicCalibration/*.png')

# Loop through each calibration image
for calibration_image in calibration_images:
  # Load the image
  img = cv2.imread(calibration_image)

  # Convert the image to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Find the chessboard corners
  ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

  # If corners are found, add object points and image points
  if ret == True:
      objpoints.append(objp)
      imgpoints.append(corners)

      # Draw and display the corners
      cv2.drawChessboardCorners(img, pattern_size, corners, ret)
      #cv2_imshow(img)
      cv2.waitKey(500)

# Calibrate the camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print the intrinsic matrix and lens distortion coefficients
print("Intrinsic Matrix:")
print(mtx)
print("Distortion Coefficients:")
print(dist)

######################################

# Load the extrinsic image
image_dis = cv2.imread('./WhiteBackground/extrinsic.png')
img = cv2.undistort(image_dis, mtx, dist, None)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the size of the black square in the chessboard pattern (in millimeters)
square_size = 22

# Define the dimensions of the chessboard pattern
pattern_size = (4, 7)

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

# Calculate the conversion ratio between pixel and millimeter
n = 1
if ret == True:
    # Calculate the distance between the corners of a black square
    for i in range(len(corners) - 1):
      if not(i == 3 or i == 7 or i == 11 or i == 15 or i == 19 or i == 23):
        square_distance_pixels = np.linalg.norm(corners[i] - corners[i + 1])
        pixel_to_mm = pixel_to_mm + (square_size / square_distance_pixels)
        n = n + 1

    pixel_to_mm = pixel_to_mm/n

    # Print the conversion ratio
    print("Conversion ratio (pixel to mm):", pixel_to_mm)

    # Calculate the extrinsic matrix
    ret, rvecs, tvecs = cv2.solvePnP(np.zeros((pattern_size[0]*pattern_size[1],3), np.float32), corners, mtx, dist)
    R, _ = cv2.Rodrigues(rvecs)
    extrinsic_matrix = np.hstack((R, tvecs))
    print("Extrinsic Matrix:")
    print(extrinsic_matrix)
else:
    print("Error: chessboard corners not found.")