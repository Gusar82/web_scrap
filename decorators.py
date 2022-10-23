"""Задача 1: Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
    имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
    Задача 2: Написать декоратор из З.1, но с параметром – путь к логам.
    Задача 3: Применить написанный логгер к приложению из любого предыдущего д/з."""

import datetime
from functools import wraps
import os


def log(old_function):
    files_dir = 'logs'
    file = "scrap.log"
    path = os.path.join(os.path.join(os.getcwd(), files_dir), file)

    @wraps(old_function)
    def new_function(*args, **kwargs):
        with open(path, 'a', encoding='utf8') as _file:
            print(f"функция: {old_function.__name__}", file=_file)
            print(f"дата и время вызова - {datetime.datetime.now()}", file=_file)
            # print(f"аргументы - {args} и {kwargs}", file=_file)

            result = old_function(*args, **kwargs)

            print(f"возр.значение - {result}", file=_file)
            print("----------------------------------------", file=_file)
            return result

    return new_function


def log_path(path):
    def log(old_function):
        _path = os.path.join(os.getcwd(), path)

        @wraps(old_function)
        def new_function(*args, **kwargs):
            with open(_path, 'a', encoding='utf8') as _file:
                print(f"функция: {old_function.__name__}", file=_file)
                print(f"дата и время вызова - {datetime.datetime.now()}", file=_file)
                # print(f"аргументы - {args} и {kwargs}", file=_file)

                result = old_function(*args, **kwargs)

                print(f"возр.значение - {result}", file=_file)
                print("----------------------------------------", file=_file)
                return result

        return new_function
    return log
