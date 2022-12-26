'''
*5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
Пересоздавать список нельзя! (используйте метод pop)
'''
from random import randint
my_list = [randint(1,5) for i in range(4)]
print(my_list)
my_list.append(my_list.pop(0))
print(my_list)
