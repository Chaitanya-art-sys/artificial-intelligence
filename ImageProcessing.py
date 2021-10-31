#This program will improve image sharpness and constrast

#importing libraries
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
from PIL import Image, ImageEnhance, ImageFilter

# Open the image by specifying the image path.
image_path = "image path"
image_file = Image.open(image_path)

#enhance the image
factor = 2 

#increase contrast
enhancer = ImageEnhance.Contrast(image_file)
image_file = enhancer.enhance(factor)

#increase sharpness
enhancer = ImageEnhance.Sharpness(image_file)
image_file = enhancer.enhance(factor)