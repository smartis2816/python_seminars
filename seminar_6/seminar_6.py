
# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

# string = '1 + 2 * 3 + 8 / 2'.split()
# for i in range(len(string)):
#     if string[i].isdigit():
#         string[i] = int(string[i])
# op_1 = {'+': lambda x, y: x + y,
#         '-': lambda x, y: x - y}
# op_2 = {'*': lambda x, y: x * y,
#         '/': lambda x, y: x / y}

# index = 0
# while ('*' in string) or ('/' in string):
#     if string[index] in op_2:
#         temp = op_2[string[index]](string[index - 1], string[index + 1])
#         del string[index - 1:index + 2]
#         string.insert(index - 1, temp)
#         index = 0
#     else:
#         index += 1

# index = 0
# while'+' in string or '-' in string:
#     if string[index] in op_1:
#         temp = op_1[string[index]](string[index - 1], string[index + 1])
#         del string[index - 1:index + 2]
#         string.insert(index - 1, temp)
#         index = 0
#     else:
#         index += 1

# print(string)


# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]
#  что сделать с элементом  / с каким элементом  /  при каком условии
# outcoming_list = [i for i in incoming_list if incoming_list.count(i) == 1]
# print(outcoming_list)

# или так 
# outcoming_list_2 = list(filter(lambda x: incoming_list.count(x) == 1, incoming_list))






# Перевод строк с числами в числа
# a = ['31', '78', '3']
# a = list(map(int, a))
# или так (особенно, если в списке не только числа)
# a = [int(item) for item in a if item.isdigit()]

# Числа превратить в int, а не числа оставить как есть
# a = ['412', '*', '123', '+', '412']
# a = list(map(lambda x: int(x) if x.isdigit() else x, a))
# print(a)









