<<<<<<< HEAD
#!/usr/bin/python3
"""create class"""


class Square:
    """Private instance attribute"""
    def __init__(self, size=0):
        """initializes the square
        Args
        size (int): size of a side of the square
        Returns
        None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:

                self.__size = size
=======
#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
>>>>>>> 4a5663aa41e3718aabd1e24d94809b97711d7147
