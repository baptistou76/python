import sys
import string


def Analyzer(text):
    """
    Function that counts the number of different characters.
    How many uppercase letters, lowercase letters, punctuations, ...
    Args:
        text to analyze.
    Prints:
        Prints the differents values of counted characters.
    """
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            spaces += 1
        elif c in string.punctuation:
            punctuation += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuations marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Main program takes a string as an argument or read the stdin entry
    and uses the Analyzer function to count the number of different
    characters.
    Returns:
        Return '0' if it worked.
        Exit with code 1 in case of error.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        exit(1)
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        text = sys.stdin.read()
    Analyzer(text)
    return 0


if __name__ == "__main__":
    main()
