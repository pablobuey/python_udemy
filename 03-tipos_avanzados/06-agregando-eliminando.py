mascotas = [
    "Wolfgang", 
    "Pelusa", 
    "Pulga", 
    "Felipe", 
    "Pulga", 
    "Chanchito Feliz"
]
mascotas.insert(1, "Melvin")

print(mascotas)
#['Wolfgang', 'Melvin', 'Pelusa', 'Pulga', 'Felipe', 'Pulga', 'Chanchito Feliz']

mascotas.append("Chanchito triste")
print(mascotas)
#['Wolfgang', 'Melvin', 'Pelusa', 'Pulga', 'Felipe', 'Pulga', 'Chanchito Feliz', 'Chanchito triste']

mascotas.remove("Pulga") #solamente elimina el primero
print(mascotas)
#['Wolfgang', 'Melvin', 'Pelusa', 'Felipe', 'Pulga', 'Chanchito Feliz', 'Chanchito triste']

mascotas.pop()
print(mascotas) #eliminas el último elemento
#['Wolfgang', 'Melvin', 'Pelusa', 'Felipe', 'Pulga', 'Chanchito Feliz']

mascotas.pop(1)
print(mascotas) #elimina el elemento del indice pasado como parámetro
#['Wolfgang', 'Pelusa', 'Felipe', 'Pulga', 'Chanchito Feliz']

del mascotas[0] #también para eliminar el elemento que le indiques
print(mascotas)

mascotas.clear() #elimina todos los elementos de la lista
print(mascotas)