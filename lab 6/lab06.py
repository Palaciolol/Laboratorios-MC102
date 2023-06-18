#Operações com vetores.

def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Dadas duas listas de inteiros, soma elemento a elemento das listas

    Parametros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''
    soma_zip = zip(vetor1, vetor2)
    soma = []
    if len(vetor1) == len(vetor2):
        for x, y in soma_zip:
            soma.append(x+y)

    elif len(vetor1) > len(vetor2):
        for i in range(0, len(vetor1) - len(vetor2)):
            vetor2.append(0)

        for x, y in soma_zip:
            soma.append(x+y)

    elif len(vetor2) > len(vetor1):
        for i in range(0, len(vetor2) - len(vetor1)):
            vetor1.append(0)

        for x, y in soma_zip:
            soma.append(x+y)

    return soma


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Dadas duas listas de inteiros,subtrai elemento a elemento das listas

    Parametros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''
    subtrai_zip = zip(vetor1, vetor2)
    subtracao = []

    if len(vetor1) == len(vetor2):
        for x, y in subtrai_zip:
            subtracao.append(x-y)

    elif len(vetor1) > len(vetor2):
        for i in range(0, len(vetor1) - len(vetor2)):
            vetor2.append(0)

        for x, y in subtrai_zip:
            subtracao.append(x-y)

    elif len(vetor2) > len(vetor1):
        for i in range(0, len(vetor2) - len(vetor1)):
            vetor1.append(0)

        for x, y in subtrai_zip:
            subtracao.append(x-y)

    return subtracao


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Dadas duas listas de inteiros, multiplica elemento a elemento das listas

    Parâmetros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''

    multiplica_zip = zip(vetor1, vetor2)
    multiplicacao = []

    if len(vetor1) == len(vetor2):
        for x, y in multiplica_zip:
            multiplicacao.append(x*y)

    elif len(vetor1) > len(vetor2):
        for i in range(0, len(vetor1) - len(vetor2)):
            vetor2.append(1)

        for x, y in multiplica_zip:
            multiplicacao.append(x*y)

    elif len(vetor2) > len(vetor1):
        for i in range(0, len(vetor2) - len(vetor1)):
            vetor1.append(1)

        for x, y in multiplica_zip:
            multiplicacao.append(x*y)

    return multiplicacao


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Dadas duas listas de inteiros faz a divisão inteira elemento a elemen-
    to das listas
    Parâmetros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''

    divide_zip = zip(vetor1, vetor2)
    divisao = []

    if len(vetor1) == len(vetor2):
        for x, y in divide_zip:
            divisao.append(x//y)

    elif len(vetor1) > len(vetor2):
        for i in range(0, len(vetor1) - len(vetor2)):
            vetor2.append(1)

        for x, y in divide_zip:
            divisao.append(x//y)

    elif len(vetor2) > len(vetor1):
        for i in range(0, len(vetor2) - len(vetor1)):
            vetor1.append(0)

        for x, y in divide_zip:
            divisao.append(x//y)

    return divisao


def multiplicacao_escalar(vetor: list[int],
                          escalar: int) -> list[int]:
    '''Dada uma lista e um número inteiro, multiplica todos os elementos da lis
    ta pelo números inteiro

    Parâmetros:
    vetor--lista de inteiros
    escalar--número inteiro
    '''
    multiplica_escalar = []

    for x in range(0, len(vetor)):
        multiplica_escalar.append(escalar*vetor[x])

    return multiplica_escalar


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    '''Dada uma lista e um número inteiro n, replica a lista n vezes

    Parâtros:
    vetor--lista de inteiros
    n--número inteiro maior ou igual a zero
    '''
    if n > 0:
        return (vetor*n)

    else:
        return []


def soma_elementos(vetor: list[int]) -> int:
    '''Dada uma lista de inteiros, soma todos os elementos da lista

    Parâmetros :
    vetor--lista de inteiros
    '''

    soma_tudo = 0
    for x in range(0, len(vetor)):
        soma_tudo += vetor[x]

    return soma_tudo


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    '''Dadas duas listas de inteiros, soma a multiplicacão elemento a elemento
    das listas
    Parâmetros :
    vetor1--listta de inteiros
    vetor2--lista de inteiros
    '''

    if len(vetor1) > len(vetor2):
        for i in range(0, len(vetor1) - len(vetor2)):
            vetor2.append(1)

        r1 = soma_elementos(multiplica_vetores(vetor1, vetor2))

    elif len(vetor2) > len(vetor1):
        for i in range(0, len(vetor2) - len(vetor1)):
            vetor1.append(1)

        r1 = soma_elementos(multiplica_vetores(vetor1, vetor2))

    elif len(vetor1) == len(vetor2):
        r1 = soma_elementos(multiplica_vetores(vetor1, vetor2))

    return r1


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Dadas duas listas de inteiros, devolve uma lista na qual os elementos
    são a soma da multiplicação do primeiro elemento da primeira lista por
    todos os elementos da segunda lista
    Parâmetros :
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''

    multi_todos = []

    for x in range(0, len(vetor1)):
        multiplicacao_escalar(vetor2, vetor1[x])
        multi_todos.append(soma_elementos(
            multiplicacao_escalar(vetor2, vetor1[x])))

    return multi_todos


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    '''Dadas duas listas, uma maior e outra menor, devolve uma
    lista na qual os elementos são a soma,até o
    último elemento da lista menor, da
    multiplicação elemento a elemento das listas
    Parâmetros:
    vetor--lista de inteiros
    mascara--lista de inteiros menor
    '''

    correlacao = []

    for x in range(0, len(vetor) - len(mascara) + 1):
        correlacao.append(produto_interno(vetor[x: len(mascara)+x], mascara))

    return correlacao


def transforma_int(vetor_t: list[str]) -> list[int]:
    vetor_aleatorio = []
    for i in range(0, len(vetor_t)):
        vetor_aleatorio.append(int(vetor_t[i]))

    return vetor_aleatorio


def main() -> None:
    vetores = input().split(',')
    vetores = transforma_int(vetores)

    while True:
        procedimento = input()

        if procedimento == 'fim':
            break

        elif procedimento == 'soma_vetores':
            vetores_soma = input().split(',')
            vetores_soma = transforma_int(vetores_soma)
            vetores = soma_vetores(vetores, vetores_soma)
            print(vetores)

        elif procedimento == 'subtrai_vetores':
            vetores_subtracao = input().split(',')
            vetores_subtracao = transforma_int(vetores_subtracao)
            vetores = subtrai_vetores(vetores, vetores_subtracao)
            print(vetores)

        elif procedimento == 'multiplica_vetores':
            vetores_multiplica = input().split(',')
            vetores_multiplica = transforma_int(vetores_multiplica)
            vetores = multiplica_vetores(vetores, vetores_multiplica)
            print(vetores)

        elif procedimento == 'divide_vetores':
            vetores_divide = input().split(',')
            vetores_divide = transforma_int(vetores_divide)
            vetores = divide_vetores(vetores, vetores_divide)
            print(vetores)

        elif procedimento == 'multiplicacao_escalar':
            multiplica_escalar = int(input())
            vetores = multiplicacao_escalar(vetores, multiplica_escalar)
            print(vetores)

        elif procedimento == 'n_duplicacao':
            duplicacao = int(input())
            vetores = n_duplicacao(vetores, duplicacao)
            print(vetores)

        elif procedimento == 'soma_elementos':
            vetores = [soma_elementos(vetores)]
            print(vetores)

        elif procedimento == 'produto_interno':
            vetores_produto_interno = input().split(',')
            vetores_produto_interno = transforma_int(vetores_produto_interno)
            vetores = [produto_interno(vetores, vetores_produto_interno)]
            print(vetores)

        elif procedimento == 'multiplica_todos':
            vetores_mtodos = input().split(',')
            vetores_mtodos = transforma_int(vetores_mtodos)
            vetores = multiplica_todos(vetores, vetores_mtodos)
            print(vetores)

        elif procedimento == 'correlacao_cruzada':
            vetores_correlacao_cruzada = input().split(',')
            vetores_correlacao_cruzada = transforma_int(
                vetores_correlacao_cruzada)
            vetores = correlacao_cruzada(vetores, vetores_correlacao_cruzada)
            print(vetores)


if __name__ == "__main__":
    main()
