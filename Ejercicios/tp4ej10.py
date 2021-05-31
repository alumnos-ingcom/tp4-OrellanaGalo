################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 10 - Factores primos 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def factores_primos(numero):
    
    numeros_primos = []
    for contador in range(2, numero + 1):
        while numero % contador == 0:
            numeros_primos.append(contador)
            numero = numero / contador
    return tuple(numeros_primos)

def prueba():
    
    print('Bienvenido!')
    ingreso = ingreso_entero('\nIngrese un numero entero para saber sus factores primos:')
    numeros_primos = factores_primos(ingreso)
    print(f'\nFactores primos de {ingreso}:', numeros_primos)

if __name__ == "__main__":
    prueba()
