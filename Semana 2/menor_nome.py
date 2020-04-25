lista_nomes = ["Ana - Zelda", "Gabriel Diniz", "Jéferson García", "Fabio RAC SJC Santana", "Letícia Menina-BOTO", "Micaela Rac Santana", 
"Teresa Stellinha", "Valvir Vinícius",  "Vinícius Coutinho"]

def menor_nome(listadeNomes):
    menornome = "abc"
    for nome in listadeNomes:
        if len(menornome) <= len(nome):
            menornome = nome

    return menornome.capitalize().strip()

print(menor_nome(lista_nomes))
#print(len(lista_nomes[]))