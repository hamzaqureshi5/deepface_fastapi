# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import numpy as np
from detection.detection import process_image_pred


def process_wrapper(input_image: np.ndarray):
    return process_image_pred(input_image)