from math import *


# Вариант 1

def task2_a():
    m = -14 / 15
    n = tan(pi / 8)
    expression = 3 * m ** 2 + pow(2 * n ** 2, 1 / 3 / m)
    print('m =', m, 'n =', n, 'Результат =', expression)


def task2_b():
    print('Введите m')
    m = float(input())
    print('Введите n')
    n = float(input())
    expression = 3 * m ** 2 + pow(2 * n ** 2, 1 / 3 / m)
    print('m =', m, 'n =', n, 'Результат =', expression)
