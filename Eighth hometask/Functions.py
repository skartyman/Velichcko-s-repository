'''
Функции в отдельном модуле, проверка работоспособности в main
'''
import random
from string import ascii_lowercase

'''
Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
'''
my_list = ['лицо','картон','песок','нога','мотор','аренда','акваланг',]
my_list1 = ['лицо','картон','песок','нога','мотор','аренда','акваланг', 78, 68, 98, 987987]
my_str = "AspdnieoJmoedj, uidha, efsdfihskefnneo  jdkismkso 1 3 kdbn"
my_str1 = 'ndoadnalskd,d qdAiqd, qedoiqhwdkqhqwdhiw, hnjiknsdik'
names = ['Brown','Martinez', 'Jenkins', 'Paul','King','Walker','Marshall','Lewis','Henry','Cole']
domains = ['ru','ua','org','com','net','doc','io','su','ar','eu','fr','de','us','uk']

def turner(my_list):
    '''Функция возвращает новый список в котором элементы с нечетным индексом обернуты.'''
    new_list = []
    for i in my_list :
        if i in my_list[1::2]:
            new_list.append(i)
        else:
            new_list.append(i[::-1])
    print(new_list)
    return (new_list)


'''
Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
'''


def a_list(my_list):
    '''Функция возвращает новый список, слова в котором начинаются на "a".'''
    new_list = []
    for i in my_list:
        if i[0] == 'а':
            new_list.append(i)
    print(new_list)
    return (new_list)


'''
Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
'''


def a_random_list(my_list):
    '''Функция возвращает новый список со словами в которых встречается буква "а".'''
    new_list = []
    for i in my_list:
        if "а" in i:
            new_list.append(i)
    print(new_list)
    return (new_list)


'''
Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.
'''


def str_list(my_list):
    '''Функция возвращает новый список только с элементами типа "str".'''
    new_list = []
    for i in my_list:
        if isinstance(i, str):
            new_list.append(i)
    print(new_list)
    return (new_list)


'''
Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.
'''


def uniq_symbols(my_str):
    '''Функция возвращает новый список в котором содержаться уникальные символы из my_str.'''
    new_list = []
    for i in my_str:
        if my_str.count(i) == 1:
            new_list.append(i)
    print(new_list)
    return (new_list)


'''
Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
'''


def symbols_in_both_str(my_str, my_str1):
    '''Функция возвращает список содержащий символы, которые есть в обеих строках хотя бы раз.'''
    new_list = []
    # for i in my_str:
    #     if i in my_str1:
    #         new_list.append(i)
    #     new_list = list(set(new_list))
    new_list = list(set(my_str) & set(my_str1))
    print(new_list)
    return (new_list)


'''
Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
'''


def uniq_symbols_for_both_str(my_str, my_str1):
    '''Функция возвращает список в который добавляет только символы, которые есть в обеих строках,
     только по одному разу.'''
    new_list = []
    new_list1 = []
    for i in my_str:
        if my_str.count(i) == 1:
            new_list.append(i)
    for i in my_str1 :
        if my_str1.count(i) == 1:
            new_list1.append(i)
    new_list = list(set(new_list) & set(new_list1))
    print(new_list)
    return (new_list)


'''
Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
'''


def mail_generator(names, domains):
    '''Функция генерирует e-mail адрес в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерирует случайным образом.
'''
    # name = random.choice(names)
    # domain = random.choice(domains)
    # number = str(random.randint(100, 1000))
    # random_str = ''.join(random.choice(ascii_lowercase) for i in range(random.randint(3, 8)))
    # # e_mail = f'{name}.{number}@{random_str}.{domain}'
    e_mail = random.choice(names) + '.' + str(random.randint(100, 1000)) + '@' + ''.join \
        (random.choice(ascii_lowercase) for i in range(random.randint(3, 7))) +'.'+ random.choice(domains)
    print(e_mail)
