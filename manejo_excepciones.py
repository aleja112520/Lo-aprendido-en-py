Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#MANEJO DE EXCEPCIONES:
#EJEMPLO: DIVISIÓN POR 0
def division a,b:
    
SyntaxError: invalid syntax
def division (a,b):
    return a/b

result=division(3,0)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    result=division(3,0)
  File "<pyshell#5>", line 2, in division
    return a/b
ZeroDivisionError: division by zero
def division (a,b):
    try:
        return a/b
    except(ZeroDivisionError):
        print("Sumercé, está dividiendo por 0")

        

print(division(3,0))
Sumercé, está dividiendo por 0
None
#OTRO EJEMPLO:
def division (a,b):
    try:
        return a/b
    except(ZeroDivisionError):
        print("Sumercé, está dividiendo por 0")
    except(TypeError):
        print("Sumercé, solo puede ingresar números")

        
print(division(*,4))
SyntaxError: invalid syntax
print(division('*',4))
Sumercé, solo puede ingresar números
None
print(division('*',0))
Sumercé, solo puede ingresar números
None

# uso de ELSE, el programa entrará en el ELSE si no entra  a ninguna excepcion:
def division (a,b):
    try:
        z= a/b
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    else:
        return z

    
print(division(2,0))
Sumercé, está ingresando un valor erróneo
None
print(division(2,9))
0.2222222222222222
def division (a,b):
    try:
        z= a/b
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    else:
        print (z)

        
print(division(2,9))
0.2222222222222222
None

#uso de FINALLY, se usa luego de usar try,except, else. Esta instrucción siempre se ejecutará sin importar si hubo una excepción o no, y se ejecutará primero que un return o break. Esto garantiza que siempre se ejecute
def division (a,b):
    try:
        z= a/b
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    else:
        return (z)
    finally:
        print("soy finally")

        
division(4,0)
Sumercé, está ingresando un valor erróneo
soy finally
division(3,4)
soy finally
0.75
#uso de RISE, con RISE se puede crear una excepción, que vaya acorde con las necesidades de mi código:
#EJEMPLO: suponer que dentro de mi lógica no acepto valores negtivos en la entrada de los vlores  y b
def division (a,b):
    try:
        z= a/b
        if a/b<0:
            raise ValueError("mija, está metiendo números negativos")
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    except (ValueError):
        print (ValueError)
    else:
        return (z)
    finally:
        print("soy finally")

        
division(4,8)
soy finally
0.5
division(-3,7)
<class 'ValueError'>
soy finally
def division (a,b):
    try:
        z= a/b
        if a/b<0:
            raise ValueError("mija, está metiendo números negativos")
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    except (ValueError):
        print ("mija, está metiendo números negativos")
    else:
        return (z)
    finally:
        print("soy finally")

        
division(-3,7)
mija, está metiendo números negativos
soy finally
def division (a,b):
    try:
        z= a/b
        if a/b<0:
            raise ValueError("mija, está metiendo números negativos")
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    except (ValueError as ve):
        print (ve)
    else:
        return (z)
    finally:
        print("soy finally")
        
SyntaxError: invalid syntax
def division (a,b):
    try:
        z= a/b
        if a/b<0:
            raise ValueError("mija, está metiendo números negativos")
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    except ValueError as ve:
        print (ve)
    else:
        return (z)
    finally:
        print("soy finally")

        
division(-3,7)
mija, está metiendo números negativos
soy finally
def division (a,b):
    try:
        z= a/b
        if a/b<0:
            raise ValueError("mija, está metiendo números negativos")
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    except ValueError:
        print (ValueError)
    else:
        return (z)
    finally:
        print("soy finally")

        
division(-3,7)
<class 'ValueError'>
soy finally
def division (a,b):
    try:
        z= a/b
        if a/b<0:
            raise ValueError("mija, está metiendo números negativos")
    except(ZeroDivisionError,TypeError):
        print("Sumercé, está ingresando un valor erróneo")
    except ValueError as ve:
        print (ve)
    else:
        return (z)
    finally:
        print("soy finally")

        
division(-3,7)
mija, está metiendo números negativos
soy finally

####EJERCICIO############3
#se va a crear una función que calcule el BMI y otra que le diga al ususario en qué nivel está, se deben tratar la mayoria de las excepciones

def BMI(peso,altura):
    return peso/altura**2

def clasificar(BMI):
    if (BMI<=24,9) or (BMI>=18,5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    else BMI<18,5:
        
SyntaxError: expected ':'

def clasificar(BMI):
    if (BMI<=24,9) or (BMI>=18,5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    else BMI<18,5:
        
SyntaxError: expected ':'

def clasificar(BMI):
    if (BMI<=24,9) or (BMI>=18,5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    elif BMI<18,5:
        
SyntaxError: invalid syntax
def clasificar(BMI):
    if (BMI<=24,9) or (BMI>=18,5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    elif BMI<18,5:
        
SyntaxError: invalid syntax
def clasificar(BMI):
    if (BMI<=24.9) or (BMI>=18.5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    elif BMI<18.5:
        return "Bajo de peso"

    
def clasificar(BMI(peso,altura)):
    if (BMI<=24.9) or (BMI>=18.5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    elif BMI<18.5:
        return "Bajo de peso"
    
SyntaxError: invalid syntax
clasificar(BMI(23,7))
'Saludable'
BMI(23,7)
0.46938775510204084
def clasificar(BMI):
    if (BMI<=24.9) and (BMI>=18.5):
        return "Saludable"
    elif BMI>25:
        return "Sobrepreso"
    elif BMI<18.5:
        return "Bajo de peso"

    
clasificar(BMI(23,7))
'Bajo de peso'
clasificar(BMI(23,98))
'Bajo de peso'
clasificar(BMI(230,98))
'Bajo de peso'
clasificar(BMI(230,8))
'Bajo de peso'
clasificar(BMI(230,2))
'Sobrepreso'
clasificar(BMI(98,2))
'Saludable'
peso=input("ingrese peso")
ingrese peso230
altura=input("ingrese altura")
ingrese altura98
try:
    clasificar(BMI(peso,altura))
    except(TypeError):
        
SyntaxError: invalid syntax
try:
    clasificar(BMI(peso,altura))
        if peso<0 or altura<0:
            raise ValueError:("Buena, está metiendo valores negativos")
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    
SyntaxError: unexpected indent
try:
    clasificar(BMI(peso,altura))
    if peso<0 or altura<0:
        raise ValueError:("Buena, está metiendo valores negativos")
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    
SyntaxError: invalid syntax
try:
    clasificar(BMI(peso,altura))
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)

    
está metiendo un valor raro
peso=input("ingrese peso")
ingrese peso230
altura=input("ingrese altura")
ingrese altura98
try:
    clasificar(BMI(peso,altura))
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)

    
está metiendo un valor raro
clasificar(BMI(peso,altura))
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    clasificar(BMI(peso,altura))
  File "<pyshell#67>", line 2, in BMI
    return peso/altura**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
peso=float(input("ingrese peso"))
ingrese peso230
altura=float(input("ingrese altura"))
ingrese altura98
clasificar(BMI(peso,altura))
'Bajo de peso'
try:
    clasificar(BMI(peso,altura))
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)

    
'Bajo de peso'
peso=float(input("ingrese peso"))
ingrese pesoy
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    peso=float(input("ingrese peso"))
ValueError: could not convert string to float: 'y'
peso=float(input("ingrese peso"))
ingrese peso-7
altura=float(input("ingrese altura"))
ingrese altura8
try:
    clasificar(BMI(peso,altura))
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)

    
'Bajo de peso'
Buena, está metiendo valores negativos
try:
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
    clasificar(BMI(peso,altura))
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)

    
Buena, está metiendo valores negativos
try:
    if peso<0 or altura<0:
        raise NegativeError("Buena, está metiendo valores negativos")
    clasificar(BMI(peso,altura))
except(TypeError):
    print("está metiendo un valor raro")
except NegativeError as ne:
    print(ne)

    
Traceback (most recent call last):
  File "<pyshell#123>", line 3, in <module>
    raise NegativeError("Buena, está metiendo valores negativos")
NameError: name 'NegativeError' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#123>", line 7, in <module>
    except NegativeError as ne:
NameError: name 'NegativeError' is not defined
try:
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
    clasificar(BMI(peso,altura))
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)
except ValueError:
    print("está metiendo un valor regulimbis")

    
Buena, está metiendo valores negativos
peso=float(input("ingrese peso"))
ingrese peso34
try:
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
    clasificar(BMI(peso,altura))
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)
except ValueError:
    print("está metiendo un valor regulimbis")

    
'Bajo de peso'
peso=float(input("ingrese peso"))
ingrese pesou
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    peso=float(input("ingrese peso"))
ValueError: could not convert string to float: 'u'
try:
    if peso<0 or altura<0:
        raise ValueError("Buena, está metiendo valores negativos")
    clasificar(BMI(peso,altura))
except(TypeError):
    print("está metiendo un valor raro")
except ValueError as ve:
    print(ve)
except (ValueError):
    print("está metiendo un valor regulimbis")

    
'Bajo de peso'
peso=float(input("ingrese peso"))
ingrese pesoy
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    peso=float(input("ingrese peso"))
ValueError: could not convert string to float: 'y'
try:
    clasificar(BMI(peso,altura))
except(TypeError):
    print("está metiendo un valor raro")
except (ValueError):
    print("está metiendo un valor regulimbis")

    
'Bajo de peso'
peso=float(input("ingrese peso"))
ingrese pesoy
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    peso=float(input("ingrese peso"))
ValueError: could not convert string to float: 'y'
peso=float(input("ingrese peso"))
ingrese peso
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    peso=float(input("ingrese peso"))
ValueError: could not convert string to float: ''
try:peso=float(input("ingrese peso"))
except ValueError("está metiendo un valor regulimbis")
SyntaxError: expected ':'
try:peso=float(input("ingrese peso"))
except ValueError:("está metiendo un valor regulimbis")

ingrese pesoj
'está metiendo un valor regulimbis'

#########################
##USO DE assert, funciona como un condicional booleano, si la condición es verdadera continuará con el código, sino ,, hará lo programado en tal caso:
def divi(a,b)
SyntaxError: expected ':'
def divi(a,b):
    assert (a>0 and b>0),"Estas dividiendo por 0 guero"
    return a/b

divi(3,8)
0.375
divi(3,0)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    divi(3,0)
  File "<pyshell#150>", line 2, in divi
    assert (a>0 and b>0),"Estas dividiendo por 0 guero"
AssertionError: Estas dividiendo por 0 guero
def divi(a,b):
    try:
        assert (a>0 and b>0),"Estas dividiendo por 0 guero"
        return a/b
    except AssertionError as ae:
        print(ae)

        
divi(6,0)
Estas dividiendo por 0 guero
