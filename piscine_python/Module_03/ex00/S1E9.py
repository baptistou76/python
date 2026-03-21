from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class contains the first_name and the
    health status. Its used as models for the children
    classes.
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character with a name and health
        status defined as True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Change the health status from a character.
        """
        self.is_alive = False


class Stark(Character):
    """
    Class representing a Stark character.
    Inherit from Character abstract class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Starck charcater.
        """
        super().__init__(first_name, is_alive)
