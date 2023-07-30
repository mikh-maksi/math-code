from sympy import diff, symbols, cos, sin
x, y = symbols('x y')

print(diff((x*x)))

z = diff((x*x))
print(z)
k = z.subs(x,4)
print(k)
print(k.evalf())
for i in range(1000):
    print(z.subs(x,i))

