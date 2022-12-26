'''
11. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках, но в каждой
 ТОЛЬКО ПО ОДНОМУ разу. Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
  т.к. эти символы есть в каждой строке по одному разу
'''
my_string_1 = 'guyghi8b iu8hiuh oi8y8rgpj8'
my_string_2 = 'ouihjnmn jloiyhiyfggohbi  iuguiyrfgh89'
new_list = []
new_list1 = []
for i in my_string_1:
    count1 = my_string_1.count(i)
    if count1 == 1:
        new_list.extend(i)
for i in my_string_2:
    count2 = my_string_2.count(i)
    if count2 == 1:
        new_list1.append(i)
result=list(set(new_list) & set(new_list1))
print(new_list)
print(new_list1)
print(result)
