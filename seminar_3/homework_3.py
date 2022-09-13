
# Задача 1
# Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# new_list = []
# def fill_list(new_list):
#     temp_list = input('Введите несколько чисел через пробел: ').split()
#     for i in range(0, len(temp_list)):
#         new_list.append(int(temp_list[i]))
#     return new_list
       
# print(fill_list(new_list))

# def find_sum(new_list):
#     sum = 0
#     for i in range (1, len(new_list), 2):
#         sum += new_list[i]
#     return sum

# print(f'Сумма элементов, стоящих на нечётных позициях - {find_sum(new_list)}')

# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def fill_list_2():
#     my_list = [int(item) for item in (input('Введите числа через пробел: ').split())]
#     print(my_list)
#     return my_list

# def product_of_numbers(list):
#     result = 1
#     i, j = 0, (len(list) - 1)
#     while i <= j:
#         result = list[i] * list[j]
#         i += 1
#         j -= 1
#         print(result)

# new_list = fill_list_2()
# product_of_numbers(new_list)

# Задача 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# original_list = [1.1, 1.2, 3.1, 10.01]

# def fill_list_3():
#     my_list = [float(item) for item in (input('Введите дробные числа через пробел: ').split())]
#     print(f'Оригинальный список - {my_list}')
#     return my_list

# def select_fractional_part (list):
#     for i in range (0, len(list)):
#         list[i] = list[i] % 1
#         list[i] = round(list[i], 2)
#     print(f'Список с выделенными дробными частями - {list}')
#     return list

# def difference_max_min (list):
#     list.sort()
#     print(f'Отсортированный список - {list}')
#     res = list[-1] - list[0]
#     print(f'Разница между максимальным и минимальным значением дробной части - {res}')
#     return res

# original_list = fill_list_3()
# original_list = select_fractional_part(original_list)
# difference_max_min(original_list)

# Задача 4
# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Введите целое число: '))

# def decimal_to_binary(num):
#     new_str = ''
#     while num > 0:
#         new_str = str(num % 2) + new_str
#         num = num // 2
#     print(new_str)
#     return int(new_str)

# decimal_to_binary(num)

# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_fibonacci(k):
    if k >= 1:
        f1 = 1
        f2 = 1
        new_list_1 = [1, 1]
        for i in range(2, k):
            f1, f2 = f2, (f1 + f2)
            new_list_1.append(f2)
    
        new_list_2 = new_list_1.copy()
        for i in range(1, len(new_list_2), 2):
            new_list_2[i] *= (-1)
        new_list_2.reverse()
        new_list_2.append(0)
        res = new_list_2 + new_list_1
        print(res)
    elif k == 0:
        res = [0]
        print(res)

k = int(input('Введите натуральное число: '))
get_fibonacci(k)





