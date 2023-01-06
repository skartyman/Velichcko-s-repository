'''
Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
   Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
'''
print()
persons = [
    {"name": "Andrew", "age": 56},
    {"name": "John", "age": 54},
    {"name": "Jacob", "age": 68},
    {"name": "Corry", "age": 46},
    {"name": "Emily", "age": 45},
    {"name": "Cortney", "age": 45},
    {"name": "Peter", "age": 47}
    ]
print(' Создать список и поместить туда имя самого молодого человека.')
min_age = min([i['age'] for i in persons])
min_age_name_list = [i['name'] for i in persons if i['age'] == min_age]
print(min_age_name_list)

print()
print('Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.')

max_len_name = max([len(i['name']) for i in persons])
max_len_name_list = [i['name'] for i in persons if len(i['name']) == max_len_name]
print(max_len_name_list)

print()
print('Посчитать среднее количество лет всех людей из начального списка.')
count = 0
for i in persons:
    count += 1
middle_age = sum(i['age'] for i in persons)//count
print(f'Средний возраст всех людей: {middle_age}')


