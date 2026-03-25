from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    The function accepts any numbers of positionnal
    arguments representing numeric values. It calculates
    statistics depending on the keyword arguments provided.
    Supported keywords values:
    -"mean"     : average of numbers
    -"median"   : middle value of the sorted numbers
    -"quartile" : first and third quartiles
    -"var"      : variance
    -"std"      : standard deviation
    Args:
        *args (Any): A variable number of numeric values
        **kwargs(Any): keywords specifying wich statistics to displays.
    Returns:
        None
    """
    if not args:
        print("ERROR")
        return None
    try:
        numbers = [float(x) for x in args]
    except ValueError:
        print("ERROR")
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mean = sum(sorted_nums) / n
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    q1 = sorted_nums[n//4]
    q3 = sorted_nums[(3*n)//4]
    variance = sum((x - mean)**2 for x in sorted_nums) / n
    std = variance ** 0.5
    for value in kwargs.values():
        if value == "mean":
            print(f"mean: {mean}")
        elif value == "median":
            print(f"median: {median}")
        elif value == "quartile":
            print(f"quartiles: [{q1}, {q3}]")
        elif value == "var":
            print(f"var: {variance}")
        elif value == "std":
            print(f"std: {std}")
        else:
            print("ERROR")
