animal = " perrO feliz "

#lo convierte en mayúsculas
print(animal.upper())

#minúsculas
print(animal.lower())

#Convierte en mayuscula la primera letra del string
print(animal.capitalize())

#Toma la primera letra de cada palabra y las pone mayúsculas
print(animal.title())

#Elimina espacios al principio y al final del string
print(animal.strip())

#Quita espacios de la derecha
print(animal.rstrip())

#Quita espacios de la izquierda
print(animal.lstrip())

#encadena metodos string, en este caso le quita espacios y pone mayuscula la primera letra del string
print(animal.strip().capitalize())

#buscar una cadena de caracteres, si devuelve un -1 es porque no lo encuentra
print(animal.find("rO"))

#reemplaza las r por l
print(animal.replace("r", "l"))

#devuelve booleano; si contiene o no contiene perrO devuelve True o False
print("perrO" in animal)
print("perrO" not in animal)


