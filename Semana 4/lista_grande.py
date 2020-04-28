import random

def lista_grande(quantidade):
    lista = []
    for i in range(0, quantidade):
        lista.append(random.randint(0,99) )
    return lista
