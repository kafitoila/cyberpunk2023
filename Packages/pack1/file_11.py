print('Это файл', __name__)
__all__ = ['some_var', 'yet_another_var', 'another_func']

# file_11 (текущий файл) находится в том же каталоге, что и file_12, поэтому ставится одна точка
#from .file_12 import num
#def some_func(n: int) -> float:
#    return (n + n) / n**n
#result = some_func(num)

some_var: int = 2
another_var: int = 4
yet_another_var: str = 'some_text'
a: int = 7


def _reverse_text(text: str) -> str:
    return text[::-1]


def some_func(text: str, times: int) -> str:
    return _reverse_text(text * times)

def another_func() -> None:
    pass

def func_1(n: int) -> int:
    return n * n