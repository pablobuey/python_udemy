# una tupla es lo mismo que una lista, pero no puedes modificarla

# se pueden encadenar tuplas
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# se utilizan cuando no queremos modificar los elementos de un listado

punto = tuple([1, 2]) # transformamos una lista en tupla
print(punto)

menosNumeros = numeros[:2] # he creado una lista a partir de "numeros"

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# si quieres modificar una tupla, se crea una lista:

listaNumeros = list(numeros)
listaNumeros[0] = 2
print(listaNumeros)