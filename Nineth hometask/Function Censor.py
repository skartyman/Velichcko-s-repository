'''
Написать функцию цензор. На вход функция получает имя файла и список слов для замены,
функция ничего не возвращает, но в результате ее работы необходимо создать файл,
в котором слова из списка заменены шаблоном(звездочками например)
'''
list = ['love', 'short', 'stories', 'Love', 'Stories', 'Short', 'still', 'the']
file = 'Loves.txt'
def censor(file, list):
    '''Функция 'censor': Принимает в параметры файл и список слов.
    Создает новый файл в который записывает текст из заданного файла, но слова которые поданы в
    списке из условия заменяет на "шаблон"'''
    with open(file, 'r+') as file:
        pattern = '____'
        f = file.read()
        for i in list:
            if i in f:
                f = f.replace(i, pattern)
    with open('file_censored.txt', 'w') as file:
        return file.write(f)






