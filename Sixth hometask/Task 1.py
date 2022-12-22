'''
1. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на четных местах из
my_list_1, а потом все элементы на нечетных местах из my_list_2.
'''

my_list_1 = [i for i in range(54)]
my_list_2 = [i for i in range(54)]
my_result = []
for i in my_list_1[::2]:
        my_result.append(i)
for n in my_list_2[1::2]:
       my_result.append(n)
print(my_result)

#или так

my_result1 = []
for i in my_list_1[::2]:
        my_result1.append(i)
del my_list_2[::2]
my_result1.extend(my_list_2)
print(my_result1)
