from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(file):
    img = Image.open(file)
    
    img_array = np.array(img)
    return img_array

def edge_detection(image_array):
  print(image_array.shape)
  grayscale_image = np.mean(image_array, axis=2)
  kernelY = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
  ])
  kernelX = np.array([
    [-1, 0, 1],
    [-2, 0,2],
    [-1, 0, 1]
  ])
  edgeX = signal.convolve2d(grayscale_image, kernelX, mode='same', boundary='symm')
  edgey = signal.convolve2d(grayscale_image, kernelY, mode='same', boundary='symm')
  edgeMAG = np.sqrt(edgeX**2 + edgey**2)
  return edgeMAG
