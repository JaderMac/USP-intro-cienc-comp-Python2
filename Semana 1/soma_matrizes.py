def soma_matrizes(m1, m2):
    m3 = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for linha in range( len(m1) ):
            m3.append([])
            for coluna in range( len(m1[0]) ):
                m3[linha].append(m1[linha][coluna] + m2[linha][coluna])

        return m3
    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))