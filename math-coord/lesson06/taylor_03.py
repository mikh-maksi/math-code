from math import factorial


def taylor(x, n):
    return sum((1+x) ** i / factorial(i) for i in range(n + 1))

print(taylor(100,2))