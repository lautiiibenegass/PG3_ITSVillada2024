ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))
caracter = str(input("Ingrese un caracter: "))

def dibujar_cuadrado(ancho, alto, caracter):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end="")
        print()
    
def dibujar_triangulo(base, caracter):
    for i in range(1, base + 1):
        print(caracter * i)

figura = input("¿Qué figura deseas dibujar? (cuadrado/triángulo): ")


if figura == "cuadrado":
    ancho = int(input("Ingrese el ancho: "))
    alto = int(input("Ingrese el alto: "))
    caracter = input("Ingrese el carácter: ")
    dibujar_cuadrado(ancho, alto, caracter)
elif figura == "triángulo":
    base = int(input("Ingrese la base: "))
    caracter = input("Ingrese el carácter: ")
    dibujar_triangulo(base, caracter)
else:
    print("Figura no válida. Por favor, elige 'cuadrado' o 'triángulo'.")