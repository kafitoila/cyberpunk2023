#print(dir())

import functions
from data import my_dict as dict
from classes import *
#import sys

#print(sys.builtin_module_names) - 1. встроенные
#                                  2. та же папка
#print(sys.path) -                 3. путь окружения переменных
#print(sys.stdlib_module_names) -  4. стандартная библиотека

print('Это исполняемый файл')
var: int = 15

if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')
    print(functions.get_double_number(100))
    print(dict)
    MyClass()
    print(__name__)