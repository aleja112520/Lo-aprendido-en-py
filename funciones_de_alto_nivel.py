Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#funciones de orden superior: son aquellas que reciben como argumento otra funcion, o que entregan como salida una función. Python cuenta con funciones superiores ya estandarizadas como: filter, map y reduce.
#Función filter: recibe como argumentos,  una función con la cual se quiera hacer el filtrado y un iterable(lista, diccionario, array...)
numeros=[1 2 3 4 5 6 7 8 9 10]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares=list(filter(lambda x:x%2==0,numeros))
print(pares)
[2, 4, 6, 8, 10]
#la función filter es booleana, así que regresará TRUE si la condición se cumple en el iterable numeros, si es así, los listará en pares

#Función map(funcion,iterable): aplica la función en el iterable que se pase como argumento
cubos=list(map(lambda x:x**3,numeros))
cubos
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#Función Reduce(funcion,iterble): reduce a un único número el iterable que se le pase como argumento, lo hace aplicando la función que se le pase como entrada, el procedimiento que sigue es el siguiente: supongamos que es l función suma, sumará el elemento primero con el segundo, el resultado lo sumará con el tercer elemento y así sucesivamente
#para usar esta función se debe importar la siguiente libreri:
from functools import reduce
reduc=reduce(lambda a,b:a*b,numeros)
reduc
3628800
