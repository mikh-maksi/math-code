import numpy as np

# Створюємо початкову матрицю 4x12 (наприклад, з нулями)
A = np.zeros((4, 12), dtype=int)

# Створюємо одиничну матрицю 4x4
I = np.eye(4, dtype=int)

# Приписуємо справа → результат матриця 4x16
A_with_I = np.hstack([A, I])

print("Матриця A (4x12):")
print(A)
print("\nОдинична матриця (4x4):")
print(I)
print("\nРезультат (4x16):")
print(A_with_I)
