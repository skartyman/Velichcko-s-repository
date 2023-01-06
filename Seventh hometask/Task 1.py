'''
Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
    Создать список и поместить туда имя самого молодого человека.
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

min_age = min([i['age'] for i in persons])
min_age_name_list = [i['name'] for i in persons if i['age'] == min_age]
print(min_age_name_list)
