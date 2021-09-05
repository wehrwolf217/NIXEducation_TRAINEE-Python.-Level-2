#! /usr/bin/env python3
"""Написать свой декоратор, который будет отлавливать ошибки, полученные в
ходе выполнения обёрнутой функции, логгировать их и делать raise отловленной ошибки"""
import sys
from time import asctime


def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            exc_type, value, traceback = sys.exc_info()
            log_file_content = f'{asctime()} - {func.__name__}, {exc_type} {e}\n'
            with open('errors.log', 'a', encoding='utf8') as file:
                file.write(log_file_content)
            raise

    return wrapper


# some func for test
@log_errors
def key_err(some_dict):
    return some_dict['123']


try:
    key_err({'test': 1, 'something': 2})
except Exception:
    pass


@log_errors
def type_err(some_list, some_tuple):
    return some_list + some_tuple


try:
    type_err([1, 2, 3], (1, 2,))
except Exception:
    pass


@log_errors
def d_by_zero(num):
    return num / 0


try:
    d_by_zero(22)
except Exception:
    pass
