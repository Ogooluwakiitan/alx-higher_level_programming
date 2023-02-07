<<<<<<< HEAD
#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
        size (int): size of a side of the square

        Returns:
        None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculaes the square's area
        Returns:
        The area of the square
        """
        return (self.__size) ** 2
=======
#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
>>>>>>> 4a5663aa41e3718aabd1e24d94809b97711d7147
