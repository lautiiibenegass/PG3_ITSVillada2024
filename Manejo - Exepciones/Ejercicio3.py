meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

try:
    mes = int(input("Ingrese el número del mes: "))
    print(meses[mes - 1])
except IndexError:
    print("Error. El número del mes debe ser entre 1 y 12.")