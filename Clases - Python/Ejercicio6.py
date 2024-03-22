class Familia:
    def __init__(self):
        self.nombre_padre = input("Ingrese el nombre del padre: ")
        self.nombre_madre = input("Ingrese el nombre de la madre: ")
        self.hijos = []

        num_hijos = int(input("Ingrese el número de hijos: "))
        for i in range(num_hijos):
            nombre_hijo = input(f"Ingrese el nombre del hijo {i + 1}: ")
            self.hijos.append(nombre_hijo)
    
    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.nombre_padre}, Madre: {self.nombre_madre}, Hijos: {hijos_str}"

# Ejemplo de uso
familia_ejemplo = Familia()
print(familia_ejemplo)