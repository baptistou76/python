import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D list, converts it into a NumPy array
    and return a sliced version of it between the given
    start and end indices.
    Print the original shape and the new shape after slicing.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: start and end must be integers")
        return None
    if not isinstance(family, list):
        print("Error: not a list")
        return None
    if not all(isinstance(row, list) for row in family):
        print("Error: not a 2D list")
        return None
    if len(family) == 0:
        print("Error: empty list")
        return None
    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        print("Error: rows are not the same size")
        return None
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    new_arr = arr[start:end]
    print(f"My new shape is : {new_arr.shape}")
    return new_arr.tolist()
