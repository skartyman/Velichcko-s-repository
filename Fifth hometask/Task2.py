'''
У вас есть список my_list с значениями типа int, и пустой список my_results.
Добавить в my_results те значения, которые больше 100.
Распечатать список my_results.
Задание выполнить с помощью цикла for.
'''
from random import randint
my_list = [randint(1,300) for i in range(200)] # генерация списка с рандомными двумя сотнями значений от 1 до 300
my_results = []
for n in my_list:
        if n > 100:
            my_results.append(n)
print(my_results)

