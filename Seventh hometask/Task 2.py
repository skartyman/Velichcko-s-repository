'''
Даны два словаря my_dict_1 и my_dict_2
'''


my_dict_1 = {4: 7, 6: 6, 7: 54, 8: 4, 9: 5 }
my_dict_2 = {5: 3, 7: 5, 6: 3, 4: 2, 8: 4}
print()
print('Создать список из ключей, которые есть в обоих словарях.')

keys_list = list(my_dict_1.keys() & (my_dict_2.keys()))
print(keys_list)
print()
print('Создать список из ключей, которые есть в первом, но нет во втором словаре.')

keys_list_1 = list(my_dict_1.keys())
keys_list_2 = list(my_dict_2.keys())
new_list = [i for i in keys_list_1 if not i in keys_list_2]
print(new_list)
print()
print('Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.')

items_list_1 = list(my_dict_1.items())
items_list_2 = list(my_dict_2.items())
new_dict = dict(i for i in items_list_1 if not i in items_list_2)
print(new_dict)
print()
print("Объединить эти два словаря в новый словарь по правилу: \n"
      " если ключ есть только в одном из двух словарей - поместить пару ключ:значение, \n"
      " если ключ есть в двух словарях -\n"
      " поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},\n"
      "{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}')")
print()

for key in my_dict_2.keys():
      if key in my_dict_1:
            my_dict_1[key] = list((my_dict_1[key],my_dict_2[key]))
      else:
            my_dict_1.update({key: my_dict_2[key]})
new_dict = my_dict_1
print(new_dict)