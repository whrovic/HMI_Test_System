import os
import cv2
import numpy as np
import pytesseract
from skimage.metrics import structural_similarity as ssim


class Displaycv():

    display_transformation_matrix = None
    display_coordinates = None

    ## CAMERA PARAMETERS - only needs to be done once, since the camera is always the same
     #                   - camera_matrix and dist_coeffs must be saved for the eternity
     #                   - all the images used by cv need to be undistorted
     #                     example: undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
    @staticmethod
    def intrinsic_calibration():

        # Define the size of the chessboard pattern used for calibration
        pattern_size = (9, 13)

        # Create arrays to store object points (3D points) and image points (2D points)
        objpoints = []  # 3D points in real world space
        imgpoints = []  # 2D points in image plane

        # Define the real world coordinates of the chessboard pattern
        objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
        objp[:,:2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

        # Define the path to the calibration images folder
        calibration_folder = "..\..\..\..\..\model_images\intrinsic_calibration"

        # Get the list of image filenames in the calibration folder
        image_files = os.listdir(calibration_folder)

        # Iterate over the image files and load them into the calibration_images list
        calibration_images = []
        for image_file in image_files:
            image_path = os.path.join(calibration_folder, image_file)
            image = cv2.imread(image_path)
            calibration_images.append(image)

        # Loop through each calibration image
        for calibration_image in calibration_images:
            # Convert the image to grayscale
            gray = cv2.cvtColor(calibration_image, cv2.COLOR_BGR2GRAY)

            # Find the chessboard corners
            ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

            # If corners are found, add object points and image points
            if ret == True:
                objpoints.append(objp)
                imgpoints.append(corners)

        # Calibrate the camera
        _, camera_matrix, dist_coeffs, _, _ = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        return camera_matrix, dist_coeffs

    camera_matrix, dist_coeffs = intrinsic_calibration()

    ## TRANSFORMATION MATRIX - only needs to be done at the start of each video, assuming the camera is static the entire time
    #                        - transform_matrix and rectangle_coords must be saved until the end of the test
    @staticmethod
    def get_transformation_matrix(image):

        if Displaycv.display_transformation_matrix is not None:
            return
        
        image = cv2.undistort(image, Displaycv.camera_matrix, Displaycv.dist_coeffs)

        # Convert image to grayscale
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert images to binary for LCD detection
        image_binary = cv2.threshold(image_gray, 70, 255, cv2.THRESH_BINARY)[1]

        # Find display contour
        image_contours = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        if len(image_contours) == 0:
            return None, None
        
        largest_contour = max(image_contours, key=cv2.contourArea)

        # Approximate the contour with a 4-sided polygon
        epsilon = 0.1 * cv2.arcLength(largest_contour, True)
        approx = cv2.approxPolyDP(largest_contour, epsilon, True)
        
        if len(approx) < 4:
            return None, None

        # Define the coordinates of the display's vertices 
        top_left = approx[1][0]
        bottom_left = approx[2][0]
        bottom_right = approx[3][0]
        top_right = approx[0][0]

        display_coords = np.float32([top_left, top_right, bottom_right, bottom_left])

        # Define the coordinates of the rectangle's vertices
        display_width = 11.2 * 50   # 11.5
        display_height = 8.32 * 50  # 8.6
        rectangle_coords = np.float32([top_left, top_left + [display_width, 0], top_left + [display_width, display_height], top_left + [0, display_height]])

        # Calculate the perspective transform matrix
        transform_matrix = cv2.getPerspectiveTransform(display_coords, rectangle_coords)

        Displaycv.display_transformation_matrix = transform_matrix
        Displaycv.display_coordinates = rectangle_coords

    @staticmethod
    def undistort_image(image):
        return cv2.undistort(image, Displaycv.camera_matrix, Displaycv.dist_coeffs)

    ## DISPLAY EXTRACTION - the display must be extracted from all images used by cv
    @staticmethod
    def extract_display(image):

        image = cv2.undistort(image, Displaycv.camera_matrix, Displaycv.dist_coeffs)

        # Apply the perspective transform matrix to the image
        corrected_image = cv2.warpPerspective(image, Displaycv.display_transformation_matrix, (image.shape[1], image.shape[0]))

        # Extract the display region
        x, y, w, h = cv2.boundingRect(Displaycv.display_coordinates)
        display = corrected_image[y:y+h, x:x+w]
        
        return display

    @staticmethod
    def read_display(display):

        # Setup tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Apply bilateral filter
        display = cv2.bilateralFilter(display, 27, 75, 75)

        # Convert image to grayscale
        display_gray = cv2.cvtColor(display, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        display_binary = cv2.threshold(display_gray, 0, 255, cv2.THRESH_OTSU)[1]

        # Read text on display
        text = pytesseract.image_to_string(display_binary, lang='eng', config='--psm 6')
        text = text.replace("\n\n", "\n")

        return text
    
    @staticmethod
    def compare_display(image, model, threshold_avg_ssim, threshold_min_ssim, threshold_mse):

        # Perform image registration using SIFT
        sift = cv2.SIFT_create()
        keypoints_image, descriptors_image = sift.detectAndCompute(image, None)
        keypoints_model, descriptors_model = sift.detectAndCompute(model, None)

        # Match keypoints
        matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches = matcher.match(descriptors_image, descriptors_model)

        # Sort matches by distance
        matches = sorted(matches, key=lambda x: x.distance)

        # Extract matched keypoints
        src_points = np.float32([keypoints_image[m.queryIdx].pt for m in matches])
        dst_points = np.float32([keypoints_model[m.trainIdx].pt for m in matches])

        # Calculate transformation matrix using RANSAC
        transformation_matrix, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC)

        # Warp the image to align with the model
        image = cv2.warpPerspective(image, transformation_matrix, (model.shape[1], model.shape[0]))

        # Convert the images to the Lab color space
        image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        model_lab = cv2.cvtColor(model, cv2.COLOR_BGR2Lab)

        # Calculate the width and height of each rectangle
        rect_width = model.shape[1] // 40
        rect_height = model.shape[0] // 16

        ssim_score = []
        diff_image = np.zeros_like(image_lab[:, :, 1], dtype=np.float64)

        # Loop over each rectangle and calculate the structural similarity index (SSIM)
        for i in range(40):
            for j in range(16):
                # Calculate the coordinates of the rectangle
                x = i * rect_width
                y = j * rect_height
                # Extract the rectangle
                image_rect = image_lab[y:y+rect_height, x:x+rect_width]
                model_rect = model_lab[y:y+rect_height, x:x+rect_width]
                # Calculate the SSIM score between the 'a' and 'b' channels
                ssim_a, diff_a = ssim(image_rect[:, :, 1], model_rect[:, :, 1], win_size=3, full=True)
                ssim_b, diff_b = ssim(image_rect[:, :, 2], model_rect[:, :, 2], win_size=3, full=True)
                ssim_score.append((ssim_a + ssim_b) / 2)
                # Add rectangle's difference to the difference image
                diff_image[y:y + rect_height, x:x + rect_width] = diff_a + diff_b

        # Display the difference image
        diff_image = cv2.convertScaleAbs(diff_image * 255)

        # Calculate the average and the minimum SSIM score
        avg_ssim = np.mean(ssim_score)
        min_ssim = np.min(ssim_score)

        # Calculate the MSE for channels 'a' and 'b'
        mse_a = np.mean((image_lab[:, :, 1] - model_lab[:, :, 1]) ** 2)
        mse_b = np.mean((image_lab[:, :, 2] - model_lab[:, :, 2]) ** 2)
        mse = (mse_a + mse_b) / 2

        print(avg_ssim, threshold_avg_ssim)
        print(min_ssim, threshold_min_ssim)
        print(mse, threshold_mse)
        print()
        
        cv2.imshow('IMG', image)
        cv2.imshow('MODEL', model)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return avg_ssim > threshold_avg_ssim and min_ssim > threshold_min_ssim and mse < threshold_mse
    