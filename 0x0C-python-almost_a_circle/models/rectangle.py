#!/usr/bin/python3
from models import base

class Rectangle(Base):
    """class Rectangle: inherits from the Base clase"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    return self.width = __width

    @width.setter
    def width(self, value):
        if Type(value) != int:
            raise TypeError ("width must be an integer")
        if value <= 0:
            raise ValueError ("width must be > 0")
        self.__width = value
    
    @property
    return self.height = __height

    @width.setter
    def height(self, value):
        if Type(value) != int:
            raise TypeError ("height must be an integer")
        if value <= 0:
            raise ValueError ("height must be > 0")
        self.__height = value
    
    @property
    return self.x = __x

    @width.setter
    def x(self, value):
         if Type(value) != int:
            raise TypeError ("x must be an integer")
        if value < 0:
            raise ValueError ("x must be >= 0")
        self.__x = value
    
    @property
    return self.y = __y

    @width.setter
    def y(self, value):
         if Type(value) != int:
            raise TypeError ("y must be an integer")
        if value < 0:
            raise ValueError ("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        if self.__width == 0 and self.__height == 0:
            print("")
        return
    [print("") for y in range(self.y)]
    for i in range(self.height):
        for x in range(self.x):
            print("", end="")
        for w in range(self.width):
            print("#", end="")
        print("")

    def update(self, *args, *kwargs):
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
    def __str__(self):
        """Return the print() and str() rep of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
                
                    
