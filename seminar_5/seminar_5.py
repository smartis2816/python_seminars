
# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5
from ast import comprehension


# with open('Exercise_01.txt', 'r') as f:
#     string = f.readline()

# string = string.split(' ')
# string = list(map(int, string))

# Классический вариант
# for i in range(1, len(string)):
#     if string[i] - 1 != string[i - 1]:
#         print(f'Missed: {string[i] - 1}')
#     break
# else:
#     print('Goog')

# Вариант с list comprehension
# result = [(string[i] - 1) for i in range(1, len(string)) if string[i] - 1 != string[i - 1]]
# print(result)


# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = ([my_list[i] for i in range(1, len(my_list)) if my_list[i] >= max(my_list[0:i])])
# new_list.insert(0, my_list[0])
# print(new_list)

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

# text = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'

# list1 = text.split(' ')
# print(list1)

# list2 = [item for item in list1 if text_find not in item]
# print(list2)

