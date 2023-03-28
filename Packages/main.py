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

#from pack1.file_11 import result
#from pack2.pack21.file_211 import r
import pack1
import pack2
from pack2 import pack21


print(dir())
print(dir(pack1))
print(dir(pack2))
print(dir(pack21))

#print('result =', result)
#print('r =', r)
#print(pack2.another_some_func(7))