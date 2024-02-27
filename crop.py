import cv2
import numpy as np
import os

def crop_image_around_face(image_path, output_path, output_size, min_confidence):
    # Load image
    image = cv2.imread(image_path)
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5, minSize=(30, 30))
    
    # Filter faces based on confidence score
    faces = [face for face in faces if face[2] > min_confidence]

    if len(faces) > 0:
        # Calculate the center of the first detected face
        (x, y, w, h) = faces[0]
        face_center = (x + w // 2, y + h // 2)
        
        # Calculate the cropping region to center the face
        crop_x = max(face_center[0] - output_size[0] // 2, 0)
        crop_y = max(face_center[1] - output_size[1] // 2, 0)
        
        # Ensure the cropping region does not exceed image boundaries
        crop_x = min(crop_x, image.shape[1] - output_size[0])
        crop_y = min(crop_y, image.shape[0] - output_size[1])
        
        # Crop image
        cropped_image = image[crop_y:crop_y + output_size[1], crop_x:crop_x + output_size[0]]
        
        print("Detection ok:", os.path.basename(image_path))
        # Save cropped image
        cv2.imwrite(output_path, cropped_image)
    else:
        print("No face detected in:", os.path.basename(image_path))
        # Perform default crop if no face is detected
        default_crop(image, output_path, output_size)

def default_crop(image, output_path, output_size):
    # Calculate image center
    image_center = (image.shape[1] // 2, image.shape[0] // 2)
    
    # Calculate the cropping region to center the image
    crop_x = max(image_center[0] - output_size[0] // 2, 0)
    crop_y = max(image_center[1] - output_size[1] // 2, 0)
    
    # Crop image
    cropped_image = image[crop_y:crop_y + output_size[1], crop_x:crop_x + output_size[0]]
    
    # Save cropped image
    cv2.imwrite(output_path, cropped_image)

def bulk_crop_images(image_dir, output_dir, output_size, min_confidence):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each image in the input directory
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'): # Adjust extensions as needed
            input_path = os.path.join(image_dir, filename)
            output_path = os.path.join(output_dir, filename)
            crop_image_around_face(input_path, output_path, output_size, min_confidence)

# Example usage
input_dir = 'test'
output_dir = 'output'
#input_dir = 'input_images'
#output_dir = 'output_cropped_images'
output_size = (450, 450)  # Adjust this tuple to specify the desired output size (width, height)
min_confidence = 50        # Adjust this value to control the minimum confidence threshold for face detection
bulk_crop_images(input_dir, output_dir, output_size, min_confidence)
