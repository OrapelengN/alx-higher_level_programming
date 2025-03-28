#!/usr/bin/python3
from models.square import Square


if __name__ == "__main__":
    s = Square.create(**{'size': 2})
    if isinstance(s, Square):
        with open("test_output.txt", "w") as f:
            f.write("OK")
