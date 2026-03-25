def NULL_not_found(object: any) -> int:
    """
    Identify and print the NULL type of a given object.
    Args:
        object (any): Object to identified.
    Returns:
        int: Return '0' if the object was identified.
        int: Return '1' in case of unknown NULL type.
    Prints:
        Prints the NULL type of the object.
    """
    if object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
    elif (isinstance(object, int) and object == 0
            and not isinstance(object, bool)):
        print("Zero:", object, type(object))
    elif isinstance(object, str) and object == "":
        print("Empty:", object, type(object))
    elif isinstance(object, bool) and object is False:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return(1)
    return(0)
