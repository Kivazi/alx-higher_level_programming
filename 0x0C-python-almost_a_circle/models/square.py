#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """repeeent a square"""

    def __init__.(self, size, x=0, y=0, id=None):
        """initialize a square.
        size: the size of the square.
        x(int): x codinate of the new square.
        y(int): y codinate of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
    @width.setter
    def size(self, value):
        self.width = value
        self.height = value

     def update(self, *args, **kwargs):
         """ assigns attributes:
         *args: the list of arguments - no-keyworded arguments
         1st argument: should be the id attribute
         2nd argument: should be the size attribute
         3rd argument: should be the x attribute
         4th argument: should be the y attribute
         **kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
         **kwargs must be skipped if *args exists and is not empty
         Each key in this dictionary represents an attribute to the instance
         """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """ returns a dictionary representation of the square"""
        return {
            'id': self.id,
            'size': self.size
            'x': self.x,
            'y': self.y
        }
