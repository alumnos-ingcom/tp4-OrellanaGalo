################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 4 - Comparacion de numeros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej3 import ingreso_real

def compara(numero, otro_numero):

    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else :
        return 1

def prueba():
    
    numero = ingreso_real("Ingrese el primer numero:")
    otro_numero = ingreso_real("Ingrese el segundo numero:")
    resultado = compara(numero, otro_numero)
    print('\nRetorna:', resultado)
    
if __name__ == "__main__":
    prueba()
