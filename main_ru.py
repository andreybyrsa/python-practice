from math import sqrt
from collections import Counter

#часть таблицы юникода с ключами - остатками от деления на сс 
unicode = {10: 'a', 11: 'b', 12: 'c' , 13: 'd' , 14: 'e' , 15: 'f' , 16: 'g' , 17: 'h', \
    18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', \
    27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}

#функция
def get_number_of_base(number):
    num_base = ''
    while number > 0:
        #проверка на соответствие ключа таблицы и остатка
        try:
            num_base = unicode[number % base] + num_base
        except:
            num_base = str(number % base) + num_base
        number = number // base
    return num_base

def check_int():
    while True:
        #проверка корректности ввода чилса: число / другой тип данных 
        try:
            number = int(input())
            if number < float('inf'):
                break
        except:
            print('Вероятно, Вы ввели не число, попробуйте еще раз:')
    return int(number)

def print_number_1():
    print('Введите первое число:')
    number_1 = check_int()
    return number_1 

def print_number_2():
    print('Введите первое число:')
    number_2 = check_int()
    return number_2

def print_base():
    stroka = 'Число ' + str(number) + ' в системе счисления с основанием ' + str(base) + \
        ' = ' + str(number)
    return stroka
#бесконечный цикл с командой выхода 
while True:
    print('Что Вы хотите сделать: \n (1) открыть калькулятор; \n (2) свойства числа; \n (3) перевод в сс; \n (4) выход.')
    main_moving = check_int()
    if main_moving == 1:
        #бесконечный цикл с командой выхода 
        while True:
            print('Действия с двумя числами: \n (1) + \n (2) - \n (3) * \n (4) / \n (5) ^ \n (6) выход')
            move = check_int()
            if move == 1:
                number_1 = print_number_1()
                number_2 = print_number_2()
                print(number_1 + number_2)
            elif move == 2:
                number_1 = print_number_1()
                number_2 = print_number_2()
                print(number_1 - number_2)
            elif move == 3:
                number_1 = print_number_1()
                number_2 = print_number_2()
                print(number_1 * number_2)
            elif move == 4:
                number_1 = print_number_1()
                number_2 = print_number_2()
                print('Вид деления: \n (1) обычное; \n (2) целочисленное.')
                division = int(input())
                if division == 1:
                    print(number_1 / number_2)
                if division == 2:
                    print(number_1 // number_2)
            elif move == 5:
                number_1 = print_number_1()
                print('Степень числа')
                number_move = int(input())
                print(number_1 ** number_move)
            elif move == 6:
                break
            else:
                print('Введена неверная команда, попробуйте снова')

    elif main_moving == 2:
        print('Введите целое число:')
        number = check_int()
        #массив с полной информацией об введенном числе 
        number_analytic = list()

        if number % 2 == 0:
            number_analytic.append('четное')
        else:
            number_analytic.append('нечетное')
        if number > 0:
            number_analytic.append('натуральное, положительное')
        else:
            number_analytic.append('натуральное, отрицательное')
            
        dividers = set()
        #множество для неповторяющихся делителей в случае квадрата числа
        #поиск делителей через обратные делитель, пример 36 -> 1 / 36; 2 / 18; 3 / 12; 4 / 9; 6 / 6
        for divider in range(1, int(sqrt(number)) + 1):
            if number % divider == 0:
                dividers.add(divider)
                dividers.add(number // divider)
        if len(dividers) == 2:
            number_analytic.append('простое число')
        else:
            number_analytic.append(str('количество делителй числа = ' + str(len(dividers))))
        
        dividers = list(sorted(dividers))
        string_of_dividers = str(dividers[0])
        for index in range(1, len(dividers)):
            string_of_dividers += ', ' + str(dividers[index])
        number_analytic.append('делители числа: ' + string_of_dividers)

        #цикл for = функции map() - ход по каждому символу
        number_analytic.append('суммы цифр с числе = ' + str(sum(map(int, str(number)))))
        number_analytic.append('количество цифр в числе = ' + str(len(str(number))))
        most_common_char = Counter(str(number)).most_common()
        number_analytic.append('распределение цифр в числе - '+ str(most_common_char))

        print('Свойства числа:')
        counter = 1
        for info in number_analytic:
            print('(' + str(counter) + ') ' + str(info))
            counter += 1
            
    elif main_moving == 3:
        print('Введите число:')
        number = check_int()
        print('Введите основание сс:')
        base = check_int()

        if base == 2:
            number = bin(number)[2:]
            print(print_base())
        elif base == 8:
            number = oct(number)[2:]
            print(print_base())
        elif base == 16:
            number = hex(number)[2:]
            print(print_base())
        else:
            number = get_number_of_base(number)
            print(print_base())

    elif main_moving == 4:
        #остановка всего скрипта
        exit()

    else:
        print('Введена неверная команда, попробуйте снова')
