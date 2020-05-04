def incomodam(numero):
    if numero <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(numero - 1)

def elefantes(numero):
    if numero == 1:
        return "Um elefante incomoda muita gente"
    elif numero == 2:
        return elefantes(numero - 1) + f"\n{numero} elefantes " + incomodam(numero) + "muito mais" 
    elif numero > 2:
        frase1 = f"\n{numero - 1} elefantes incomodam muita gente"
        frase2 = f"\n{numero} elefantes " + incomodam(numero) + "muito mais"
        return elefantes(numero-1) + frase1 +frase2
    else:
        return ""

#print(elefantes(0))
#print(elefantes(1))
#print(elefantes(2))
#print(elefantes(3))
print(elefantes(4))
            