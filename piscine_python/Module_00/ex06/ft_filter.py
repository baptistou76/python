def ft_filter(function, iterable):
    """
    Reproduce the behavior of the built-in filter function.
    If no function passed as an arugument, it will return the entire
    list as true.
    Otherwise, it will iterate over each of the item in the list.
    """
    if function is None:
        return[item for item in iterable if item]
    return[item for item in iterable if function(item)]
