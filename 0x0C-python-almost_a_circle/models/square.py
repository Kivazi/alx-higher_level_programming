#!/usr/bin/python3

class Square(Rectangle):
    """repeeent a square"""

    def __init__.(self, size, x=0, y=0, id=None):
        """initialize a square.
        size: the size of the square.
        x(int): x codinate of the new square.
        y(int): y codinate of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
