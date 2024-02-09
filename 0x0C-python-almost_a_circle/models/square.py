#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square inherates from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the public instance
        args: size, x, y, id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width
    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the square"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    def to_dictionary(self):
        """return dictionary representation of square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
