mascotas = ["wolf", "pelusa", "pulga", "copito"]
print(mascotas[0])

mascotas[0] = "Bicho"
print(mascotas)

print(mascotas[:3]) #hasta el elemento 3
print(mascotas[2:]) #desde el elemento 2
print(mascotas[-1]) #devuelve el anterior al primero, o sea el último

print(mascotas[::2])#numeros pares
print(mascotas[1::2])#numeros impares

numeros = list(range(1, 21))
print(numeros[::2]) #te imprime los numeros impares del 1 al 21.
