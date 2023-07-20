from sympy import diff, symbols, cos, sin
x, y = symbols('x y')

print(diff(cos(x)))
print(diff(cos(x) + 1j*sin(y), x))
print(diff(cos(x) + 1j*sin(y), y))
