#! /usr/bin/env python3
"""Создайте несколько классов конструктора автомобиля:
Engine -> Car -> Honda
Реализуйте наследование этих классов и базовые методы для каждого из них, например start/stop для engine,
open/close doors для Car и т.д.
Используйте __init__ для инициализации необходимых параметров (максимальная скорость, объем двигателя, и т.п.)
Примените инкапсуляцию для сокрытия вспомогательных методов
По необходимости используйте staticmethod / classmethod / property"""


class Engine:
    """Создание класса engine с параметроме volume (объем) 2 меттода старт/стоп"""
    """инициализация параметров"""

    def __init__(self, volume):
        self.volume = volume

    def start(self):
        return 'Start engine'

    def stop(self):
        return 'Stop engine'


class Car(Engine):
    """инициализация параметров, наследуем параметры и методы от родительского класса engine
    при этом, при создании объекта Car можем не указывать значаение параметра volume"""

    def __init__(self, color='white', volume=None):
        Engine.__init__(self, volume)
        self.color = color

    @staticmethod
    def open_close(value):
        if value == 'open':
            return 'door is opened'
        elif value == 'close':
            return 'door is closed'
        else:
            return 'This method takes only "open" or "close"'


class Honda(Car):
    some_cls_param = 'some param'

    """инициализация параметров и наследование от родительского класса"""

    def __init__(self, model_name, max_speed, volume=None, color='white'):
        Car.__init__(self, color, volume)
        self.__model_name = model_name
        self.max_speed = max_speed

    """методы для изменения и вывода model_name т.к. обрашение к параметру на прямую вызовет ошибку, 
    вариант инкапсуляции в Python"""

    def set_model_name(self, model_name):
        self.__model_name = model_name

    def get_model_name(self):
        return self.__model_name

    @classmethod
    def class_method(cls, value):
        return cls.some_cls_param, value

    def info(self):
        return f'название модели            {self.__model_name}\n' \
               f'цвет:                      {self.color}\n' \
               f'максимальная скорость:     {self.max_speed}\n' \
               f'объем двигателя:           {self.volume}'


# one = Car('red')
# one.volume = 5
# print()
#
# accord = Honda('Accord', 200, 5)
# print(accord.info())
# accord.start()
# print(accord.stop())
# print(accord.class_method('test class_method'))
# accord.color = 'black'
# print(accord.info())
#
# accord.set_model_name('civic')
# print(accord.info())
#
# print(accord.open_close('open'))
