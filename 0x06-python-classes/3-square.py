#!/usr/bin/python3
"""Square class defination."""

class Square:
    """Square class body."""

    def __init__(self, sized=0):
        """Square contructor.
        Args:
            size (int): The sized of the new square.
        """
        if not isinstance(sized, int):
            raise TypeError("sized must be an integer")
        elif sized < 0:
            raise ValueError("sized must be >= 0")
        self.__sized = sized

    def area(self):
        """Return the new area of the square."""
        return (self.__sized * self.__sized)
