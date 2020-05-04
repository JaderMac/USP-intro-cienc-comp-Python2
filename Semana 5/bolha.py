def bubble_sort(lista):
    for ultimo in range(len(lista)-1,0,-1):
        for i in range(ultimo):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                print(lista)
    return lista