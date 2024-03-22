class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))
    
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = int(input("Ingrese el sueldo del empleado: "))

    def imprimir_datos(self):
        super().imprimir_datos()
        print("Sueldo:", self.sueldo)

    def pagar_impuestos(self):
        if self.sueldo >= 3000:
            print("Paga impuestos")
        else:
            print("No paga impuestos")



#main code
persona = Persona("", 0)
persona.cargar_datos()
persona.imprimir_datos()

print("---------------------------------------")

empleado = Empleado("", 0, 0)
empleado.pagar_impuestos()
empleado.cargar_datos()
empleado.imprimir_datos()