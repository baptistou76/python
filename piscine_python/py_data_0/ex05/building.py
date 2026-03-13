import sys
import string


def Analyzer(text):

    """
    Count different types of characters in the text.
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
    Main program.
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


if __name__ == "__main__":
    main()
