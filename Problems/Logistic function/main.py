from math import e

x = int(input())
sigmoid = pow(e, x) / (pow(e, x) + 1)
print(round(sigmoid, 2))
