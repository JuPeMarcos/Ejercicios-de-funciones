"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las 
dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un 
mensaje de error. El menú se volverá a mostrar, a menos que no se de a la opción terminar.
Modifica el programa anterior para que la introducción de las variables sea una opción del menú 
(la primera). Las variables se inicializan a cero.
Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente 
no se puedan ejecutar el resto de las opciones.
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, 
pide una opción (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función. 
"""
# Función que muestra el menú y devuelve la opción elegida
def menu(optionmenu):
    for x in optionmenu:
        print(x)
    option = int(input("Introduce una opción: "))
    return option

# Funciones que realizan las operaciones
def sumar(a, b):
    print("La suma es:", a + b)

def restar(a, b):
    print("La resta es:", a - b)

def multiplicar(a, b):
    print("La multiplicación es:", a * b)

def dividir(a, b):
    if b != 0:
        print("La división es:", a / b)
    else:
        print("No se puede dividir por cero")

# Función principal
def main():
    a = 0
    b = 0
    optionmenu = ["1. Sumar", "2. Restar", "3. Multiplicar", "4. Dividir", "5. Terminar"]
    option = menu(optionmenu)
    while option != 5:
        if option == 1:
            a = int(input("Introduce el primer valor: "))
            b = int(input("Introduce el segundo valor: "))
            sumar(a, b)
        elif option == 2:
            a = int(input("Introduce el primer valor: "))
            b = int(input("Introduce el segundo valor: "))
            restar(a, b)
        elif option == 3:
            a = int(input("Introduce el primer valor: "))
            b = int(input("Introduce el segundo valor: "))
            multiplicar(a, b)
        elif option == 4:
            a = int(input("Introduce el primer valor: "))
            b = int(input("Introduce el segundo valor: "))
            dividir(a, b)
        else:
            print("Opción incorrecta")
        option = menu(optionmenu)
    print("Fin del programa")

# Inicio del programa
main()