#####################################################################
#####################################################################
########################### CALCULADORA #############################
#####################################################################
#####################################################################
import os
from datetime import datetime

# variables para promt
usuario = os.getlogin()
hora_actual = datetime.now().strftime("%H:%M:%S")

#inicio
print("\n# Bienvenido a la calculadora.")
instruccion = input("# Introduce primer numero o escribe salir: \n $"+ usuario + " - " + datetime.now().strftime("%H:%M:%S" + ": "))


if instruccion == "salir":    
    print("adiós")

elif not instruccion.isnumeric():

    print("Solo puedes introducir numeros o salir. \n ")

else:    
         
    numero1 = int(instruccion)

    resultado = numero1

    while instruccion != "salir":

        instruccion = input("# Escribe sumar, restar, multiplicar, dividir o salir:\n $"+ usuario + " - " + datetime.now().strftime("%H:%M:%S" + ": "))  

        if instruccion == "salir":
            print("adios")
        else:        
            numero2 = int(input("Introduce segundo numero:\n " + usuario + " - " + datetime.now().strftime("%H:%M:%S" + ": ")))


            if instruccion == "sumar":

                resultado = resultado + numero2
                print(f"La suma es: {resultado}")

            elif instruccion == "restar":

                resultado = resultado - numero2
                print(f"La resta es: {resultado}")

            elif instruccion == "multiplicar":

                resultado = resultado * numero2
                print(f"La multiplicacion es: {resultado}")

            elif instruccion == "dividir":
                if numero2 != 0:
                    resultado = resultado / numero2
                    print(f"La division es: {resultado}")
                else:
                    print("ERROR: No puedes dividir entre cero.")

            else:
                print("ERROR: Escribe sumar, restar, multiplicar, dividir o salir.")