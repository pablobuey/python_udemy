#pueden usarse comillas dobles o simples
nombre = "Pablo"
nombre2 = 'Pablo'

#string de varias líneas
direccion = """
Esto es un String de 
varias líneas 
"""
#la función len() es como el length de Java
#sirve para obtener la longitud de un String
print(len(direccion))

#para acceder al íncide de un string
print(nombre[0])
#devolverá P

print(nombre[0:5])
#devolverá de la P (slot 0) a la o (se indica el número de caracteres que quieres mostrar despues del primer slot)

print(nombre[2:])
#devuelve desde el slot 2 hasta el final

print(nombre[:2])
#deuelve hasta el caracter 2

print(nombre[:])
#devolverá todo
