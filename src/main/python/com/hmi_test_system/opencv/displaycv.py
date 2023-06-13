import cv2
import numpy as np
import pytesseract


class Displaycv():

    display_transformation_matrix = None
    display_coordinates = None

    @staticmethod
    def read_char(display):

        # Setup tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Convert image to grayscale
        display_gray = cv2.cvtColor(display, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        display_binary = cv2.threshold(display_gray, 140, 255, cv2.THRESH_BINARY)[1]

        # Read text on display
        text = pytesseract.image_to_string(display_binary, lang='eng')
        text = text.replace("\n\n", "\n")

        return text
    
    @staticmethod
    def extract_display(image, transform_matrix, coordinates):
        
        # Apply the perspective transform matrix to the image
        corrected_image = cv2.warpPerspective(image, transform_matrix, (image.shape[1], image.shape[0]))

        # Extract the display region
        x, y, w, h = cv2.boundingRect(coordinates)
        display = corrected_image[y:y+h, x:x+w]

        return display

    @staticmethod
    def get_transformation_matrix(image):

        if Displaycv.display_transformation_matrix is not None:
            return Displaycv.display_transformation_matrix, Displaycv.display_coordinates

        # Convert image to grayscale
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert images to binary for LCD detection
        image_binary = cv2.threshold(image_gray, 70, 255, cv2.THRESH_BINARY)[1]

        # Find display contour
        image_contours = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        # Check if the display was found
        if len(image_contours) == 0:
            return None, None

        largest_contour = max(image_contours, key=cv2.contourArea)

        # Approximate the contour with a 4-sided polygon
        epsilon = 0.1 * cv2.arcLength(largest_contour, True)
        approx = cv2.approxPolyDP(largest_contour, epsilon, True)
        
        # Define the coordinates of the display's vertices 
        top_right = approx[0][0]
        top_left = approx[1][0]
        bottom_left = approx[2][0]
        bottom_right = approx[3][0]
        display_coords = np.float32([top_left, top_right, bottom_right, bottom_left])

        # Define the coordinates of the rectangle's vertices
        display_width = 11.564 * 50  # atualizar
        display_height = 8.710 * 50  # atualizar
        rectangle_coords = np.float32([top_left, top_left + [display_width, 0], top_left + [display_width, display_height], top_left + [0, display_height]])

        # Calculate the perspective transform matrix
        transform_matrix = cv2.getPerspectiveTransform(display_coords, rectangle_coords)

        Displaycv.display_transformation_matrix = transform_matrix
        Displaycv.display_coordinates = rectangle_coords
        return transform_matrix, rectangle_coords

    @staticmethod
    def get_extracted_display(image):
        if Displaycv.display_transformation_matrix is None:
            transformation_matrix, display_coordinates = Displaycv.get_transformation_matrix(image)
            if transformation_matrix is None:
                return None
            else:
                Displaycv.display_transformation_matrix = transformation_matrix
                Displaycv.display_coordinates = display_coordinates

        corrected_display = Displaycv.extract_display(image, Displaycv.display_transformation_matrix, Displaycv.display_coordinates)

        return corrected_display

    @staticmethod
    def correct_low_sharpness(image, threshold, strength):
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Compute the gradient magnitude using the Sobel operator
        gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

        # Normalize the gradient magnitude to the range [0, 255]
        gradient_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

        # Apply a threshold to detect low sharpness regions
        low_sharpness_mask = cv2.threshold(gradient_normalized, threshold, 255, cv2.THRESH_BINARY)[1]

        # Convert the image to floating-point representation
        image_float = image.astype(np.float32) / 255.0

        # Split the image into color channels
        b, g, r = cv2.split(image_float)

        # Apply unsharp mask to each channel only in the low sharpness regions
        sharpened_b = np.where(low_sharpness_mask > 0, np.clip(b * (1.0 + strength) + cv2.GaussianBlur(b, (0, 0), strength) * -strength, 0.0, 1.0), b)
        sharpened_g = np.where(low_sharpness_mask > 0, np.clip(g * (1.0 + strength) + cv2.GaussianBlur(g, (0, 0), strength) * -strength, 0.0, 1.0), g)
        sharpened_r = np.where(low_sharpness_mask > 0, np.clip(r * (1.0 + strength) + cv2.GaussianBlur(r, (0, 0), strength) * -strength, 0.0, 1.0), r)

        # Merge the corrected channels back into a color image
        corrected_image = cv2.merge((sharpened_b, sharpened_g, sharpened_r))

        # Convert the image back to 8-bit unsigned integer representation
        corrected_image = (corrected_image * 255).astype(np.uint8)

        return corrected_image
    