import random


def task4_sub_task1():
    a = float(input())
    b = float(input())
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print('a = b')


def task4_sub_task2():
    a = float(input())
    if a > 0:
        print('введённое число больше нуля')
    elif a < 0:
        print('введённое число меньше нуля')
    else:
        print('введённое число равно нулю')


def task4_sub_task3():
    valueList = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            valueList[i][j] = int(random.uniform(-10, 10))
    print(valueList)
    summa = 0
    for width in valueList:
        for ind in width:
            if ind > 0:
                summa = summa + ind
    print(summa)
