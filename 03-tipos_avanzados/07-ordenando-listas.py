numeros = [2, 123, 22, 44, 45]

numeros.sort()
print(numeros)
#[2, 22, 44, 45, 123]

numeros.sort(reverse=True)
print(numeros)
#[123, 45, 44, 22, 2]

numeros2 = sorted(numeros) #va a devolver una nueva lista
print(numeros)
print(numeros2)
# [2, 22, 44, 45, 123]
# [123, 45, 44, 22, 2]

numeros3 = sorted(numeros, reverse=True)
print(numeros3) # lo ordena al revés

usuarios = [
    [4, "Chanchito"], 
    [1, "Felipe"], 
    [5, "Pulga"]
]
usuarios.sort()
print(usuarios)
# [[1, 'Felipe'], [4, 'Chanchito'], [5, 'Pulga']]

# cambiando el par clave valor necesitamos una función
usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
print(usuarios)

usuarios.sort(key=ordena, reverse = True)
print(usuarios)
# los ordena al revés

usuarios.sort(key=lambda el:el[1], reverse = True) # función lambda o función anónima. No haría falta tener la funcion ordena creada a parte.
print(usuarios)
# los ordena al revés
