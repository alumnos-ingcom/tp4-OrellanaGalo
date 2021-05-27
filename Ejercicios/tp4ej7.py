################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 7 - Restas sucesivas 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):

    contador = 0
    for i in range (0, divisor, 1):
        dividendo = dividendo -  divisor
        contador = contador + 1
    return dividendo 

def prueba():
    
    dividendo = ingreso_entero("Ingrese el dividendo")
    divisor = ingreso_entero("Ingrese el divisor")
    print(f"\nCUENTA: {dividendo}/{divisor}")
    resultado = division_lenta(dividendo, divisor)
    print("\nResultado de la operacion:", resultado)
    pass

if __name__ == "__main__":
    prueba()
