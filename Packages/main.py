print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)

#from pack1.file_11 import a
#from pack2.pack21.file_211 import b
#print('a =', a)
#print('b =', b)

#from pack1 import file_11
#from pack2.pack21 import file_211
#print('a =', file_11.a)
#print('b =', file_211.b)
#print('Словарь some_dict:', file_211.some_dict)

from pack1.file_11 import result
from pack2.pack21.file_211 import r

print('result =', result)
print('r =', r)