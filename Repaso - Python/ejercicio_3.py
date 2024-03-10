ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))
caracter = str(input("Ingrese un caracter: "))

for j in range(alto):
    for i in range(ancho):
        print(caracter, end='')
    print()
    