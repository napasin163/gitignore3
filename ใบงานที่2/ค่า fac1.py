x = input(" Enter Number: ")
x = int(x)

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
y = x - x**3/fac(3) + x**5/fac(5) - x**7/fac(7) + x**9/fac(9)
print("{:.7f}".format(y))
