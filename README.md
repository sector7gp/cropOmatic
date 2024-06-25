# Image Cropping Tool

This Python script uses OpenCV to detect and crop images around faces. It processes all images in a specified directory, cropping them to a specified size centered on the detected face, or performing a default center crop if no face is detected.

## Description

### `crop_image_around_face(image_path, output_path, output_size, min_confidence)`
This function crops an image around the first detected face with a confidence score above a specified threshold.
- **image_path**: Path to the input image file.
- **output_path**: Path to save the cropped image file.
- **output_size**: Tuple specifying the width and height of the cropped image.
- **min_confidence**: Minimum confidence threshold for face detection.

### `default_crop(image, output_path, output_size)`
If no face is detected, this function performs a default crop centered on the image.
- **image**: The input image.
- **output_path**: Path to save the cropped image file.
- **output_size**: Tuple specifying the width and height of the cropped image.

### `bulk_crop_images(image_dir, output_dir, output_size, min_confidence)`
This function processes all images in a given directory, applying the face-centered crop or default crop to each image.
- **image_dir**: Directory containing the input images.
- **output_dir**: Directory to save the cropped images.
- **output_size**: Tuple specifying the width and height of the cropped images.
- **min_confidence**: Minimum confidence threshold for face detection.


## Usage Example
```
input_dir = 'test'
output_dir = 'output'
output_size = (450, 450)  # Desired output size (width, height)
min_confidence = 50       # Minimum confidence threshold for face detection

bulk_crop_images(input_dir, output_dir, output_size, min_confidence)
```


Make sure to adjust input_dir, output_dir, output_size, and min_confidence according to your needs. The script will create the output directory if it doesn't exist and will process all .jpg and .png images found in the input directory.


The description was made with ChatGPT4
