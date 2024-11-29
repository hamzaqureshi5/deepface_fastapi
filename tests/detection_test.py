import cv2
from detection.detection import process_image
import  numpy as np

input_image: np.ndarray = cv2.imread("example_1.jpg")
print(process_image(input_image))
