# Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out), es decir, el último elemento en entrar es el primero en salir. 
# En Python, las pilas se pueden implementar usando listas, aprovechando los métodos append() y pop().

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila) # [1, 2, 3]

# al utilizar append y pop, se comporta como una pila (o stack)

ultimoElemento = pila.pop()
print(ultimoElemento) # 3
print(pila) # [1, 2]
print(pila[-1]) # devuelve el último elemento de la lista


if not pila:
    print("pila vacia")


# DIFERENCIAS CLAVE ENTRE FILA Y PILA:

# Acceso a elementos: En una lista, se puede acceder a cualquier elemento mediante su índice. En una pila, normalmente solo se accede al último elemento añadido.

# Operaciones permitidas: Las listas permiten una gran variedad de operaciones (inserciones, eliminaciones en cualquier posición, ordenamientos, etc.), 
# mientras que las pilas se limitan a operaciones LIFO (añadir al final y quitar del final).

# Uso típico: Las listas son más generales y se usan para almacenar y manipular colecciones de elementos de forma flexible. 
#Las pilas se usan en situaciones específicas donde el orden LIFO es necesario, como en algoritmos de retroceso (backtracking), evaluación de expresiones, manejo de llamadas recursivas, etc.

