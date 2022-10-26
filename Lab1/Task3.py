def task3_sub_task1():
    print('Веедите ваше имя')
    name = input()
    print('Введите количество полных лет')
    years = int(input())
    print('Введите образовательное учереждение, в котором вы учитесь')
    educationalInstitution = input()
    print('Ваc зовут ', name, '.', ' Вам ', years, ' лет и Вы учитесь в ', educationalInstitution, 'е.', sep='')


def task3_sub_task2():
    str1 = 'Введите ваше имя'
    str2 = 'Введите количество полных лет'
    str3 = 'Введите образовательное учереждение, в котором вы учитесь'
    str4 = 'Дадая'

    concat = str1 + str2
    print('concat =', concat)
    repeat = str4 * 3
    print('repeat =', repeat)
    index = str1[1]
    print('index =', index)
    slice = str1[1:8:3]
    print('slice =', slice)
    length = len(str3)
    print('length =', length)
    counts = repeat.count('д', 0, len(repeat) - 5)
    print('counts =', counts)
    subSearch = str1.find('ваше')
    print('subsearch', subSearch)
    split = str1.split(' ')
    print(split)
    upper = str4.upper()
    lower = str4.lower()
    print('upper:', upper, 'lower:', lower)


def task3_sub_task3():
    str = 'Емеля ехал ельником, егозил, ехидничал.'
    split = str.split(' ')
    count = 0
    for word in split:
        a = word[0]
        if word[0] == 'е' or word[0] == 'Е':
            count = count + 1
    print('В предложении:', str, count, 'букв на букву \"е\"')
task3_sub_task3()
