################
# Galo Orellana - @OrellanaGalo
# TP4 - Ejercicio 8 - Ordenar 3 valores 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def ordenar_mayor_a_menor(uno, dos, tres):
    
    v1 = min(uno, dos, tres)
    v3 = max(uno, dos, tres)
    v2 = (uno + dos + tres) - v1 - v3
    
    return v3, v2, v1
    
def ordenar_menor_a_mayor(uno, dos, tres):
    
    v1 = min(uno, dos, tres)
    v3 = max(uno, dos, tres)
    v2 = (uno + dos + tres) - v1 - v3
    
    return v1, v2, v3
              
def prueba():
    
    print('Ingrese 3 valores para ordenarlos de mayor a menor y visceversa!')
    uno = ingreso_entero("\nIngrese el primer entero:")
    dos = ingreso_entero("Ingrese el segundo entero:")
    tres = ingreso_entero("Ingrese el tercer entero:")
    mayor_a_menor = ordenar_mayor_a_menor(uno, dos, tres)
    menor_a_mayor = ordenar_menor_a_mayor(uno, dos, tres)
    print('\nOrden de mayor a menor: ', mayor_a_menor)
    print('\nOrden de menor a mayor: ', menor_a_mayor)
    

if __name__ == "__main__":
    prueba()
