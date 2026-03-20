from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    The function takes the image 'animal.jpeg' linked to the subject,
    call the ft_load function to display the shape and pixel content.
    The main program will make a 400 x 400 cutting on the image, transpose
    the x and y axis to rotate the image, display the new shape and show
    the result.
    """
    try:
        path = "animal.jpeg"
        img = ft_load(path)
        if img is None:
            return
        h, w, _ = img.shape
        center_y = h // 2
        center_x = w // 2
        size = 200
        y_start = center_y - size
        y_end = center_y + size
        x_start = center_x - size
        x_end = center_x + size
        zoom_img = img[y_start:y_end, x_start:x_end]
        zoom_gray = np.mean(zoom_img, axis=2).astype(np.uint8)
        zoom_gray = zoom_gray[:, :, np.newaxis]
        print(
            f"New shape after slicing: {zoom_gray.shape} "
            f"or ({zoom_img.shape[0]}, {zoom_img.shape[1]})")
        print(zoom_gray)
        # --- Transposing --- #
        gray_2d = zoom_gray[:, :, 0]
        h, w = gray_2d.shape
        transposed = np.zeros((w, h), dtype=np.uint8)
        i = 0
        while i < h:
            j = 0
            while j < w:
                transposed[j][i] = gray_2d[i][j]
                j += 1
            i += 1
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        plt.imshow(transposed, cmap='gray')
        plt.show()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
