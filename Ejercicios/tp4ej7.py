################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 7 - Restas sucesivas 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):

    cociente = 0
    while dividendo >= divisor :
        for i in range (divisor):
            dividendo = dividendo - divisor
            cociente = cociente + 1
            print(f"\n- {cociente} - {dividendo}")
        return dividendo
    else :
        print('hola')

def prueba():
    
    dividendo = ingreso_entero("Ingrese el dividendo")
    divisor = ingreso_entero("Ingrese el divisor")
    print(f"\nCUENTA: {dividendo}/{divisor}")
    resultado = division_lenta(dividendo, divisor)
    print("\nResultado de la operacion:", resultado)
    pass

if __name__ == "__main__":
    prueba()
