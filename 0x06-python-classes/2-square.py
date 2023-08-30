#!/usr/bin/python3
# 2-square.py
"""Square class defination."""

class Square:
    """Square class body"""

    def __init__(self, sized=0):
        """Square class contructor
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(sized, int):
            raise TypeError("size must be an integer")
        elif sized < 0:
            raise ValueError("size must be >= 0")
        self.__sized = sized
