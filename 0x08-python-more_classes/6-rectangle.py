#!/usr/bin/python3
"""
Defines a class Rectangle
"""

class Rectangle:
	"""Representation of a rectangle"""
	
	number_of_instances = 0

	def __init__(self, width=0, height=0):
		"""Initializes the rectangle"""
		self.width = width
		self.height = height
		Rectangle.number_of_instances += 1

	def __del__(self_:
		"""prints a string when an instance has been deleted"""
		print("Bye rectangle...")
		Rectangle.number_of_instances -= 1

	@property
	def width(self):
		"""getter for the private instance attribute width"""
		return self._width

	@width.setter
	def width(self, value):
		"""setter for the private instance attribute width"""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""getter for the private instance attribute height"""
		return self.__height
