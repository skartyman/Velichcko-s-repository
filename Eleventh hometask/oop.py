'''
1. Создать класс Employee содержащий следуюущие свойства:
    'firstname': 'Ivasik',
    'lastname': 'Telesik',
    'age': 13,
    'e-mail': 'ivasik-telesik1732@izkurnanog.ua',
    'skills': ['ходить', "говорить", "кодить"],
    'people_lang': ['Україньська', "Англійська"],
    'coding_lang': ['Python', "C++", "lisp"],
методы добавить на свое усмотрение(удобство нужно)
добавить метод записи данных сотрудника в файл(JSON/CSV)

'''
import csv
import json


class Employee :
    '''Объявление класса "Employee".'''
    def __init__(self) :
        '''Перегрузка инициализации класса Employee. При объявлении класса
        определяем свойства класса. И печатаем в консоль строку, которая сообщает об успешном
        создании персонажа.'''
        self.firstname = 'Ivasik'
        self.lastname = 'Telesik'
        self.age = 13
        self.email = 'ivasik-telesik1732@izkurnanog.ua'
        self.skills = ['ходить', "говорить", "кодить"]
        self.people_lang = ['Україньська', "Англійська"]
        self.coding_lang = ['Python', "C++", "lisp"]
        print('На ваших глазах рождается новый персонаж со всеми вытекающими из этого последствиями.')

    def data_in_json(self) :
        '''Создание обновляемого файла в формате JSON. В который записываем свойства с их значениями.'''
        with open('Employee.json', 'at') as file :
            json.dump(self.__dict__, file)
        return

    def data_in_csv(self) :
        '''Создание обновляемого файла в формате CSV. В который записываем свойства с их значениями.'''
        with open('Employee.csv', 'at') as file :
            writer = csv.DictWriter(file, fieldnames=self.__dict__.keys(), delimiter=';')
            writer.writeheader()
            writer.writerow(self.__dict__)
        return

    def info(self) :
        '''Метод ИНФО передает информацию о персонаже используя стандартные свойства класса.
        Имя, фамилия,возраст и языки на которых разговаривает и программирует'''
        print(f'Так вот: этого персонажа зовут {self.firstname} {self.lastname}, ему {self.age} лет от роду.'
              f' Он знает два языка: {self.people_lang} и он знает несколько языков программирования, '
              f'а именно: {self.coding_lang}. Вот такой вот персонаж')

    def walk(self) :
        '''Метод передает информацию об определенной способности персонажа. В данном случае (ходьба)'''
        print(f"Этот персонаж еще умеет {self.skills[0]}. Для этого ему приходится переставлять ноги по очереди."
              f" Сначала левую, затем правую, ну или наоборот, это уже не так важно.")

    def add_employee_to_file(self) :
        '''Метод записывает в текстовый обновляемый файл все свойства со значениями класса. '''
        with open('Employee.txt', 'at') as file :
            file.write(str(self.__dict__))
        return
