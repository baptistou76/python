import sys
from ft_filter import ft_filter


def validate_string(s):
    """
    Check if the string countains only alphanumeric characters or spaces.
    Return True if valid, False otherwise
    """
    for c in s:
        if not (c.isalnum() or c == ' '):
            return False
    return True


def main():
    """
    Main program.
    """
    try:
        assert len(sys.argv) == 3
        s = sys.argv[1]
        n = int(sys.argv[2])
        assert validate_string(s)
        words = s.split()
        result = ft_filter(lambda word: len(word) > n, words)
        print(result)
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
