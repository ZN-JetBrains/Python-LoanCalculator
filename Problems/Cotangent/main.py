from math import sin
from math import cos
from math import radians

angle = int(input())
angle = radians(angle)
cotangent = round(cos(angle) / sin(angle), 10)
print(cotangent)
