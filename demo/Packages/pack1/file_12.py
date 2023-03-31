print('Это файл', __name__)

import sys
from pprint import pprint
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
pprint(sys.path)

num: int = 3

from pack1.file_11 import a

print(a)

def func_2(n: int) -> int:
    return n + n

print(func_2(a))