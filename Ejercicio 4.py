"""
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres. 

Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar que funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Los números en Morse los puedes encontrar aquí.
"""

# Función para convertir un número a Morse
def to_morse(number):
    morse_dict = {
        '0': "-----",
        '1': ".----",
        '2': "..---",
        '3': "...--",
        '4': "....-",
        '5': ".....",
        '6': "-....",
        '7': "--...",
        '8': "---..",
        '9': "----."
    }
    
    number_str = str(number)
    morse = ""
    for digit in number_str:
        if digit in morse_dict:
            morse += morse_dict[digit] + " "
    
    return morse


# Programa principal
def main():
    number = int(input("Introduce un número: "))
    print(to_morse(number))

main()

