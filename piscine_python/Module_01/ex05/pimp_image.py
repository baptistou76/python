from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def ft_invert(array) -> np.array:
    """
    Invert the colors of the image.
    """
    img = 255 - array
    Image.fromarray(img).show()
 

def ft_red(array):
    """
    Keep only the red channel
    """
    red = np.copy(array)
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    Image.fromarray(red).show()


def ft_green(array):
    """
    Keep only the green channel
    """
    green = np.copy(array)
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    Image.fromarray(green).show()


def ft_blue(array):
    """
    Keep only ther blue channel
    """
    blue = np.copy(array)
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Image.fromarray(blue).show()


def ft_grey(array):
    """
    Convert the image to greyscale.
    """
    grey = np.mean(array, axis=2).astype(np.uint8)
    plt.imshow(grey, cmap='gray')
    plt.axis('off')
    plt.show()
