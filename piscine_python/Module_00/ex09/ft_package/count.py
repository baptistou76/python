def count_in_list(lst, value):
    """
    Counting the items from a list.
    Return the count value.
    """
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count
