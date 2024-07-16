'''Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.'''
try:
    tam = int(input("Escribir el tamaño de la lista: "))  #Se elige el tamaño de la lista.
except ValueError:
    print("Escribir un valor correcto")
lista = [] #La lista donde se van a anexar los valores que el usuario desee posteriormente.
a : int = 0   #El valor con el que va a comparar el loop while para su funcionamiento.

while a < tam:
    try:
        lis = int(input("Escribir números para la lista: ")) #Se comienzan a escribir los valores de la lista.
        lista.append(lis) #Añade lo que está dentro de la lista.
        a += 1
    except ValueError:
        print("Escribir un valor correcto")    
    
print(lista)  #Muestra la lista en el terminal.

def sumi(listap: list):  #Formamos la función que va a buscar la mayor suma de dos consecutivos.
    mayor = listap[0] + listap[1] #La función toma de referencia el 1er y 2do valor de la lista del usuario.
    for i in range(len(listap) - 1):  # Rango ajustado para ir hasta el penúltimo elemento
        sumar = listap[i] + listap[i + 1]
        if sumar > mayor:
            mayor = sumar
    return mayor

print("La mayor suma entre dos elementos consecutivos es:", sumi(lista))
