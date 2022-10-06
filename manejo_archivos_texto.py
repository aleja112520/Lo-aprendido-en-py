Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from io import open
archivo_texto=open(archivo_texto.txt,"w")#w de write, hay modo lectura y append para agregar datos al archivo.
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    archivo_texto=open(archivo_texto.txt,"w")#w de write, hay modo lectura y append para agregar datos al archivo.
NameError: name 'archivo_texto' is not defined
archivo_texto=open("archivo.txt","w")#w de write, hay modo lectura y append para agregar datos al archivo.
frase="mi mama me mima yo la mimo a ella \n a ver si aprendemos"
archivo_texto.write(frase)
55
archivo_texto.close()
archivo_read=("archivo_texto.txt","r")
texto=archivo_read.read()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    texto=archivo_read.read()
AttributeError: 'tuple' object has no attribute 'read'
archivo_read=open("archivo_texto.txt","r")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    archivo_read=open("archivo_texto.txt","r")
FileNotFoundError: [Errno 2] No such file or directory: 'archivo_texto.txt'
archivo_read=open("archivo.txt","r")
texto=archivo_read.read()
print(texto)
mi mama me mima yo la mimo a ella 
 a ver si aprendemos
archivo_read.close()
archivo_read=open("archivo.txt","r")
lineas_texto=archivo_read.readlines()
print(lineas_texto)
['mi mama me mima yo la mimo a ella \n', ' a ver si aprendemos']
print(lineas_texto[0])
mi mama me mima yo la mimo a ella 

print(lineas_texto[1])
 a ver si aprendemos
archivo_read=open("archivo.txt","a")
archivo_read.write("\n ay pero qué buena ocasión para programar en python")
52
archivo_read=open("archivo.txt","r")
archivo_read.read()
'mi mama me mima yo la mimo a ella \n a ver si aprendemos\n ay pero qué buena ocasión para programar en python'
###############################3
##############################
###CONCLUSION#############333
##########################33

#para manipular archivos de texto se pueden usar los métodos:
#archivo_read=open("archivo.txt","w"): w de write, con este se creará el archivo en la carpeta donde se guarde el proyecto y con archivo_read.write("\n ay pero qué buen") se puede escribir en el archivo
#archivo_read=open("archivo.txt","w")
#archivo_read=open("archivo.txt","r"): r de read, para leer lo que hay en el archivo, se puede usar tambien lineas_texto=archivo_read.readlines() que hará una lista con cada linea que haya en el archivo
##archivo_read=open("archivo.txt","a"):a de append que agregará información en el documento que ya debe estar creado
