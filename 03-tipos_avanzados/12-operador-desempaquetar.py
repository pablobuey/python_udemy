lista1 = [1, 2, 3, 4]
print(lista1) # [1, 2, 3, 4]
print(*lista1) # 1 2 3 4

lista2 = [5,6]

combinada = ["hola", *lista1, "mundo", *lista2, "chanchito"]

print(combinada) # ['hola', 1, 2, 3, 4, 'mundo', 5, 6, 'chanchito']


punto1 = { "x": 19}
punto2 = { "y": 15}

nuevoPunto = { **punto1, **punto2}
print(nuevoPunto) # {'x': 19, 'y': 15}
