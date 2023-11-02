"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres. 

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes. 

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.
"""

# Función para convertir un número a palotes
def to_palotes(number):
    palotes = ""
    cont = 0
    while number > 0:
        digit = number % 10
        if cont > 0:
            palotes = "-" + palotes
        for i in range(digit):
            palotes = "|" + palotes
        cont += 1
        number //= 10
    return palotes


# Programa principal
def main():
    number = int(input("Introduce un número: "))
    print(to_palotes(number))

main()