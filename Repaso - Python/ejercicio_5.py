def EsPalindromo(palabra, arbalap):
    if palabra == arbalap:
        print('True (su palabra es capicua)')
    else:
        print('False (su palabra no es capicua)')



palabra = str(input('ingrese una palabra para descubrir si es un palindromo: '))
arbalap = palabra[::-1]

EsPalindromo(palabra, arbalap)
