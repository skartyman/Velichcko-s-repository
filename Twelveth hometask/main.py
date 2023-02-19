from ClassDir import Directory

# Создаем экземпляр класса Directory
directory = Directory(r'C:\Users\Сергей\PycharmProjects\Velichcko-s-repository')

# Получаем словарь файловой системы и выводим в консоль
filesystem_dict = directory.get_filesystem_dict()
print(filesystem_dict)

# Выводим информацию о сортировке если Тrue сортировка по алфавиту.
print(directory.sorted_files_and_dirs())

# Добавляем строку в соответствующие списки в словаре и выводим обновленный словарь.
print(directory.add_to_dict('new_file.txt'))


