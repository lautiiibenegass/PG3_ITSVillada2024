def IsInLista(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return f"El elemento {elemento} no se encuentra en la lista."
    
lista = [8, 12, 9, 45]

busqueda = int(input("Ingrese el elemento que desea buscar: "))

resultado = IsInLista(lista, busqueda)

print(f"El elemento {busqueda} esta en el índice {resultado} de la lista.")