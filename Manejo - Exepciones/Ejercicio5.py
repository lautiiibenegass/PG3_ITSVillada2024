try:
    with open("strings.txt", "w") as file:
        series = ["Hola", "Mundo", "Python", "OpenAI"]
        for string in series:
            file.write(string + "\n")
            # Simulamos un error al intentar escribir un entero
            if string == "Mundo":
                file.write(42)  # Intentamos escribir un entero
except TypeError as e:
    print("Se produjo un error al escribir en el archivo:", e)