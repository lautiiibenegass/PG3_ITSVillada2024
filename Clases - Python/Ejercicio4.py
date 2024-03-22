class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    
    def suma(self):
        print(f"Suma: {self.num1} + {self.num2} = {self.num1 + self.num2}")

    def resta(self):
        print(f"Resta: {self.num1} - {self.num2} = {self.num1 - self.num2}")

    def multiplicacion(self):
        print(f"Multiplicación: {self.num1} * {self.num2} = {self.num1 * self.num2}")

    def division(self):
        if self.num2 != 0:
            print(f"División: {self.num1} / {self.num2} = {self.num1 / self.num2}")
        else:
            print("No se puede dividir por cero.")

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operaciones = Operaciones(num1, num2)