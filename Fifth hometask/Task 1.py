'''
У вас есть список my_list с значениями типа int.
Распечатать те значения, которые больше 100.
Задание выполнить с помощью цикла for.
'''

from random import randint
my_list = [randint(1,300) for i in range(200)] # генерация списка с рандомными двумясотнями значений от 1 до 300
for n in my_list:
        if n > 100:
            print(n,end=' ')

