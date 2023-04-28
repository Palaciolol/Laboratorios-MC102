# Calculadora de genoma.


def reverter(genoma, i, j):
    inverso = ''
    sobrou1 = ''
    sobrou2 = ''
    if i > len(genoma):
        return genoma

    elif j > len(genoma):
        j = len(genoma)-1
    for letra in range(j, i-1, -1):
        inverso = inverso + genoma[letra]

    c = j+1
    while c < len(genoma):
        sobrou2 = sobrou2 + genoma[c]

        c += 1

    c = 0
    while c < i:
        sobrou1 = sobrou1 + genoma[c]

        c += 1

    return sobrou1 + inverso + sobrou2


def transpor(genoma, i, j, k):
    pedaco1 = ''
    pedaco2 = ''
    sobrou1 = ''
    sobrou2 = ''

    if (j > len(genoma)) or (i > len(genoma)):
        return genoma

    elif k > len(genoma):
        k = len(genoma)-1
    for letra in range(i, j+1, 1):
        pedaco1 = pedaco1 + genoma[letra]

    for w in range(j+1, k+1, 1):
        pedaco2 = pedaco2 + genoma[w]

    c = 0
    while c < i:
        sobrou1 = sobrou1 + genoma[c]

        c += 1

    d = k+1
    while d < len(genoma):
        sobrou2 = sobrou2 + genoma[d]

        d += 1

    return sobrou1 + pedaco2 + pedaco1 + sobrou2


def combinar(genoma, txt, i):
    genoma_novo = txt
    sobrou1 = ''
    sobrou2 = ''
    for c in range(0, i):
        sobrou1 = sobrou1 + genoma[c]

    for d in range(i, len(genoma)):
        sobrou2 = sobrou2 + genoma[d]

    return sobrou1 + genoma_novo + sobrou2


def concatenar(genoma, txt):
    return genoma + txt


def remover(genoma, i, j):
    if i > len(genoma):
        return genoma
    elif j > len(genoma):
        j = len(genoma)-1
    return genoma[0:i]+genoma[j+1:]


def buscar(genoma, txt):
    print(genoma.count(txt))


def buscar_bidirecional(genoma, txt):
    genoma.count(txt)
    inverso = ''
    for letra in range(len(genoma)-1, -1, -1):
        inverso = inverso + genoma[letra]

    print(inverso.count(txt)+genoma.count(txt))


def mostrar(genoma):
    print(genoma)


def transpor_e_reverter(genoma, i, j, k):
    resultado_transpor = transpor(genoma, i, j, k)
    resultadotranspor_e_reverter = reverter(resultado_transpor, i, k)
    return resultadotranspor_e_reverter


def main():
    genoma = input()
    while True:
        procedimento = input().split()

        if procedimento[0] == 'mostrar':
            mostrar(genoma)

        elif procedimento[0] == 'reverter':
            procedimento[1] = int(procedimento[1])
            procedimento[2] = int(procedimento[2])
            genoma = reverter(genoma, procedimento[1], procedimento[2])

        elif procedimento[0] == 'transpor':
            procedimento[1] = int(procedimento[1])
            procedimento[2] = int(procedimento[2])
            procedimento[3] = int(procedimento[3])
            genoma = transpor(
                genoma, procedimento[1], procedimento[2], procedimento[3])

        elif procedimento[0] == 'combinar':
            procedimento[2] = int(procedimento[2])
            genoma = combinar(genoma, procedimento[1], procedimento[2])

        elif procedimento[0] == 'concatenar':
            genoma = concatenar(genoma, procedimento[1])

        elif procedimento[0] == 'remover':
            procedimento[1] = int(procedimento[1])
            procedimento[2] = int(procedimento[2])
            genoma = remover(genoma, procedimento[1], procedimento[2])

        elif procedimento[0] == 'buscar':
            buscar(genoma, procedimento[1])

        elif procedimento[0] == 'buscar_bidirecional':
            buscar_bidirecional(genoma, procedimento[1])

        elif procedimento[0] == 'transpor_e_reverter':
            procedimento[1] = int(procedimento[1])
            procedimento[2] = int(procedimento[2])
            procedimento[3] = int(procedimento[3])
            genoma = transpor_e_reverter(
                genoma, procedimento[1], procedimento[2], procedimento[3])

        elif procedimento[0] == 'sair':
            break


main()
