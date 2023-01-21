'''
Реализовать программу(несколько функций) цензор.
Принимает файл с текстом и список слов.
На выходе:
1) новый файл с тем же текстом, но заданные слова заменены на звездочки,
2) файл stat.json(формат данных JSON) со статисткой(обновляемый) в виде:
 название файла, список слов, сколько раз каждое слово встретилось в тесте.
3)файл stat.csv(формат данных csv) со статисткой(обновляемый) в виде:
 название файла, список слов, сколько раз каждое слово встретилось в тесте.
'''
import json
import csv
file = 'Loves.txt'


def censor(file, list) :
    '''Функция 'censor': Принимает в параметры файл и список слов.
    Создает новый файл в который записывает текст из заданного файла, но слова которые поданы в
    списке из условия заменяет на "шаблон"'''
    with open(file, 'r+') as file :
        pattern = '____'
        f = file.read()
        for i in list :
            if i in f :
                f = f.replace(i, pattern)
    with open('file_censored.txt', 'w') as file :
        return file.write(f)

def gen_dict_words_num(file):
    """Функция возвращает словарь ключами которого являютсся слова,
     а значения количество раз, которое слово упоминается в тексте"""
    with open(file, 'r+') as file :
        f = file.read()
        dict_words_num = {}
        for word in f.split() :
            if word not in dict_words_num :
                dict_words_num[word] = 1
            else :
                dict_words_num[word] += 1
        dictionary = dict_words_num
    return dictionary
dictionary = gen_dict_words_num(file)

def stat_json(dictionary) :
    """Функция создает файл статистики в JSON формате, в который записывает словарь полученный из gen_dict_words_num """
    with open('stats.json', 'wt') as file :
        return json.dump(dictionary, file)


def stat_csv(dictionary) :
    """Функция создает файл статистики в СSV формате, в который записывает словарь полученный из gen_dict_words_num """
    with open('stats.csv', 'wt') as file :
        writer = csv.DictWriter(file, fieldnames=dictionary.keys(), delimiter=';')
        writer.writeheader()
        writer.writerow(dictionary)



