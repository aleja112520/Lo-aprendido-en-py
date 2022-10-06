Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
""
''
#Hay dos formas de crear una lista:
#LA FORMA TRADICIONAL:
numeros=[2,5,4,6]
for n in numeros:
    cuadrados.append(n*n)

    
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    cuadrados.append(n*n)
NameError: name 'cuadrados' is not defined
cuadrados=[]
for n in numeros:
    cuadrados.append(n*n)

    
print(cuadrados)
[4, 25, 16, 36]
#Y CON COMPRESION DE LISTAS:
cuadrados=[x*x for x in numeros]
cuadra=[x*x for x in numeros]
print(cuadra)
[4, 25, 16, 36]
#OTRO EJEMPLO:
num=[x if (x>5) else '*' for x in numeros]
print(num)
['*', '*', '*', 6]
#La ventaja de esta manera es que no se le asignará la lista interna (que es una lista que va haciendo python internamente)a la lista que esté creando hasta que no recorra todo el for, en rendimiento resulta ser más eficiente y rápido.
diccionarios_anidados.py
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    diccionarios_anidados.py
NameError: name 'diccionarios_anidados' is not defined
