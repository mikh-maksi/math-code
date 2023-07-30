from sympy import symbols, solve, parse_expr, simplify
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

formula = "6*x**5+10*x**4-120*x**3+48*x**2-24*x+1=0"

def map_operations(formula_str):
    return formula_str.replace("^", "**").replace("=", "-")

f = parse_expr(map_operations(formula), transformations=transformations)
roots = solve(f) # <-- вернуть все корни уравнения в виде списка
print(roots)