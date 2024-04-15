# listas de comprensión

# Las listas de comprensión en Python son una forma concisa y poderosa de crear listas. 
# Son una alternativa a la creación de listas utilizando el bucle for.

usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)


nombres = [usuario[0] for usuario in usuarios] # devuelve los nombres 
print(nombres)

nombres = [usuario for usuario in usuarios if usuario[1] > 2] # devuelve los elementos con id > 2 
print(nombres)


nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2] # filtrando y transformando la lista
print(nombres)

#lo mismo pero con map y filter

nombres = list(map(lambda usuario: usuario[0], usuarios)) # map
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios)) # filter
print(menosUsuarios)