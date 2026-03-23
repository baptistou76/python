class calculator:
    """
    Class contains a lot of functions able to calcutlate
    a vector content.
    """
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, value) -> None:
        result = []
        for num in self.vector:
            result.append(num + value)
        self.vector = result
        print(result)

    def __mul__(self, value) -> None:
        result = []
        for num in self.vector:
            result.append(num * value)
        self.vector = result
        print(result)

    def __sub__(self, value) -> None:
        result = []
        for num in self.vector:
            result.append(num - value)
        self.vector = result
        print(result)

    def __truediv__(self, value) -> None:
        result = []
        for num in self.vector:
            result.append(num / value)
        self.vector = result
        print(result)
