mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz", "Chanchito Feliz"]

print(mascotas.index("Pulga"))
#1

if "Felipe" in mascotas:
    print(mascotas.index("Felipe"))
#2

if "Nombre que no existe" in mascotas:
    print(mascotas.index("Nombre que no existe"))
else:
    print("No existe")
#No existe

if "Chanchito Feliz" in mascotas:
    print(mascotas.index("Chanchito Feliz"))
#solo imprime el primero que encuentra

print(mascotas.count("Chanchito Feliz"))
#2


