from math import *

import matplotlib.pyplot as plt
import numpy as np


def function(x_values):
    yValues = exp(-x_values) / (sqrt(exp(-x_values) + 1)) - 1
    return yValues


def function_graf(x_values):
    y_values = []
    for x in x_values:
        y_values.append(function(x))
    plt.plot(x_values, y_values)
    plt.show()


def lambda_function_graf(x_values, lambda_function):
    y = list(map(lambda_function, x_values))
    plt.plot(x_values, y)
    plt.show()


def task5_sub_task1():
    y_function = lambda x: \
        exp(-x) / (sqrt(exp(-x) + 1)) - 1

    x0 = 5.5
    y1 = function(x0)
    y2 = y_function(x0)
    print(y1)
    print(y2)

    x = np.array(range(0, 10))
    lambda_function_graf(x, y_function)
    function_graf(x)


def task5_sub_task2():
    while True:
        print('Введите целое число >= 2')
        input_value = int(input())
        if input_value > 2:
            break
    divider = 2
    while input_value % divider > 0:
        divider = divider + 1
    print('Наименьший делитель =', divider)


def task5_sub_task3(matrix):
    trance_matrix = [[0 for j in range(len(matrix))] for i in range (len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            trance_matrix[j][i] = matrix[i][j]
    return trance_matrix


new_matrix = [[1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5]]
a = task5_sub_task3(new_matrix)
