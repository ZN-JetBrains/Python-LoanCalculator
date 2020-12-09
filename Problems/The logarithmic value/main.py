from math import log

x = abs(int(input()))
base = int(input())
result = 0

if base <= 1:
    result = log(x)
else:
    result = log(x, base)

result = round(result, 2)
print(result)
