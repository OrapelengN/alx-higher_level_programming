#!/usr/bin/python3
from models.square import Square

if __name__ == "__main__":
    s = Square.create(**{'size': 2})
    if isinstance(s, Square):
        print("OK")
