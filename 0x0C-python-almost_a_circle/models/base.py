#!/usr/bin/python3

class Base:
    """represents the base for all base models
    __nb_objects is the number of instiated bases.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """ initializing new base
           with id as the identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
