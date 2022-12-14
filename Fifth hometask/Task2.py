'''
У вас есть список my_list с значениями типа int, и пустой список my_results.
Добавить в my_results те значения, которые больше 100.
Распечатать список my_results.
Задание выполнить с помощью цикла for.
'''
from random import randint
list_1 = [randint(1,300) for i in range(200)] # генерация списка с рандомными двумя сотнями значений от 1 до 300
list_over_100 = []
for n in list_1:
        if n > 100:
            list_over_100.append(n)
print(list_over_100)

