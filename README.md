# RETO1
Reto 1 programación oreitnada a objetos

## Reto 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.

En este reto utilizamos una función con unas variables, 2 de tipo int que van a ser los valores que van a pasar por una operación. Nos aseguramos que esos valores sean de tipo int y el último valor que sea de tipo str dónde el usuario va a seleccionar qué clase de operación desea realizar. 
```python


def repo(x:int,y:int,z:str):
    print("Salida: ")
    if z == "+":
        return x+y
    elif z== "-":
        return x-y
    elif z== "*":
        return x*y
    elif z== "/":
        if y==0:
            return "Operación no válida"
        else:
            return x/y
    else:
        return "Operación no válida"
    

print("Elija la operación que desea realizar: +, -, *, /")
try:
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    z = input("Ingrese el operador: ")

    resultado = repo(x, y, z)
    print("Salida:", resultado)
except ValueError:
    print("Error: Entrada inválida. Por favor, ingrese números válidos.")
except Exception as e:
    print(f"Error inesperado: {e}")
```

## Reto 2:
Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

En este reto el usuario digita una palabra, la cual se convierte en tipo string. Este string va a servir para trabajar con la función que va a manejarse a partir de valores booleanos, donde sí la condición cambia va a negar que sea políndromo; de lo contrario va a retornar que efectivamente es un políndromo. 
```python 
palabra = input("Ingrese una palabra: ") #El usuario digita una palabra. 
if not palabra.isalpha():
    print("Error: Ingrese una palabra válida.")
    exit()
else:
    palabra = list(palabra) #Esa palabra se convierte en una lista para poder acceder a ella luego.  
try:
    def repo2(x: list): #Utilizamos una función que recibe una lista.
        palindroma = True #Variable de booleano que cambiará si la condición de palindroma no se cumple.
        i = 0 #Inicializador para el loop.

        while i < len(x)//2:  #Loop  que se ejecuta si el inicializador es menor a la mitad de la longitud de la lista.
            if x[i] != x[-(i+1)]:  #Condición que corta el booleano y transforma el booleano si al leer los caracteres desde adelante y desde atrás no coinciden.
                palindroma = False #Transformación del booleano a Falso si no cumple la idea de palindromo.
                break 
            i += 1 #Se aumenta el incializador si la condición se cumple.

        if palindroma: #Si palindroma sigue siendo True se enseñará en la terminal.
            print("Es palíndroma")
        else: #Y si no se enseñará en terminal que no es.
            print("No es palíndroma")

    repo2(palabra) #Ejecución de la función.

except Exception as e: #Captura de errores.
    print(f"Error inesperado: {e}") #Mensaje de error en caso de que haya un error inesperado. 
```

## Reto 3: 
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

En este reto, el usuario proporciona una lista de números que luego se procesa para identificar los números primos. Se utiliza un bucle `while` para recopilar los números y una función `repo3` para determinar si un número es primo. Dentro de `repo3`, se itera sobre cada número de la lista y se verifica si es divisible por algún número menor que él mismo. Si un número no es divisible por ningún número menor que él mismo (excepto 1), se considera primo y se agrega a una lista de números primos. Finalmente, se muestra la lista de números primos en la terminal.

```python 
try:
    ln = int(input("Escribir el tamaño de la lista: ")) #Se elige el tamaño de la lista.
except Exception as e:
    print(f"Error inesperado: {e}")
    
numbers = [] #La lista donde se van a anexar los valores que el usuario desee posteriormente.
a : int = 0  #El valor con el que va a comparar el loop while para su funcionamiento.
while a < ln:
    try:
        number = int(input("Escribir un número: "))
        numbers.append(number)
        a += 1
    except ValueError:
        print("Escribir un valor coorrecto")



def repo3(numb : list):
    primolist = []
    for i in numb: #Se itera sobre la lista de números.
        primo = True #El booleano que permite saber si un número es primo o no.
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            primolist.append(i)
    return primolist


print("Los números primos son:", repo3(numbers))
  


```

## Reto 4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

En el reto, el usuario proporciona el tamaño de una lista y luego ingresa los valores de la lista. El programa se asegura de que los valores ingresados sean números enteros y luego muestra la lista en la terminal. Después, se define una función llamada `sumi` que busca la mayor suma entre dos elementos consecutivos en la lista. La función itera sobre la lista, sumando cada par de elementos consecutivos y comparando con la suma más grande encontrada hasta el momento. Si una suma es mayor que la suma más grande anterior, se actualiza la variable `mayor` con ese valor. Finalmente, se muestra en la terminal la mayor suma entre dos elementos consecutivos en la lista proporcionada por el usuario.

```python
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

  ```

## Reto 5:
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`

La función anagrama busca anagramas en una lista de palabras. Si la lista está vacía, retorna una lista vacía. De lo contrario, toma la primera palabra como referencia y compara las demás con ella. Si las palabras tienen la misma longitud y los mismos caracteres (o si se pueden reorganizar para que coincidan), se agregan al conjunto de anagramas. Finalmente, se retorna una lista con los anagramas encontrados.

```python
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

```


¡Gracias!
