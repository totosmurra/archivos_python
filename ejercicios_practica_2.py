# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from os import close


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo)
    
    stock = list(csv.DictReader(csvfile))

    csvfile.close()

    print (stock)

    suma_tornillos = 0

    lista_con_los_numeros = []


    for i in stock:
        lista_con_los_numeros.append(i['tornillos'])

    
    lista_con_los_numeros = [int(i) for i in lista_con_los_numeros]

    suma_tornillos = sum(lista_con_los_numeros)
        
    
    print (suma_tornillos)




def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo)
    
    props = list(csv.DictReader(csvfile))

    csvfile.close()

    ambs2 = 0

    ambs3 = 0

    for i in props:
        try:
            if i['ambientes'] == '2':
                ambs2 += 1
            elif i['ambientes'] == '3':
                ambs3 += 1
        except:
            continue

    print("Dos Ambientes:", ambs2)    
    print("Tres Ambientes", ambs3)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
