def maiusculas(string):
    grandes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    saida = []
    for letra in string:
        if letra in grandes:
            saida.append(letra)
              
    return ''.join(map(str, saida))

print(maiusculas('PrOgRaMaMoS em python!'))

