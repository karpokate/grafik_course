import cv2
from skimage import img_as_int, img_as_ubyte
from PIL import Image
import scipy.ndimage.filters as flt
import numpy as np

img_gray = img_as_int(cv2.imread('giraffe.jpg', 0))


sobel_vertical = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

Image.fromarray(flt.convolve(img_gray, sobel_vertical)).show()

sobel_horizontal = sobel_vertical.T
Image.fromarray(flt.convolve(img_gray, sobel_horizontal)).show()



sobel_x = cv2.Sobel(img_gray, -1, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img_gray, -1, 0, 1, ksize=5)

Image.fromarray(sobel_x).show()
Image.fromarray(sobel_y).show()