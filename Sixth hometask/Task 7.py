'''
11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
в строке ТОЛЬКО ОДИН раз.
'''
my_string = 'fgfgfgddddd H jjjjjdddkk L hhdhd'
new_list = []
for i in my_string:
    count1 = my_string.count(i)
    if count1 == 1:
        new_list.extend(i)
print(new_list)