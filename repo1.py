
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