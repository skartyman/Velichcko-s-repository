'''
2. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
 Если my_list [1,2,3,4], то new_list [2,3,4,1]
'''
from random import randint
my_list = [randint(1,5) for i in range(4)]
print(my_list)
new_list = []
for i in my_list:
    new_list.append(i)
new_list.append(new_list.pop(0))
print(new_list)
