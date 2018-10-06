## Tipos
shapeName = 'circle'
print type(shapeName)

shapeNr = 5
print type(shapeNr)

var = [u'polyCube1', u'polyCubeShape1']
print var[0]
print var[1]

## Estructuras

# Lista
lista = ["string", 2, [1,2,3], "string"]
lista.append(True)
lista[0] = "Chile"
print lista

# Tupla
tupla = ("string", 2, [1,2,3], "string")
print tupla
tupla[2][0] = "99"
print tupla

# Set
#conjunto = set(tupla)   ### EJEMPLO DE UNA LISTA (mutable) dentro de un SET (inmutable)
tupla_2 = ("string", 2, (1,2,3), "string")
print set(tupla_2)

# Dictionary
dict = {"A": "Arbol", "B": "Barroco"}
print dict


for clave,valor in dict.iteritems():
    print clave, valor