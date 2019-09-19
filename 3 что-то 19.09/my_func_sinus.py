import math

x = float(input("Введите число "))
print(1 if x < 0.2 or x > 0.9 else math.sin(x))
