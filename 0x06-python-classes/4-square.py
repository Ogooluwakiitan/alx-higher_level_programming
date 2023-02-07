<<<<<<< HEAD
#!/usr/bin/python3
"""Square related feature module."""


class Square:
    """Class that define a Square."""
    def __init__(self, size=0):
        """
        Args:
        size (int): size initializer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Compute the area of the Square.
            Returns:
            The area. An (integer)
            """
            return (self.__size ** 2)

        @property
        def size(self):
            """__size property getter"""
            return self.__size

        @size.setter
        def size(self, value):
            """__size property setter.
            Args:
            value (int): new size value
            Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is < 0
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")

            self.__size = value
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
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
>>>>>>> 4a5663aa41e3718aabd1e24d94809b97711d7147
