# son una colección de datos agrupados por una clave - valor

punto = { "x": 25, "y": 50}
print(punto) # { "x": 25, "y": 50}
print(punto["x"]) # 25
print(punto["y"]) # 50

punto["z"] = 45 # para agregar un nuevo elemento

print(punto)  # {'x': 25, 'y': 50, 'z': 45}

print(punto, punto["x"])

 # print(punto["lala"]) 
 # KeyError: 'lala'

if "lala" in punto:
    print("lala in punto")

else:
    print("no lala in punto")


print(punto.get("x"))
print(punto.get("lala")) # devuelve None porque no existe

print(punto.get("lala", 97)) # devuelve 97

del punto["x"] # eliminas la clave valor x

del(punto["y"]) # lo mismo pero con una función

print(punto) # solo imprime el par de z

punto["x"] = 25

for valor in punto:
    print(valor) # z x
    #para acceder a los valores de z x:
    print (valor, punto[valor]) # z 45 x 25

for valor in punto.items():
    print(valor)    
    # ('z', 45)
    # ('x', 25)

for llave, valor in punto.items(): # desempaquetado
    print(llave, valor)   
    # z 45
    # x 25

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])

