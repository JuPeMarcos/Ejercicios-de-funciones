"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. 
Recuerda que puedes usar unas dentro de otras si es necesario.
Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, 
te puedes ahorrar mucho trabajo. Por ejemplo, la función is_palindromic() resulta trivial teniendo turn() y 
la función next_prime() también es muy fácil de implementar teniendo is_prime().

Está prohibido usar funciones de conversión del número a una cadena.

is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
digits: devuelve el número de dígitos de un número entero.
turn: le da la vuelta a un número.
digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
remove_behind: le quita a un número n dígitos por detrás (por la derecha).
remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
paste_behind: añade un dígito a un número por detrás.
paste_ahead: añade un dígito a un número por delante.
piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
put_numbers_together: pega dos números para formar uno.
Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.
"""

# Función para verificar si un número es capicúa (palíndromo)
def is_palindromic(number):
    return number == turn(number)

# Función para verificar si un número es primo
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Función para encontrar el siguiente número primo mayor que el número dado
def next_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number
        number += 1

# Función para contar el número de dígitos en un número
def digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

# Función para dar vuelta a un número
def turn(number):
    reversed_number = 0
    while number > 0:
        reversed_number = (reversed_number * 10) + (number % 10)
        number //= 10
    return reversed_number

# Función para obtener un dígito en una posición específica de un número
def digit_n(number, n):
    num = abs(number)
    num =turn(num)
    for i in range(n):
        num //= 10 
    return num % 10

# Función para encontrar la posición de la primera ocurrencia de un dígito en un número
def digit_position(number, digit):
    position = 0
    while number > 0:
        if number % 10 == digit:
            return position
        number //= 10
        position += 1
    return -1

# Función para quitar dígitos de la derecha de un número
def remove_behind(number, n):
    return number // 10**n

# Función para quitar dígitos de la izquierda de un número
def remove_ahead(number, n):
    return number % 10**(digits(number) - n)

# Función para agregar un dígito a la derecha de un número
def paste_behind(number, digit):
    return (number * 10) + digit

# Función para agregar un dígito a la izquierda de un número
def paste_ahead(number, digit):
    return (digit * 10**digits(number)) + number

# Función para obtener un fragmento de un número entre las posiciones inicial y final
def piece_of_number(number, start, end):
    num_digits = digits(number)
    if start < 0:
        start = 0
    if end >= num_digits:
        end = num_digits - 1
    return (number // 10**start) % 10**(end - start + 1)

# Función para unir dos números
def put_numbers_together(number1, number2):
    return (number1 * 10**digits(number2)) + number2

# Ejemplos de uso de las funciones
def main():
    # Pruebas de las funciones
    num = 12321
    print("is_palindromic(12321):", is_palindromic(num))

    prime_num = 17
    print("is_prime(17):", is_prime(prime_num))
    print("next_prime(17):", next_prime(prime_num))

    num_digits_count = 12345
    print("digits(12345):", digits(num_digits_count))

    num_to_reverse = 12345
    print("turn(12345):", turn(num_to_reverse))

    num_to_get_digit = 12345
    print("digit_n(12345, 2):", digit_n(num_to_get_digit, 2))

    num_to_find_position = 12345
    digit_to_find = 4
    print("digit_position(12345, 4):", digit_position(num_to_find_position, digit_to_find))

    num_to_remove_behind = 12345
    n_to_remove = 2
    print("remove_behind(12345, 2):", remove_behind(num_to_remove_behind, n_to_remove))

    num_to_remove_ahead = 12345
    n_to_remove = 2
    print("remove_ahead(12345, 2):", remove_ahead(num_to_remove_ahead, n_to_remove))

    num_to_paste_behind = 123
    digit_to_paste = 4
    print("paste_behind(123, 4):", paste_behind(num_to_paste_behind, digit_to_paste))

    num_to_paste_ahead = 123
    digit_to_paste = 4
    print("paste_ahead(123, 4):", paste_ahead(num_to_paste_ahead, digit_to_paste))

    num_to_slice = 123456
    start_position = 2
    end_position = 4
    print("piece_of_number(123456, 2, 4):", piece_of_number(num_to_slice, start_position, end_position))

    num1 = 123
    num2 = 45
    print("put_numbers_together(123, 45):", put_numbers_together(num1, num2))

# Inicio del programa
main()
