#! /usr/bin/env python3
"""Создайте несколько классов: Animal (абстрактный класс), Cat, Dog
Создайте абстрактные методы say, run и jump в классе Animal (abc.abstractmethod)
Реализуйте полиморфизм поведения животных для методов: say, run, jump"""
import abc
from abc import ABC


class Animal(ABC):
    """abstract class"""

    def __init__(self):
        if type(self) is Animal:
            raise Exception('Animal is an abstract class and cannot be instantiated directly')

    @abc.abstractmethod
    def say(self):
        return 'abs method say'

    @abc.abstractmethod
    def run(self):
        return 'abs method run'

    @abc.abstractmethod
    def jump(self):
        return 'abs method jump'


class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def say(self):
        return 'Meow'

    def run(self):
        return f'Cat {self.name} is running'

    def jump(self):
        return f'Cat {self.name} is jumping'


class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def say(self):
        return 'Woof!'

    def run(self):
        return f'Dog {self.name} is running'

    def jump(self):
        return f'Dog {self.name} is jumping'


# kryakva = Animal()
# print(kryakva.say())

kuzya = Cat('Kuzya')
bobik = Dog('Bobik')
print(kuzya.say())
print(bobik.say())
print(kuzya.run())
print(bobik.jump())
