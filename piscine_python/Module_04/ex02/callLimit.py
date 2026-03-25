from typing import Any


def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.
    Args:
        limit (int): Int representing the maximum nomber of allowed calls.
    Returns:
        Callable: A decorator that wraps the function and prevents it from
        being executed more than 'limit' times.
    """
    count = 0

    def callLimiter(function):
        """
        Wraps the given function and tracks the number of calls.
        Args:
            function (callable): The function to limit.
        Returns:
            Callable: The wrapped function with call limitation.
        """
        nonlocal count

        def limit_function(*args: Any, **kwds: Any):
            """
            Executes the function if the call limit has not been reached.
            Args:
                *args: Positional arguments of the function.
                **kwds: Keyword arguments of the function.
            Returns:
                Any: The result of the function call if allowed,
                otherwise prints an error message.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
