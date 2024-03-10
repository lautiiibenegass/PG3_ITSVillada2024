def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return f"{anio} es bisiesto."
    else:
        return f"{anio} no es bisiesto."

anio_usuario = int(input("Ingrese un año: "))

resultado = es_bisiesto(anio_usuario)

print(resultado)
