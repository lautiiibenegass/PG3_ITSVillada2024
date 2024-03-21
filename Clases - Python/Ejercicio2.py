class Alumno:
    def __init__(self, nombre: str, nota: int):
        self.nombre = nombre
        self.nota = nota
        self.imprimir()
    
    def imprimir(self):
        print(f"su nombre es: {self.nombre} y su nota es: {self.nota}")
        if self.nota >= 4:
            print("Es regular")
        else:
            print("Esta libre")

# main code
print("---------------------------------------")
alumno1 = Alumno("Pedro", 6)
print("---------------------------------------")
alumno2 = Alumno("Juan", 3)
print("---------------------------------------")