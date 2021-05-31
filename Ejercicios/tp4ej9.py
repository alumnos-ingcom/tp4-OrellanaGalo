################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 9 - Numeros primos 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def es_primo(numero):
    
    for contador in range(numero):
        if contador + 1 == numero:
            return True
        elif contador + 1 == 1:
            pass
        elif numero <= 0 or numero == 1:
            return 0
        else:
            resto_div = numero % (contador + 1)
            if resto_div == 0:
                return False

def prueba():
    
    print('Bienvenido!')
    
    numero = ingreso_entero('\nIngrese un numero para saber si es primo.')
    num_primo = es_primo(numero)
    print('\n True = El numero ingresado es primo\n False = El numero ingresado no es primo\n None = El valor ingresado no es valido')
    print('\nEl valor ingresado corresponde a: ', num_primo)

if __name__ == "__main__":
    prueba()
