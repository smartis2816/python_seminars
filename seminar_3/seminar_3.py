
# 1. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.



# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# Первый вариант
# listt = ["65h34q", "sdg634d", "147jnbv"]

# result = [i for i in listt if '147' in i]
# print(result)
# if len(result) > 0:
#     print(True)
# else:
#     print(False)

# Второй вариант
# my_list = ["65h34q", "sdg634d", "147jnbv"]
# n = '7'
# for i in my_list:
#     if i.find(n) > 0:
#         print(i)

# 3. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
# myList = ["1", "qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# myString = '5'
# count = 0

# for i in range(0, len(myList)):
#     if myList[i] == myString:
#         count += 1
#     if count == 2:
#         print(i)
#         break
#     if count < 2:
#         print("False")

