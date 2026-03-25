import sys
from ft_filter import ft_filter


def validate_string(s):
    """
    Check if the string countains only alphanumeric characters or spaces.
    Returns:
        True if valid
        False otherwise
    """
    for c in s:
        if not (c.isalnum() or c == ' '):
            return False
    return True


def main():
    """
    Main program that uses the validate_string function to
    check if the string has only alphanumeric characters.
    A lambda function ('word') is passed to the ft_filter function.
    returns:
        Return '0' if the program worked.
        Exit with code error '1' in case of error.
    """
    try:
        assert len(sys.argv) == 3
        s = sys.argv[1]
        n = int(sys.argv[2])
        assert validate_string(s)
        words = s.split()
        result = ft_filter(lambda word: len(word) > n, words)
        print(result)
        return 0
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
