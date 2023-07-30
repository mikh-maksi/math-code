# Импортируем оболочку OR-Tools для линейного программирования
from ortools.linear_solver import pywraplp

# Создаем решатель с помощью бэкенда GLOP
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

solver.Maximize(swordsmen*70 + bowmen*95 + horsemen*230)
solver.Add()
status = solver.Solve()


if status == pywraplp.Solver.OPTIMAL:
  print('================= Solution =================')
  print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
  print()
  print(f'Optimal power = {solver.Objective().Value()} 💪power')
  print('Army:')
  print(f' - 🗡️Swordsmen = {swordsmen.solution_value()}')
  print(f' - 🏹Bowmen = {bowmen.solution_value()}')
  print(f' - 🐎Horsemen = {horsemen.solution_value()}')
else:
  print('The solver could not find an optimal solution.')