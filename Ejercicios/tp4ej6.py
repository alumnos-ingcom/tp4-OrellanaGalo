################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 6 - Maximo / Minimo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def construccion_lista ():
    lista=[]
    for i in range(5):
        numero = ingreso_entero("Ingrese un valor para sumarlo a la lista")
        lista.append(numero)
    return lista

def minimo(lista):
    
    minimo = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return [minimo]

def maximo(lista):
    
    maximo = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return [maximo]

def prueba():
    
    lista = construccion_lista()
    valor_minimo = minimo(lista)
    valor_maximo = maximo(lista)
    print("\nLos valores maximos y minimos de la lista son: ")
    print("Minimo:", valor_minimo[0])
    print("Maximo:", valor_maximo[0])
    
    pass

if __name__ == "__main__":
    prueba()
