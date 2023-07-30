# Модуль scipy.integrate містить функції для чисельного інтегрування [11, 14, 25, 31, 53], у тому числі для інтегрування звичайних диференціальних рівнянь. У прикладі дано функцію  . Розраховується визначений інтеграл .
# https://vkopey.github.io/Python-for-engineers-and-scientists/#_Toc13763957
import numpy as np
from scipy.integrate import quad
f = lambda x,a: x**a # функція
print (quad(f, -3, 3, args=(2,))) # результат інтегрування і оцінка абсолютної похибки результату
x=np.array([-3,-2,-1,0,1,2,3])
print (np.trapz(f(x,2),x)) # інтегрувати задану масивом функцію методом трапецій