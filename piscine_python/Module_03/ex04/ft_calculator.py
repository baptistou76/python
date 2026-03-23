class calculator:
    """
    Class of Vector calculator utilities uses staticmethod.
    """
    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        result = 0
        for i in range(len(v1)):
            result += v1[i] * v2[i]
        print("Dot product is:", result)

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        result = []
        for i in range(len(v1)):
            result.append(v1[i] + v2[i])
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        result = []
        for i in range(len(v1)):
            result.append(v1[i] - v2[i])
        print("Sous Vector is:", result)
