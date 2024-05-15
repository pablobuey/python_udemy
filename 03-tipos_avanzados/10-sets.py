# set es grupo o conjunto

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
print(primer)

segundo = [3, 4, 5] # lista

#transformar en set
segundo = set(segundo)

#imprime los dos sets juntos sin numeros repetidos (es decir, 1, 2, 3, 4, 5)
print(primer | segundo) #el operador | se le conoce como unión

print(primer & segundo) # con el operador "intersección" & imprime sólo los elementos que se encuentran en ambos sets, en este caso 3, 4.

print(primer - segundo) # con el operador "diferencia" - imprime los elementos del primer grupo eliminando los elementos del segundo grupo.

print(primer ^ segundo) # con el operador "diferencia simétrica" ^ devuelve los elementos que no se encuentran en ninguno de los dos sets.

# con los sets no se puede acceder a los elementos, como en las listas
# se puede hacer esto:
if 5 in segundo:
    print("contiene el 5")