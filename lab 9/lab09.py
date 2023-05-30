linhas = int(input())

matriz = []

for l in range(linhas):
    m = []
    for c in range(linhas):
        m.append(input())   
    matriz.append(m)

for l in range(linhas):
    for c in range(linhas):
        print( matriz[l][c] , end='')
    print()