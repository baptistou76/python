import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Load an image from the given path and return it as
    an array. Prints the shape of the image and the pixel
    content in RGB format.
    """
    try:
        if not isinstance(path, str):
            print("Error: Path must be a string")
            return None
        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            print(f"Error: Unsupported format '{img.format}'")
            return None
        img = img.convert("RGB")
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        return arr
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except Exception as e:
        print("Error:", e)
        return None
