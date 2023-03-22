# PROGRAMA PARA ENCONTRAR LA LETRA SIGUIENTE Y ANTERIOR DE UNA LETRA INGRESADA

def next_letter_alphabet(letter):
    """
    Función que recibe una letra y 
    devuelve la siguiente y la anterior letra de la letra ingresada
    en el alfabeto español.

    :param letter: letra ingresada por el usuario.
    :return: letra siguiente y letra anterior en el alfabeto.

    """
    # Se define el alfabeto que se va a utilizar
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTVWXYZ"

    # Se encuentra la posición de la letra en el alfabeto
    letters = alphabet.find(letter)

    # Se define la letra que está anterior y después de la letra ingresada,
    # y se manejan los casos especiales para la primera y última letra del alfabeto.
    next_letter_after = alphabet[0] if letter == 'Z' else alphabet[letters + 1]
    next_letter_before = alphabet[-1] if letter == 'A' else alphabet[letters - 1]

    # Se imprime la letra siguiente y la letra anterior
    print(f"la letra siguiente es: {next_letter_after}")
    print(f"la letra anterior es: {next_letter_before}")

while True:
    # Se solicita al usuario ingresar una letra
    my_letter = input("Ingresa una letra (Escribe salir para terminar el programa): ")

    # Si se ingresa "salir" se termina el programa
    if my_letter == "salir":
        print("Has salido del programa, El programa ha terminado")
        break
    
    # Si se ingresa más de una letra, se solicita ingresar solo una letra
    if len(my_letter) != 1:
        print("Ingresa solo una letra")
        continue
    
    # Si se ingresa un número, se solicita ingresar una letra
    if my_letter.isnumeric():
        print("Dato incorrecto, Ingrese una letra")
        continue
    
    # Se llama a la función next_letter_alphabet y se convierte la letra ingresada a mayúscula
    next_letter_alphabet(my_letter.upper())
    