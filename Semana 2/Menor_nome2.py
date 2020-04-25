lista_nomes = (['maria', '  josé      ', 'PAULO', 'Catarina'])

def menor_nome(listadeNomes):
    cop = []
    for nome in listadeNomes:
        cop.append(nome.strip(" ").capitalize())
        
    menornome = cop[0] 
    for nome in cop:
       if len(menornome) >= len(nome):
            menornome = nome
    return menornome


print(menor_nome(lista_nomes))