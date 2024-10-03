

import os, time
#import time
#dirpath - это строка, путь к каталогу.
#os.listdir() - список файлов в директории/каталоге,
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')
        print('The root is:', root)

# Функция os.walk('dirname') возвращает генератор, который производит кортежи,
# содержащие информацию о каждой директории в директории dirname, включая её поддиректории.
# Каждый кортеж состоит из трёх элементов:
# Строка с именем текущей директории.
# Список с именами поддиректорий в текущей директории.
# Список с именами файлов в текущей директории.
#
# walk(), возвращающий имена файлов в дереве каталогов, двигаясь по дереву сверху вниз или снизу вверх
# (сверху вниз по умолчанию).