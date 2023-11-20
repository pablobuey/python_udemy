
#sin parametros
def hola():
    print("Hola mundo")

hola()

#con parametros
def hola2(nombre):
    print(f"Hola {nombre}")

hola2("pablo")

#argumentos opcionales
def hola3(nombre, apellido="buey"):
    print(f"Hola {nombre}")

hola3("pablo")
hola3("pablo", "martin")

#argumentos nombrados
hola3(nombre="Pablo", apellido="bueyy")






