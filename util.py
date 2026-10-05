def Buscar(lista, valor):
    for i in range(len(lista)):
        inicio = i
        fin = len(lista) - 1 - i

        if inicio > fin:
            break

        if lista[inicio] == valor:
            return True

        if lista[fin] == valor:
            return True

    return False
