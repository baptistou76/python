from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    The function takes the image 'animal.jpeg' linked to the subject,
    called the ft_load function for print the shape.
    The main program will make a 400 x 400 zoom on the image, print
    the new shape and show the result.
    """
    try:
        path = "animal.jpeg"
        if not path:
            print("Error: 'animal.jpeg' is missing")
            return None
        img = ft_load(path)
        if img is None:
            return
        y_start, y_end = 100, 500
        x_start, x_end = 450, 850
        zoom_img = img[y_start:y_end, x_start:x_end]
        zoom_gray = np.mean(zoom_img, axis=2).astype(np.uint8)
        zoom_gray = zoom_gray[:, :, np.newaxis]
        print(f"New shape after slicing: {zoom_gray.shape} or \
                {zoom_img.shape[0]}, ({zoom_img.shape[1]})")
        print(zoom_gray)
        plt.imshow(zoom_gray[:, :, 0], cmap='gray')
        plt.title("Zoomed Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
