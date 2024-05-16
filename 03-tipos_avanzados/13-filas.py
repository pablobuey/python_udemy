from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila) # deque([1, 2, 3, 4, 5])

fila.popleft() # elimino el elemento más a la izda
print(fila) # deque([2, 3, 4, 5])

if not fila:
    print("fila vacía") # se puede evaluar como false un arreglo vacío, un string vacío y el número 0.



