################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 7 - Restas sucesivas 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):

    cociente = 0
    variables=[]
    while dividendo >= divisor :
        dividendo = dividendo - divisor
        cociente = cociente + 1
    variables.append(dividendo)
    variables.append(cociente)
    if divisor == 0:
        return 0 # Esto lo deberia haber retornado en Prueba pero bueno, a caballo regalado no se le miran los dientes...
    return variables

def prueba():
    
    dividendo = ingreso_entero("Ingrese el dividendo")
    divisor = ingreso_entero("Ingrese el divisor")
    
    print(f"\nCUENTA: {dividendo}/{divisor}")
    resultado = division_lenta(dividendo, divisor)
    print('\nEl cociente es: ', resultado[1])
    print("\nResto de la operacion es:", resultado[0])

if __name__ == "__main__":
    prueba()
