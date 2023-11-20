

def es_palindromo(texto):      
    reverse = texto[::-1] 
    if texto == reverse:
        return True

palabra = input("introduce palabra para comprobar si es palindromo:")
print(es_palindromo(palabra))
