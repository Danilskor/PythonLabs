from Task2 import *
from Task3 import *
from Task4 import *
from Task5 import *

if __name__ == '__main__':
    exit_number = 0
    task_number = int(input('Введите номер задания: '))
    while task_number != exit_number:
        if task_number == 2:
            task2_a()
            task2_b()
        elif task_number == 3:
            task3_sub_task1()
            task3_sub_task2()
            task3_sub_task3()
        elif task_number == 4:
            task4_sub_task1()
            task4_sub_task2()
            task4_sub_task3()
        elif task_number == 5:
            task5_sub_task1()
            task5_sub_task2()
            new_matrix = [[1, 2, 3, 4, 5],
                          [1, 2, 3, 4, 5],
                          [1, 2, 3, 4, 5],
                          [1, 2, 3, 4, 5],
                          [1, 2, 3, 4, 5]]
            task5_sub_task3(new_matrix)
        else:
            print('Номер задания введен неправильно, номер должен дыть от 2 до 5')

        print()
        task_number = int(input('Для выхода нажмите 0 или номер другого задания: '))
