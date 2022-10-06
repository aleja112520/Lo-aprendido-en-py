Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hola")
hola
agenda={"felipe":{
                  "telefono":234532,
                  "Pais":"Rusia"},
        "andrea":{"telefono":3485940,
                  "Pais":"Colombia"}
        }
print(agenda.items)
<built-in method items of dict object at 0x0000018022DEB940>
print(agenda["felipe"])
{'telefono': 234532, 'Pais': 'Rusia'}
print(agenda["felipe"]["telefono"])
234532
agenda={"felipe":{
                  "telefono":234532,
                  "Pais":"Rusia",
                  "hobbies":["futbol","nadar"]},
        "andrea":{"telefono":3485940,
                  "Pais":"Colombia",
                  "hobbies":["futbol",567]}
        }
hob_feli=agenda["felipe"]["hobbies"]
print(hob_feli)
['futbol', 'nadar']
for i in hob_feli:
    print(i)

futbol
nadar
hob_andre=agenda["andrea"]["hobbies"]
for i in hob_andre:
    print(i)

    
futbol
567
for nombre,datos in agenda.items():
    print("{}:{}".format(nombre,datos["hobbies"]))

    
felipe:['futbol', 'nadar']
andrea:['futbol', 567]
for nombre,datos in agenda.items():
    print("{}:{}".format(nombre,datos["Pais"]))

    
felipe:Rusia
andrea:Colombia
agenda={"felipe":{
                  "telefono":234532,
                  "Pais":"Rusia",
                  "info_personal":{"musica":"pop",
                                   "estudios":"no tiene"}
                  },
        "andrea":{"telefono":3485940,
                  "Pais":"Colombia",
                  "info_personal":{"musica":"rock",
                                   "estudios":"inge"}
                  }
        }
for nombre,datos in agenda.items():
    if (datos["Pais"]=="Colombia"):
        print(nombre)

        
andrea
for nombre,datos in agenda.items():
    if (datos["Pais"]=="Colombia") & (datos["info_personal"]["musica"]=="rock"):
        print(nombre)

        
andrea
for nombre,datos in agenda.items():
    if (datos["Pais"]=="Colombia") & (datos["info_personal"]["musica"]=="pop"):
        print(nombre)

        
for nombre,datos in agenda.items():
    print("{}:{}".format(nombre,datos["info_personal"]))

    
felipe:{'musica': 'pop', 'estudios': 'no tiene'}
andrea:{'musica': 'rock', 'estudios': 'inge'}
for nombre,datos in agenda.items():
    print(nombre,datos["info_personal"])

    
felipe {'musica': 'pop', 'estudios': 'no tiene'}
andrea {'musica': 'rock', 'estudios': 'inge'}
for nombre,datos in agenda.items():
    print("{}:{} \n".format(nombre,datos["info_personal"]))

    
felipe:{'musica': 'pop', 'estudios': 'no tiene'} 

andrea:{'musica': 'rock', 'estudios': 'inge'} 

for nombre,datos in agenda.items():
    print("{}:\n{}".format(nombre,datos["info_personal"]))

    
felipe:
{'musica': 'pop', 'estudios': 'no tiene'}
andrea:
{'musica': 'rock', 'estudios': 'inge'}
