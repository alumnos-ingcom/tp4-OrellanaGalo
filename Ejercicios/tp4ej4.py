################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 4 - Comparacion de numeros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej3 import ingreso_real

def compara(numero, otro_numero):
    numero = ingreso_real("Ingrese el primer numero:")
    otro_numero = ingreso_real("Ingrese el segundo numero:")
    if numero < otro_numero:
        print("-1")
    elif numero == otro_numero:
        print("0")
    else :
        print("1")

def prueba():
    compara(1,1)
    pass

if __name__ == "__main__":
    prueba()
