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
pass

def convertir_a_fahrrenheit(centigrados):
    centigrados = ingreso_real("Ingrese los grados Celsius que desee convertir:")
    conversion = (centigrados * 9/5) + 32
    print(f"Fahrrenheit = {conversion}")
    pass
    
def convertir_a_centigrados(fahrrenheit):
    fahrrenheit = ingreso_real("Ingrese los grados Fahrrenheit que desee convertir")
    conversion = (fahrrenheit - 32) * 5/9
    print(f"Celsius = {conversion}")
    pass

def prueba():
    print("Bienvenido a mi convertidor de grados Celsius a Fahrrenheit y visceversa!")
    i = ingreso_real("Ingrese cual de las 2 conversiones desea utilizar:\n'1' - Celsius a Fahrrenheit\n'2' - Fahrrenheit a Celsius\n")
    if i == 1:
        convertir_a_fahrrenheit(1)
    elif i == 2:
        convertir_a_centigrados(1)
    else :
        print("El valor ingresado no corresponde a las funciones de este programa. Por favor, intentelo nuevamente.")
        
    pass

if __name__ == "__main__":
    prueba()
