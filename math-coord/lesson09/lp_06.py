from pulp import LpMaximize, LpProblem, LpStatus, LpVariable

import matplotlib.pyplot as plt


# Create the maximization problem
# name - Ім'я проблеми, sense - напрямок оптимізації LpMinimize | LpMaximize
model = LpProblem(name='Field Problem', sense=LpMaximize)

# Initialize the variables
x = LpVariable(name="x", lowBound=0, upBound=40)
y = LpVariable(name="y", lowBound=0, upBound=40)
x = LpVariable(name="x", lowBound=20, upBound=50)


# Додайте обмеження до моделі. Використовуйте +=, щоб додати вирази до моделі
model += (x <= 40, "margin_X") #it cannot go past the fence
model += (y <= 40, "margin_Y")
model += (x >= 10, "margin_Y2")


# Цільова функція
obj_func = x + y*5
# Додати функцію Objective до моделі
model += obj_func

status = model.solve()

# print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

# The field solution plot
# Create a plot space
plt.figure(figsize=(8,8))
# Dimensions of the field.
xlimits=[0,100,0,100]
ylimits=[0,0,100,100]
# Plot field
plt.scatter(xlimits,ylimits)
# Plot line SOLUTION
plt.plot([0,x.value()], [0,y.value()], c='green')
# Plot MAX POINT
plt.scatter(x.value(),y.value(), c='yellow')
# Plot Fence 1
plt.vlines(50, 0,100, linestyles='--', colors='red')
# Plot Fence 2
plt.hlines(40, 0,100, linestyles='--', colors='red')
# Annotations
plt.annotate(f'Optimal Value: {x.value(), y.value()} --->', xy=(40  , 40));


plt.show()