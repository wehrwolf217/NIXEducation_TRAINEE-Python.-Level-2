#! /usr/bin/env python3
"""Напишите функцию, которая делает return строки приветствия людей из разных стран на разных
языках, в зависимости от страны человека.
Вызовите функцию используя map
Требование: используйте map
Для примера можете взять этот список юзеров:
users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]
На выходе с использованием users_list, после использования map вы должны получить результат
iterable с такими приветствиями:
Привет, Александр!
Hello, James!
Hola, Daniella!
Hello, Someone, but I do not know where are you from!"""

users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Someone', 'unknown country'),
    ('Daniella', 'es'),
]


def hello(user_tuple):
    languages = {'ru': f'Привет, {user_tuple[0]}!',
                 'us': f'Hello, {user_tuple[0]}!',
                 'es': f'Hola, {user_tuple[0]}!', }
    try:
        return languages[user_tuple[1]]
    except KeyError:
        return f'Hello, {user_tuple[0]}, but I do not know where are you from!'


print('\n'.join(map(hello, users_list)))
