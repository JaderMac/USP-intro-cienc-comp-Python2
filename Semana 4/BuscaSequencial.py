def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

print(busca(['a', 'e', 'i'], 'e'))
print(busca([12, 13, 14], 15))