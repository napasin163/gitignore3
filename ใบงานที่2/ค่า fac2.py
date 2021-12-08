import math

x = int(input(" Enter number: "))
y = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9)
print("{:.7f}".format(y))
