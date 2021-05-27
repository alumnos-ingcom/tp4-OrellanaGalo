################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 2 - SUMA LENTA
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def suma_lenta(numero, otro_numero):
    
    for i in range (0, otro_numero, 1):
        numero = numero + 1
        print(f"{numero}")
    return numero

def prueba():
    
    print("Bienvenido a mi codigo!")
    print("Por favor, ingrese 2 numeros para ejecutar la SUMA LENTA.")
    numero = ingreso_entero("Ingrese un numero:")
    otro_numero = ingreso_entero("Ingrese otro numero:")
    suma_lenta(numero, otro_numero)

if __name__ == "__main__":
    prueba()

