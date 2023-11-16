print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while  True:
    if not resultado:
        resultado = input("Ingresa numero: ")
        if resultado.lower() == "salir":
            break
        resultado(int(resultado))
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ") 
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower == "suma":
        resultado += n2
    elif op.lower == "resta":
        resultado -= n2 
    elif op.lower == "multi":
        resultado *= n2 
    elif op.lower == "div":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    print(f"El resultado es {resultado}")
