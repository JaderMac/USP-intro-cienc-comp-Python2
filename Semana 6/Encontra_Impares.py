def encontra_impares(lista):
    if not len(lista):
        return 0
    else:
        impares = []
        for item in lista:
            if (item % 2) != 0:
                impares.append(item)
        return impares[:] + encontra_impares(lista[1:])

l = [1, 2, 3]
print( encontra_impares(l)) 