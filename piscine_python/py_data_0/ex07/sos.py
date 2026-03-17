import sys


def validate_args(s):
    """
    Check if the string countains only alphanumeric characters or spaces.
    Return True if valid, False otherwise
    """
    for c in s:
        if not (c.isalnum() or c == ' '):
            return False
    return True


MORSE_DICT = {
    """"
    The dictionnary contained the morse code
    """
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.",
    " ": "/"
}


def encode_morse(s):
    """"
    This function will translate the string in morse code
    """
    s = s.upper()
    return ' '.join(MORSE_DICT[c] for c in s)


def main():
    """
    Main program
    """
    try:
        assert len(sys.argv) == 2
        s = sys.argv[1]
        assert validate_args(s)
        print(encode_morse(s))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
