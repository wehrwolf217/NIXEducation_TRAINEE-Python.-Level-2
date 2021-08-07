#! /usr/bin/env python3

"""создайте тестовую директорию с несколькими файлами разных названий
при помощи модуля os создайте функцию для очистки директории от файлов определённого расширения,
принимающую на вход:
путь к директории, где нужно удалить файлы
строку - формат файла, по которой будет определяться, нужно ли удалять файл
пример вызова:
delete_files_func(path='/path/to/folder', file_extension='.txt')
после удаления файлов функция должна вернуть список названий всех удалённых файлов

результат - в директории /path/to/folder удалены все файлы, расширение которых == .txt"""

import os


def delete_files(dir_path, extension):
    deleted_list = []
    for paths, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(extension):
                path_to_file = os.path.join(paths, file)
                deleted_list.append(file)
                os.remove(path_to_file)
            else:
                continue
    return print(f'результат - в директории {dir_path} удалены все файлы, '
                 f'расширение которых == {extension}\n' + '\n'.join(deleted_list))


path = '/home/master/nix_edu_trainee/for_task12'
file_extension = '.txt'

delete_files(path, file_extension)
