creacion_lista = input('ingrese los elementos de la lista separados por espacios: ')

lista = creacion_lista.split()

lista = [int(elemento) for elemento in lista]

lista.sort(reverse=True)

print(lista)