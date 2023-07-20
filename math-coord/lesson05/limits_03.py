from sympy import *

x = symbols('x')
x0=oo
func = (7*(x**2)+7*x-2)/(x**2-2*x+3)
print (limit(func, x, x0))