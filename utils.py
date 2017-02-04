import math
import pygame

class vector2:
   # note, no data member declarations needed

   # constructor
   def __init__(self, x, y):
      # unlike C/Java, no implicit "this" pointer
      # instead, reference is passed in as first argument (self in this case)
      self.x = x
      self.y = y

   # method definitions
   def add(self, other):
      v = vector2(self.x + other.x, self.y + other.y)
      return v

   def scale(self, scalar):
      v = vector2(self.x * scalar, self.y * scalar)
      return v

   def sub(self, other):
      return vector2(self.x - other.x, self.y - other.y)

   def magnitude(self):
      return math.sqrt(self.x**2 + self.y**2)

   def normalize(self):
      m = self.magnitude()
      return vector2(self.x/m, self.y/m)


   # overload return-this-as-string for printing
   def __str__(self):
      # format allows you to replace "{}" with variable values
      return "({}, {})".format(self.x, self.y)