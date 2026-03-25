import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Check if the values are int or float and calculate the bmi.
    Args:
        Height: a list contains int or float.
        Weight: a list contains int or float.
    Return a bmi array
    """
    if len(height) != len(weight):
        raise ValueError("Lists must be the same size")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("All values must be int or float")
    h = np.array(height)
    w = np.array(weight)
    return (w / (h ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check the limit passed as parameter and return true or false
    """
    arr = np.array(bmi)
    return(arr > limit).tolist()
