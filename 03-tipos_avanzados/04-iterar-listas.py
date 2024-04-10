mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

for mascota in mascotas: 
    print(mascota)
# Pelusa
# Pulga
# Felipe
# Chanchito Feliz

for mascota in enumerate(mascotas):
    print(mascota)   
# (0, 'Pelusa')
# (1, 'Pulga') 
# (2, 'Felipe')
# (3, 'Chanchito Feliz')
   
for indice, mascota in enumerate(mascotas):
    print(indice, mascota) 
# 0 Pelusa
# 1 Pulga
# 2 Felipe
# 3 Chanchito Feliz
    