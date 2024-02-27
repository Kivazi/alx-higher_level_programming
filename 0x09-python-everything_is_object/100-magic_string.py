#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (string_magic.n -1) + "BestSchool")
