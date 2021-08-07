#! /usr/bin/env python3
"""Дан список из словарей:
list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]
Отфильтруйте его так, чтобы в нём остались только люди, имена которых
начинаются с буквы "А", и возраст между 18 и 30 годами включительно.
В итоговом результате должен быть такой список:
[{'name': 'Alex', 'age': 25}]"""


list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]

result = [d for d in list_ if d['name'].startswith("A") and (18 <= d['age'] <= 30)]
result2 = list(filter(lambda d: d['name'].startswith("A") and (18 <= d['age'] <= 30), list_))

print(result, result2)