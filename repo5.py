try:
    tam = int(input("Escribir el tamaño de la lista: "))
except ValueError:
    print("Escribir un valor correcto")
    exit()
    
lista = []
a = 0       #Creates variables for the list and the pivot
while a < tam:
    try:
        lis = input("Escribir las palabras para la lista: ")
        lista.append(lis)
        a += 1
    except ValueError:
        print("Escribir un valor correcto")
    

def mismos_caracteres(lista):
    resultado = []
    for i in lista:
        if len(i) != len(lista[0]):
            if sorted(i) == sorted(lista[0]):  
                resultado.append(i)
    return resultado

print(mismos_caracteres(lista))
