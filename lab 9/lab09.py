#Robô que limpa um cômodo.

def imprime_matriz(mat: list[list[str]]) -> None:
    '''Função que que recebe como parâmetro uma lista de listas e imprime a matriz'''
    for linha in mat:
        for caractere in range(len(linha)):
            if caractere == len(linha)-1:
                print(linha[caractere], end='')

            else:
                print(linha[caractere], end=' ')

        print()


def retornar(
        mat: list[list[str]],
        pos_retorno: tuple[int, int],
        pos_atual: tuple[int, int]
) -> None:
    '''Função que recebe uma matriz e a posição inicial do robo como parâmetros e faz o robo retornar da onde ele veio'''

    x, y = pos_retorno
    a, b = pos_atual

    while x != a or y != b:
        if y > b:
            mat[a][b] = '.'
            mat[a][b+1] = 'r'
            imprime_matriz(mat)
            print()

            a, b = limpar(mat, (a, b + 1))

        elif y < b:
            mat[a][b] = '.'
            mat[a][b-1] = 'r'
            imprime_matriz(mat)
            print()

            a, b = limpar(mat, (a, b-1))

        elif a > x:
            mat[a][b] = '.'
            mat[a-1][b] = 'r'
            imprime_matriz(mat)
            print()

            a, b = limpar(mat, (a-1, b))

        elif a < x:
            mat[a][y] = '.'
            mat[a+1][y] = 'r'
            imprime_matriz(mat)
            print()

            a, b = limpar(mat, (a+1, y))


def limpar(mat: list[list[str]], pos_atual: tuple[int, int]) -> tuple[int, int]:
    '''Função que recebe uma matriz e uma coordenada como parâmetro, enquanto houver sujeira nas adjacências do robô, ele vai limpando'''
    (a, b) = pos_atual

    if mat[a][max(b-1, 0)] == 'o':
        mat[a][b] = '.'
        mat[a][b-1] = 'r'
        imprime_matriz(mat)
        print()

        return limpar(mat, (a, b-1))

    elif mat[max(a-1, 0)][b] == 'o':
        mat[a][b] = '.'
        mat[a-1][b] = 'r'
        imprime_matriz(mat)
        print()

        return limpar(mat, (a-1, b))

    elif mat[a][min(b+1, len(mat[0])-1)] == 'o':
        mat[a][b] = '.'
        mat[a][b+1] = 'r'
        imprime_matriz(mat)
        print()

        return limpar(mat, (a, b+1))

    elif mat[min(a+1, len(mat)-1)][b] == 'o':
        mat[a][b] = '.'
        mat[a+1][b] = 'r'
        imprime_matriz(mat)
        print()

        return limpar(mat, (a+1, b))

    return (a, b)


def escanear(mat: list[list[str]]) -> None:
    '''Função que recebe uma matriz como parâmetro e verifica se há sujeira nas adjacências , se houver, a função limpar é chamada'''

    for i in range(len(mat)):
        if i % 2 == 0:
            for j in range(len(mat[0])):
                if j+1 < len(mat[0]) and mat[i][j+1] == 'o':
                    mat[i][j+1] = 'r'
                    mat[i][j] = '.'
                    imprime_matriz(mat)
                    print()
                elif j == len(mat[0])-1 and i+1 < len(mat) and mat[i+1][j] == 'o':
                    mat[i][j] = '.'
                    mat[i+1][j] = 'r'
                    imprime_matriz(mat)
                    print()

                else:
                    pos_retorno = (i, j)
                    pos_atual = limpar(mat, (i, j))
                    retornar(mat, pos_retorno, pos_atual)
                    if j + 1 < len(mat[0]):
                        mat[i][j] = '.'
                        mat[i][j+1] = 'r'
                        imprime_matriz(mat)
                        print()

                    elif i + 1 < len(mat):
                        mat[i][j] = '.'
                        mat[i+1][j] = 'r'
                        imprime_matriz(mat)
                        print()

        else:
            for j in range(len(mat[0]) - 1, -1, -1):
                if j-1 >= 0 and mat[i][j-1] == 'o':
                    mat[i][j-1] = 'r'
                    mat[i][j] = '.'
                    imprime_matriz(mat)
                    print()

                elif j == 0 and i+1 < len(mat) and mat[i+1][j] == 'o':
                    mat[i][j] = '.'
                    mat[i+1][j] = 'r'
                    imprime_matriz(mat)
                    print()

                else:
                    pos_retorno = (i, j)
                    pos_atual = limpar(mat, (i, j))
                    retornar(mat, pos_retorno, pos_atual)
                    if j - 1 >= 0:
                        mat[i][j] = '.'
                        mat[i][j-1] = 'r'
                        imprime_matriz(mat)
                        print()

                    elif i + 1 < len(mat):
                        mat[i][j] = '.'
                        mat[i+1][j] = 'r'
                        imprime_matriz(mat)
                        print()


def ir_para_o_final(mat):
    if (mat[-1][0] == 'r'):
        # Esse laço serve para fazer o robô ir para a posição final.
        for i in range(len(mat[0])-1):
            mat[-1][i] = '.'
            mat[-1][i+1] = 'r'
            imprime_matriz(mat)
            print()
        return


def main():

    n = int(input())

    mat = []
    for i in range(n):
        mat.append([])
        linha = input().split()
        mat[i] = linha

    imprime_matriz(mat)
    print()
    if len(mat) % 2 == 0:
        escanear(mat)
        ir_para_o_final(mat)

    else:
        escanear(mat)


if __name__ == "__main__":
    main()
