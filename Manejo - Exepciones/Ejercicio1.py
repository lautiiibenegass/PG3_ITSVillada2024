def suma():
    try:
        num1:int = int(input("Ingrese el primer número: "))
        num2:int = int(input("Ingrese el segundo número: "))
        print(f"Suma: {num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("Error. Debe ser un valor numerico.")

seguir = "si"
while seguir == "si":
    suma()
    seguir:str = str(input("Desea continuar sumando? \n >>> "))