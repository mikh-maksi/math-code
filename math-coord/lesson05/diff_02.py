from sympy import diff, symbols, cos, sin
x, y = symbols('x y')

print(diff(cos(x)))

z = diff(cos(x))
print(z)
k = z.subs(x,4)
print(k)
print(k.evalf())
# for i in range(1000):

