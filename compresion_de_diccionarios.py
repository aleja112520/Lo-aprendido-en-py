Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#forma tradicional de hacer un diccionario:
#ejercicio:se desea crear un dicconario donde la key es un número divisible por 2 en un rango de -10 a 0 y su value es el cuadrado del número
dic={}
for i in range(-10,0):
    if (i%2==0):
        dic[i]=i**2

        
print(dic)
{-10: 100, -8: 64, -6: 36, -4: 16, -2: 4}
#con dictionary comprehensions:
diccionario={i:i**2 for i in range(-10,0) if (i%2==0)}
print(diccionario)
{-10: 100, -8: 64, -6: 36, -4: 16, -2: 4}
#o tambien se puede crear un diccionario a partir de otro diccionario, restrigiendo algunos key:value o poneiendo una condicion nueva
frutas={'fresa':2,"mora":6,'pera':19}
fru={key:valor*2 for (key,valor) in frutas.items()}
print(fru)
{'fresa': 4, 'mora': 12, 'pera': 38}
#o tambien con condicional:
fruta={key:valor for (key:valor) in frutas if (frutas.values>3)}
SyntaxError: invalid syntax
fruta={key:valor for (key,valor) in frutas if (frutas.values>3)}
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fruta={key:valor for (key,valor) in frutas if (frutas.values>3)}
  File "<pyshell#17>", line 1, in <dictcomp>
    fruta={key:valor for (key,valor) in frutas if (frutas.values>3)}
ValueError: too many values to unpack (expected 2)
fruta={key:valor for (key,valor) in frutas.items() if (frutas.values>3)}
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fruta={key:valor for (key,valor) in frutas.items() if (frutas.values>3)}
  File "<pyshell#18>", line 1, in <dictcomp>
    fruta={key:valor for (key,valor) in frutas.items() if (frutas.values>3)}
TypeError: '>' not supported between instances of 'builtin_function_or_method' and 'int'
fruta={key:valor for (key,valor) in frutas.items() if (valor>3)}
print(fruta)
{'mora': 6, 'pera': 19}
nombre_fruta=[key for key in frutas.keys]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nombre_fruta=[key for key in frutas.keys]
TypeError: 'builtin_function_or_method' object is not iterable
nombre_fruta=[key for key in frutas.keys()]
print(nombre_fruta)
['fresa', 'mora', 'pera']
cantidad=[valor for valor in frutas.values()]
print(cantidad)
[2, 6, 19]
