from math import sqrt

a = int(input())
area = round(2 * sqrt(3) * a ** 2, 2)
volume = round((1 / 3) * sqrt(2) * a ** 3, 2)
print(f"{area} {volume}")
