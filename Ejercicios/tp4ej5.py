################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 5 - Numeros positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej3 import ingreso_real

def signo(numero):
    
    if numero < 0:
        print("El numero es negativo")
    elif numero > 0:
        print("El numero es positivo")
    else:
        print("El numero es igual a 0")

def prueba():
    numero = ingreso_real("Ingrese un numero para saber su signo:")
    signo(numero)
    pass

if __name__ == "__main__":
    prueba()
