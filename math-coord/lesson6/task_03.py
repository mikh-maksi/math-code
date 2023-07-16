from scipy.optimize import linprog
obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Коефійієнт для y
#       └────┤ Коефійієнт для x

lhs_ineq = [[ 2,  1],  # ліва сторона (1)
            [-4,  5],  # ліва сторона (2)
            [ 1, -2]]  # ліва сторона (3)

rhs_ineq = [20,  # права сторона (1)
            10,  # права сторона (2)
             2]  # права сторона (3)

lhs_eq = [[-1, 5]]  # ліва сторона зеленого равенства
rhs_eq = [15]       # права сторона зеленого равенства

    
bnd = [(0, float("inf")),  # Границі x
       (0, float("inf"))]  # Границі y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
              method="revised simplex")
print(opt)