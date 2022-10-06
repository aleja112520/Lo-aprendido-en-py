Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#forma tradicional de hacer una función:
def suma (a,b):
    return a+b

suma(4,5)
9
#con funciones lambda:
suma_lambda=lambda a,b:a+b
suma_lambda(5,6)
11
#otro ejemplo:
far=lambda celcius:celcius*(7/5)+32
far(4)
37.6
#pueden tener cualquier número de argumentos(entradas) pero solo pueden tener una expresión(operación)
