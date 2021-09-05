#! /usr/bin/env python3
from math import sqrt
import sys


class Figure:
    def __init__(self, s):
        self.s = s

    def area(self):
        return f'Площадь равна {self.s}'


class Square(Figure):
    def __init__(self, side, s=None):
        super().__init__(s)
        self.side = side

        self.s = side ** 2


class Rectangle(Figure):
    def __init__(self, side_a, side_b, s=None):
        super().__init__(s)
        self.side_a = side_a
        self.side_b = side_b

        self.s = side_a * side_b


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, s=None):
        super().__init__(s)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        p = (side_c + side_b + side_a) / 2
        self.s = sqrt(p * (p - side_c) * (p - side_b) * (p - side_a))


def err_probe(input_string, list_of_len_sides, cls):
    if (input_string == 'triangle' and len(list_of_len_sides) != 3) or \
            (input_string == 'square' and len(list_of_len_sides) != 1) or \
            (input_string == 'rectangle' and len(list_of_len_sides) != 2):
        print('may be you forget some params, or to mach params')
    else:
        try:
            print(cls(*map(int, list_of_len_sides)).area())
        except Exception as e:
            print('something went wrong!')
            pass


if __name__ == '__main__':
    while True:
        print('enter name of figure(square, rectangle, triangle): ')
        step1 = sys.stdin.readline().strip()
        if step1 == 'triangle':
            print('enter the lengths of the sides separated by a space(for triangle 3 sides)')
            sides = sys.stdin.readline().strip().split(' ')
            err_probe(step1, sides, Triangle)
        elif step1 == 'square':
            print('enter the lengths of the side(for square 1 sides)')
            sides = sys.stdin.readline().strip().split(' ')
            err_probe(step1, sides, Square)
        elif step1 == 'rectangle':
            print('enter the lengths of the sides separated by a space(for square 2 sides)')
            sides = sys.stdin.readline().strip().split(' ')
            err_probe(step1, sides, Rectangle)
        else:
            print('I do not understand')
