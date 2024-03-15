class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.imprimir()
    
    def imprimir(self):
        print(f"su nombre es: {self.nombre}")

# main code

persona1 = Persona("Pedro")
persona2 = Persona("Juan")
