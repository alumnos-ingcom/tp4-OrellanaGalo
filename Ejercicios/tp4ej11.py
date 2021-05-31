################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 11 - Palindromos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def es_palindromo(texto):
    
    igual = 0
    oracion = 0
    for i in reversed(range(len(texto))):
        if texto[i].lower() == texto[oracion].lower():
            igual += 1
            oracion += 1
    if len(texto) == igual:
        return True
    else:
        return False   

def prueba():
    
    print('Bienvenido!')
    texto = input('\nIngrese una palabra y el programa identificara si es palindromo o no: ')
    print(f'\nPalabra a identificar: {texto}')
    if es_palindromo(texto):
        print('\nLa palabra ingresada es palindromo.')
    else:
        print('\nLa palabra ingresada no es palindromo.')
    return 0

if __name__ == "__main__":
    prueba()
