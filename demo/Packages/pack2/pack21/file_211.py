print('Это модуль', __name__)

# file_21 находится на один уровень выше текущего файла file_211, поэтому две точки
from ..file_21 import another_some_func
from file_0 import some_var

b: int = 4

some_dict: dict[int, str] = {1: 'A',
                             2: 'B',
                             3: 'C'}

r = another_some_func(b)
r = another_some_func(some_var)