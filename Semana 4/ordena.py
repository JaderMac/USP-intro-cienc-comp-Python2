import random

def lista_grande(quantidade):
    lista = []
    for i in range(0, quantidade):
        lista.append(random.randint(0,99) )
    return lista


def ordena(lista):
    tamanhoLista = len(lista)
    for i in range(tamanhoLista - 1):
        posicaoMenor = i
        for j in range(i+1, tamanhoLista):
            if lista[j] < lista[posicaoMenor]:
                posicaoMenor = j
        lista[i], lista[posicaoMenor] = lista[posicaoMenor], lista[i]
    return lista

teste =lista_grande(9)
print(ordena(teste))
