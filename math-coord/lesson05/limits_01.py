from sympy import *
str_expr = "x**2 + 3*x - 1/2"
expr = sympify(str_expr)
print(expr)
print(expr.subs('x', 2))



x = symbols('x')
x0=0
func = sin(x)/x
print (limit(func, x, x0))