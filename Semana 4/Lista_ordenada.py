def ordenada(lista):
    verifica = []
    for i in range(len(lista) - 1):
        if lista[i] <= lista[i + 1]:
            verifica.append(True)
        else: 
            verifica.append(False)
    
    for i in range(len(verifica)):
        if verifica[i] == False:
            return False
    return True
