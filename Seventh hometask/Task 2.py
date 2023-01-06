'''
Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
   Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
'''

persons = [
    {"name": "Andrew", "age": 56},
    {"name": "John", "age": 54},
    {"name": "Jacob", "age": 68},
    {"name": "Corry", "age": 46},
    {"name": "Emily", "age": 45},
    {"name": "Cortney", "age": 45},
    {"name": "Peter", "age": 47}
    ]
max_len_name = max([len(i['name']) for i in persons])
max_len_name_list = [i['name'] for i in persons if len(i['name']) == max_len_name]
print(max_len_name_list)