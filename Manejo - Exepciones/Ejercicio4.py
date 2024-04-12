def division():
    try:
        num1:int = int(input("Ingrese el primer número: "))
        num2:int = int(input("Ingrese el segundo número: "))
        print(f"Division: {num1} / {num2} = {num1 / num2}")
    except ZeroDivisionError:
        print("Error. No se puede dividir por cero.")
    except ValueError:
        print("Error. Debe ser un valor numerico.")


division()
