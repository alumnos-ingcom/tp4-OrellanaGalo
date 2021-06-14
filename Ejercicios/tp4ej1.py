################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 1 - Ingreso de numeros enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

class IngresoIncorrecto(Exception):
    """Esta es la excepcion para el ingreso incorrecto"""
    pass

class SinIntentos(Exception):
    """Esta es la excepcion para el reintento de ingreso en la funcion 'ingreso_entero_reintento'."""
    pass

class SinParametro(Exception):
    """Esta es la excepcion para establecer los parametros en la funcion 'ingreso_entero_restringido'."""
    pass

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    
    intentos = 0
    entero = None
    
    while entero == None and intentos < cantidad_reintentos:
        entero = ingreso_entero(mensaje)
        intentos = intentos - 1
        if entero == None:
            print('Intentos restantes: ', intentos)
    if intentos == cantidad_reintentos:
        raise SinIntentos('Se han terminado las oportunidades de reintentos.')
    return entero

def ingreso_entero_restringido(mensaje, valor_minimo, valor_maximo):

    entero = ingreso_entero(mensaje)
    
    try:
        if entero >= valor_minimo and entero <= valor_maximo:
            return entero
        else:
            raise SinParametro('El numero ingresado se encuentra fuera de los parametros establecidos.')
    except TypeError as err:
        raise TypeError ('Ingrese solo numeros enteros.') from err

def ingreso_entero(mensaje):
    
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un numero entero.
    """
    try:
        entero = int(input(mensaje + " #"))
        return entero
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero!") from err
        return entero

def prueba():
    
    print('Bienvenido a mi codigo!')
    ingreso_usuario = ingreso_entero_reintento("\nTenes 5 intentos para agregar un numero entero")
    ingreso_usuario2 = ingreso_entero_restringido("Ingrese un numero entre 0 y 10", 0, 10)
    print(f'El numero ingresado fue: {ingreso_usuario}')
    print(f'El segundo numero ingresado fue: {ingreso_usuario2}')


if __name__ == "__main__":
    prueba()