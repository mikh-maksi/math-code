from pulp import LpMaximize, LpProblem, LpStatus, LpVariable

import matplotlib.pyplot as plt


# Create the maximization problem
model = LpProblem(name='Field Problem', sense=LpMaximize)
# Initialize the variables
x = LpVariable(name="x", lowBound=0, upBound=100)
y = LpVariable(name="y", lowBound=0, upBound=100)
x = LpVariable(name="x", lowBound=20, upBound=50)


# Add the constraints to the model. Use += to append expressions to the model
model += (x <= 95, "margin_X") #it cannot go past the fence
model += (y <= 95, "margin_Y")


# Objective Function
obj_func = x + y
# Add Objective function to the model
model += obj_func

status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
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
plt.plot([0,x.value()], [0,y.value()], c='red')
# Plot MAX POINT
plt.scatter(x.value(),y.value(), c='red')
# Plot Fence 1
plt.vlines(95, 0,100, linestyles='--', colors='red')
# Plot Fence 2
plt.hlines(95, 0,100, linestyles='--', colors='red')
# Annotations
plt.annotate(f'Optimal Value: {x.value(), y.value()} --->', xy=(47, 96));


plt.show()