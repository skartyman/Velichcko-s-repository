'''
2. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
 Если my_list [1,2,3,4], то new_list [2,3,4,1]
'''
my_list = [i for i in range(20)]
new_list = []
for n in my_list[::-1]:
    new_list.append(n)
print(my_list)
print(new_list)