import random

print("Охват".ljust(10), "Кількість лідів:".ljust(20), "Кількість продажів".ljust(20))
for i in range(10):
    N = random.randint(45264, 72456)
    A = random.uniform(0.09491942092, 0.09999116296)
    B = random.uniform(0.7601226994,0.9502872293)
    C = random.uniform(0.8846487424,0.9830508475)
    D = random.uniform(0.4831691297,0.5422179456)
    E = random.uniform(0.153593579,0.1594882729)
    F = random.uniform(0.2032193159,0.5401069519)
    S = N * A* B*C*D*E*F
    print(f"{'%.0f' %N:10} {'%.0f'%(N*A):15} {'%.0f'%S:15}")

