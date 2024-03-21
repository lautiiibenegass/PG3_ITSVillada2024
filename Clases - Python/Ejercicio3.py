class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lados)
        print("El lado mayor del triángulo es:", lado_mayor)

    def es_equilatero(self):
        if self.lados[0] == self.lados[1] == self.lados[2]:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")

# Solicitar al usuario que ingrese los valores de los lados
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Crear un objeto Triangulo con los valores ingresados por el usuario
triangulo = Triangulo(lado1, lado2, lado3)
triangulo.imprimir_lado_mayor()
triangulo.es_equilatero()