#!/usr/bin/python3
"""Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square

    Args:
        Rectangle ([type]): [description]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ [summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ [summary]

        Returns:
            [type]: [description]
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """size [summary]

        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """size [summary]

        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update [summary]
        """
        arguments = ["id", "size", "x", "y"]
        if args:
            for arg in range(len(args)):
                setattr(self, arguments[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary [summary]

        Returns:
            [type]: [description]
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
