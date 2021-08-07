#! /usr/bin/env python3
"""создайте файл с таким содержанием:
"
    some line blablabla you dont need to catch this line try to catch me but not me I'm here, catch me!!!
"
откройте данный файл при помощи контекстного менеджера в режиме чтения и соберите список всех
строк, которые содержат текст "catch me" в один список после чего выведите в консоль количество
найденных в файле строк"""


with open('catch_me.txt', 'r') as file:
    lines = file.readlines()
    res_list = [line for line in lines if "catch me" in line]

print(len(res_list))