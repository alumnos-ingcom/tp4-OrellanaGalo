################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 1 - Ingreso de numeros enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    
    """ Donde comienza // Cuando termina // Cuanto avanza """ 
    
    for i in range(0, cantidad_reintentos, 1):
        ingreso_entero("Puede ingresar 5 valores enteros.") 

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):

    print(mensaje)
    i = int(input("Numero a ingresar: "))
    if i < valor_minimo or i > valor_maximo:
        print ("Por favor. Solo ingresar numeros entre 0 y 10")
    elif i >= valor_minimo or i <= valor_maximo:
        print ("El numero ingresado es correcto. Muchas gracias por su colaboracion.")

class IngresoIncorrecto(Exception):
    """Esta es la excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(mensaje):
    
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un numero entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero!") from err
    return entero

def prueba():
    
    print(mensaje)
    ingreso_entero_reintento("Tenes 5 intentos para agregar un numero entero")
    ingreso_entero_restringido("Ingrese un numero entre 0 y 10")
    
    pass

if __name__ == "__main__":
    prueba()