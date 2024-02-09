#!/usr/bin/pyhon3
from models.base import Base

class Rectangle(Base):
    """define a REctangle class"""
    def __init__(self, width, height, x, y, id=None):
        
    """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        self.width = __width
        self.height = __height
        self.x = __x
        self.y = __y
        super.__init__(id)
        
    """Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
