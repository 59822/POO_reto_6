# RETO1
Reto 1 programación oreitnada a objetos

## Reto 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.

En este reto utilizamos una función con unas variables, 2 de tipo int que van a ser los valores que van a pasar por una operación. Nos aseguramos que esos valores sean de tipo int y el último valor que sea de tipo str dónde el usuario va a seleccionar qué clase de operación desea realizar. 
```python

def repo(x:int,y:int,z:str): #La función pide 3 variables, 2 para numeros y 1 para elegir el operador.
    print("Salida: ")
    if z == "+":
        return x+y   #Si la varaible del operador es "+" se retorna una suma.
    elif z== "-":
        return x-y   #Si la varaible del operador es "-" se retorna una resta. 
    elif z== "*":
        return x*y   #Si la varaible del operador es "*" se retorna una multiplicación. 
    elif z== "/":    #Si la varaible del operador es "/" se retorna una división.
        if y==0:
            return "Operación no válida" #Se valida que el divisor no sea 0 para una evitar una indeterminación
        else:
            return x/y  
    else:
        return "Operación no válida"
    


x= int(input("Ingrese el primer número: "))  #Se le pide al usuario que escriba los valores.
y= int(input("Ingrese el segundo número: "))
print("Elija la operación que desea realizar: +, -, *, /")  
z= input("*Ingrese el operador*: ")

print(repo(x,y,z))  #Se muestran los valores de las variables sobre su respectiva operación.

```

## Reto 2:
Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

En este reto el usuario digita una palabra, la cual se convierte en tipo string. Este string va a servir para trabajar con la función que va a manejarse a partir de valores booleanos, donde sí la condición cambia va a negar que sea políndromo; de lo contrario va a retornar que efectivamente es un políndromo. 
```python 
palabra = input("Ingrese una palabra: ") #El usuario digita una palabra. 
palabra = list(palabra) #Esa palabra se convierte en una lista para poder acceder a ella luego.  

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
```

## Reto 3: 
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

En este reto, el usuario proporciona una lista de números que luego se procesa para identificar los números primos. Se utiliza un bucle `while` para recopilar los números y una función `repo3` para determinar si un número es primo. Dentro de `repo3`, se itera sobre cada número de la lista y se verifica si es divisible por algún número menor que él mismo. Si un número no es divisible por ningún número menor que él mismo (excepto 1), se considera primo y se agrega a una lista de números primos. Finalmente, se muestra la lista de números primos en la terminal.

```python 
ln = int(input("Escribir el tamaño de la lista: ")) #Se elige el tamaño de la lista.
numbers = [] #La lista donde se van a anexar los valores que el usuario desee posteriormente.
a : int = 0  #El valor con el que va a comparar el loop while para su funcionamiento.
while a < ln:
    a += 1
    number = int(input("Escribir un número: "))
    if type(number) != int:
        print("Escribir un número válido")
    else:
        numbers.append(number) #Se conforma la lista con los valores del usuario de tipo int.


def repo3(numb : list):
    primolist = []
    for i in numb: #Se itera sobre la lista de números.
        primo = True #El booleano que permite saber si un número es primo o no.
        if i <= 1: #Si el número es menor o igual a 1, no es primo.
            continue
        for j in range(2, i): #Se itera sobre el rango de 2 a i.
            if i % j == 0: #Si el residuo de la división de i entre j es 0, el número no es primo.
                primo = False #El booleano se convierte en falso.
                break
        if primo:
            primolist.append(i) #Si el número es primo, se añade a la lista de primos.
    return primolist


print("Los números primos son:", repo3(numbers)) #Muestra en el terminal los números primos de la lista.
```

## Reto 4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

En el reto, el usuario proporciona el tamaño de una lista y luego ingresa los valores de la lista. El programa se asegura de que los valores ingresados sean números enteros y luego muestra la lista en la terminal. Después, se define una función llamada `sumi` que busca la mayor suma entre dos elementos consecutivos en la lista. La función itera sobre la lista, sumando cada par de elementos consecutivos y comparando con la suma más grande encontrada hasta el momento. Si una suma es mayor que la suma más grande anterior, se actualiza la variable `mayor` con ese valor. Finalmente, se muestra en la terminal la mayor suma entre dos elementos consecutivos en la lista proporcionada por el usuario.

```python
tam = int(input("Escribir el tamaño de la lista: "))  #Se elige el tamaño de la lista.
lista = [] #La lista donde se van a anexar los valores que el usuario desee posteriormente.
a : int = 0   #El valor con el que va a comparar el loop while para su funcionamiento.
while a <= tam:
    a+=1
    lis = int(input("Escribir números para la lista: ")) #Se comienzan a escribir los valores de la lista.
    if type(lis) != int:  #Nos aseguramos de que los valores sean de tipo int.
        print("Escribir un número valido")
    else:
        lista.append(lis) #Añade lo que está dentro de la lista.
    if a == tam :
        break  #Se asegura que la lista contenga la cantidad que previamente el usuario deseó.
    
print(lista)  #Muestra la lista en el terminal.

def sumi(listap: list):  #Formamos la función que va a buscar la mayor suma de dos consecutivos.
    mayor = listap[0] + listap[1] #La función toma de referencia el 1er y 2do valor en suma para encontrar la suma consecutiva en la lista del usuario.
    for i in range(len(listap) - 1):  #Rango ajustado para ir hasta el penúltimo elemento.
        sumar = listap[i] + listap[i + 1]  #Comienza a comparar cada uno de los valores consecutivos de la lista con un iterador con la variable sumar.
        if sumar > mayor: #Si la suma de los valores que toma el iterador es mayor a la referencia inicial. La variable de referencia se convierte en la variable sumar.
            mayor = sumar
    return mayor #Retorna la variable con la mayor suma de consecutivos.

print("La mayor suma entre dos elementos consecutivos es:", sumi(lista))
#Muestra en el terminal la mayor suma.
  ```

## Reto 5:
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`

La función anagrama busca anagramas en una lista de palabras. Si la lista está vacía, retorna una lista vacía. De lo contrario, toma la primera palabra como referencia y compara las demás con ella. Si las palabras tienen la misma longitud y los mismos caracteres (o si se pueden reorganizar para que coincidan), se agregan al conjunto de anagramas. Finalmente, se retorna una lista con los anagramas encontrados.

```python
def anagrama(listap): #Formamos la función que va a buscar los anagramas.
    if not listap: #Si la lista está vacía, no hay anagramas. 
        return [] #Retorna una lista vacía.

    pal1 = listap[0] #La primera palabra de la lista se convierte en la referencia para buscar anagramas.
    paligual = {pal1} #Se crea un conjunto con la primera palabra para comparar con las demás.

    # Calcular la longitud de la primera palabra
    longitud_pal1 = len(pal1)

    for palabra in listap[1:]: 
        # Verificar si la longitud de la palabra actual es la misma que la de la primera palabra
        if len(palabra) != longitud_pal1:
            continue

        # Verificar si los caracteres de la palabra actual son los mismos que los de la primera palabra
        if set(palabra) == set(pal1): #Set para que no se repitan los caracteres.
            paligual.add(palabra)
            continue

        # Verificar si los caracteres de la palabra actual se pueden reorganizar para que coincidan con la primera palabra
        if len(set(palabra)) == len(set(pal1)): #Si la longitud de los caracteres de la palabra actual es igual a la de la primera palabra.
            pal_or = ''.join(sorted(palabra)) #Se ordenan las letras de la palabra. Join para unir las letras.
            pal1_or = ''.join(sorted(pal1)) #Se ordenan las letras de la primera palabra.
            if pal_or == pal1_or:
                paligual.add(palabra)

    return list(paligual)

lista = ["amor", "roma", "perro", "ayuda", "mora", "ramo", "roma"]
result = anagrama(lista)
print(result)  
```


¡Gracias!
