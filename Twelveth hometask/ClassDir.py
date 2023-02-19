'''
1. Инициализация класса с одним параметром - имя директории.
2. Написать метод класса, который создает атрибут класса в ввиде словаря
{'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
{'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
2. Написать метод класса, которая получает булевое значение (True/False).
Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
3. Написать метод класса, которая получает строку, которая может быть
или именем файла, или именем папки. (В имени файла должна быть точка).
В зависимости от того, что функция получила (имя файла или имя папки) - записать его
в соответствующий список и вернуть обновленный словарь.

'''

import os


class Directory:
    def __init__(self, dir_path):
        '''Конструктор класса.

        :param dir_path: Путь до директории.
        '''
        self.dir_path = dir_path

    def get_filesystem_dict(self):
        '''Метод для получения словаря с файлами и папками текущей директории.

        :return: Словарь, содержащий имена файлов папок текущей директории.
        '''
        items = os.listdir(self.dir_path)
        filenames = [item for item in items if os.path.isfile(os.path.join(self.dir_path, item))]
        dirnames = [item for item in items if os.path.isdir(os.path.join(self.dir_path, item))]
        filesystem_dict = {'filenames': filenames, 'dirnames': dirnames}
        return filesystem_dict

    def sorted_files_and_dirs(self, reverse=False):
        '''Метод для проверки, отсортированы ли имена файлов и директорий по возрастанию или убыванию.

        :param reverse: Флаг, указывающий направление сортировки. По умолчанию - False (сортировка по возрастанию).
        :return: True, если имена файлов и директорий отсортированы по возрастанию , False - в противном случае.
        '''
        sorted_files = sorted(self.get_filesystem_dict()['filenames'], reverse=reverse)
        sorted_dirs = sorted(self.get_filesystem_dict()['dirnames'], reverse=reverse)
        return not (not (sorted_files == self.get_filesystem_dict()['filenames']) or not (
                    sorted_dirs == self.get_filesystem_dict()['dirnames']))

    def add_to_dict(self, string):
        '''Метод для проверки строки, которую он получает на вход,
         если точка в имени то это файл, если нет то это папка.

        :param string: Строка: имя файла или папки.
        :return: Словарь, с добавленным значением к ключам из строки в соответствии с проверкой.
        '''
        filesystem_dict = self.get_filesystem_dict()
        if '.' in string:
            filesystem_dict['filenames'].append(string)
        else:
            filesystem_dict['dirnames'].append(string)
        return filesystem_dict
