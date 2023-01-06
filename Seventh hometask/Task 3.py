'''
Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
   Посчитать среднее количество лет всех людей из начального списка.
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
count = 0
for i in persons:
    count += 1
middle_age = sum(i['age'] for i in persons)//count
print(f'Средний возраст всех людей: {middle_age}')
