#! /usr/bin/env python3
"""создайте функцию-генератор, которая принимает на вход два числа, первое - старт, второе - end.
генератор в каждом цикле должен возвращать число и увеличивать его на 1
при итерации генератор должен начать с числа start и закончить итерации на числе end
т.е. при вызове
    for i in my_generator(1, 3):
        print(i)
в консоли должно быть:
1
2
3"""


def my_generator(start, end):
    while start <= end:
        yield start
        start += 1


for i in my_generator(1, 3):
    print(i)
