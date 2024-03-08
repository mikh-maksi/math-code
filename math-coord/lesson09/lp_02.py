import time

from pulp import *

start = time()

problem = pulp.LpProblem("0", pulp.LpMinimize)
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)

problem += 30 * x1 + 30 * x2 + 45 * x3, "Целевая функция"
problem += 0.03 * x1 + 0.01 * x2 - 0.01 * x3 <= 0, "1-е ограничение"
problem += -1.25 * x1 + 0.75 * x2 - 0.25 * x3 <= 0, "2-е ограничение"
problem += x1 + x2 + x3 == 1, "3-е ограничение"
problem.solve()

print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Цена:")
print(value(problem.objective))

stop = time.time()
print("Время:")
print(stop - start)