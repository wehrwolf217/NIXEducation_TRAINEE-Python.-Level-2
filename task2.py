#! /usr/bin/env python3
"""Дан список из словарей в формате [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]
Отсортируйте список по возрасту людей, чтобы получилось [{'name': 'Vasya', 'age': 19}, {'name': 'Oleg', 'age': 23}]
Используйте sorted и lambda"""

data = [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]
sorted_data = sorted(data, key=lambda k: k['age'])
