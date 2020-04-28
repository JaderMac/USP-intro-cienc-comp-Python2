def ordena(lista):
    tamanhoLista = len(lista)
    for i in range(tamanhoLista - 1):
        posicaoMenor = i
        for j in range(i+1, tamanhoLista):
            if lista[j] < lista[posicaoMenor]:
                posicaoMenor = j
        lista[i], lista[posicaoMenor] = lista[posicaoMenor], lista[i]
    return lista

def remove_repetidos(lista):
    controle = []
    for i in lista:
        if i not in controle:
            controle.append(i)
    ordena(controle)
    return controle

