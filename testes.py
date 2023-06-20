tot_monstros = int(input())

for _ in range(tot_monstros):
    entrada_atributos_monstro = input().split()
    vida, ataque, tipo,(pos)  = int(entrada_atributos_monstro[0]), int(entrada_atributos_monstro[1]), entrada_atributos_monstro[2], entrada_atributos_monstro[3]

    print(vida)
    print(ataque)
    print(tipo)
    print(pos)