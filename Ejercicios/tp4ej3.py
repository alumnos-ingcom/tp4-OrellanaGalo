################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 3 - CONVERSION DE GRADOS  
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import IngresoIncorrecto

def ingreso_real(mensaje):
    ingreso = input(mensaje + ' #')
    try:
        real = float(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero valido!") from err
    return real

def convertir_a_fahrrenheit(centigrados):
    
    conversion = (centigrados * 9/5) + 32

    return conversion
    
def convertir_a_centigrados(fahrrenheit):

    conversion = (fahrrenheit - 32) * 5/9

    return conversion

def prueba():
    
    print("Bienvenido a mi convertidor de grados Celsius a Fahrrenheit y visceversa!")
    ingreso = ingreso_real("Ingrese cual de las 2 conversiones desea utilizar:\n'1' - Celsius a Fahrrenheit\n'2' - Fahrrenheit a Celsius\n")
    if ingreso == 1:
        centigrados = ingreso_real("Ingrese los grados Celsius que desee convertir:")
        resultado = convertir_a_fahrrenheit(centigrados)
        print ('Fahrrenheit: ', resultado)
    elif ingreso == 2:
        fahrrenheit = ingreso_real("Ingrese los grados Fahrrenheit que desee convertir")
        resultado = convertir_a_centigrados(fahrrenheit)
        print ('Celsius: ', resultado)
    else :
        print("El valor ingresado no corresponde a las funciones de este programa. Por favor, intentelo nuevamente.")

if __name__ == "__main__":
    prueba()
