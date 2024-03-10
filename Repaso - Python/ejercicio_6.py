def CantVocales(frase, vocales, contador):
    for i in frase:
        if i in vocales:
            contador += 1
        else:
            pass
    print(f'su frase tiene', contador, 'vocales')


contador = 0

vocales = ['A','a','E','e','I','i','O','o','U','u']

frase = str(input('ingrese una frase para descubrir su cantidad de vocales: '))

CantVocales(frase, vocales, contador)