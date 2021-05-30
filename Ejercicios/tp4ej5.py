################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 5 - Numeros positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej3 import ingreso_real

def signo(numero):
    
    if numero < 0:
        return -1
    elif numero > 0:
        return 1
    else:
        return 0

def prueba():
    
    numero = ingreso_real("Ingrese un numero para saber su signo:")
    print (f'\n 1 = Positivo\n-1 = Negativo\n 0 = Cero')
    resultado = signo(numero)
    print('\nSu numero corresponde a: ', resultado)

if __name__ == "__main__":
    prueba()
