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

