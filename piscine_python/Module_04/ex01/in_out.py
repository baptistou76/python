def square(x: int | float) -> int | float:
    """Function that calculate the square of
    an int or a float passed as en argument.
    Args:
        x (int | float)
    Returns:
        int | float
    """
    return x * x


def pow(x: int | float) -> int | float:
    """Function that calculate the power of
    an in int or a float passed as an argument.
    Args:
        x (int | float)

    Returns:
        int | float
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Create a closure repeatedly applies a function a value.
    The returned function ('inner') keeps the value 'x' in
    memory and, each time it is called, applies the given
    function to the current value of 'x'.
    Args:
        x (int | float): The initial value.
        function (_type_): The function passed as an argument.
    Returns:
        object: A functin ('inner') that, when called, applies
        the given function to the stored value and returns the
        updated result.
    """
    count = 0

    def inner() -> float:
        nonlocal x
        nonlocal count
        count += 1
        x = function(x)
        return x
    return inner
