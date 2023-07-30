from sympy import diff, symbols, cos, sin,expand_trig,integrate
x, y = symbols('x y')

k = (x - 3) * (x - 5) * (x - 7) + 85

print(expand_trig(k))

s = float(integrate(k, (x,2, 9)))
