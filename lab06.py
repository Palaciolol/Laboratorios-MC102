def soma_vetores(vetor1:list[int], vetor2 : list[int]):
    '''Dadas duas listas de inteiros, soma elemento a elemento das listas

    Parametros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    ''' 

def subtrai_vetores(vetor1:list[int],vetor2:list[int]):
    '''Dadas duas listas de inteiros,subtrai elemento a elemento das listas

    Parametros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''
def multiplica_vetores(vetor1:list[int],vetor2:list[int]):
    '''Dadas duas listas de inteiros, multiplica elemento a elemento das listas
    
    Parâmetros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''

def divide_vetores(vetor1:list[int],vetor2:list[int]):
    ''''Dadas duas listas de inteiros, faz a divisão inteira elemento a elemento das listas
    
    Parâmetros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''

def multiplicacao_escalar(vetor:list[int],escalar:int):
    '''Dada uma lista e um número inteiro, multiplica todos os elementos da lista pelo números inteiro
    
    Parâmetros:
    vetor--lista de inteiros
    escalar--número inteiro
    '''

def n_duplicacao(vetor:list[int],n:int):
    '''Dada uma lista e um número inteiro n, replica a lista n vezes
    
    Parâtros:
    vetor--lista de inteiros
    n--número inteiro maior ou igual a zero
    '''    

def soma_elementos(vetor:list[int]):
    '''Dada uma lista de inteiros, soma todos os elementos da lista
    
    Parâmetros:
    vetor--lista de inteiros
    '''

def produto_interno(vetor1:list[int],vetor2:list[int]):
    '''Dadas duas listas de inteiros, soma a multiplicacão elemento a elemento das listas
    
    Parâmetros:
    vetor1--listta de inteiros
    vetor2--lista de inteiros
    '''

def multiplica_todos(vetor1:list[int],vetor2:list[int]):
    '''Dadas duas listas de inteiros, devolve uma lista na qual os elementos são a soma da multiplicação do primeiro elemento da primeira lista por todos os elementos da segunda lista
    
    Parâmetros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''

def correlacao_cruzada(vetor:list[int],mascara:list[int]):
    '''Dadas duas listas, uma maior e outra menor, devolve uma lista na qual os elementos são a soma,até o último elemento da lista menor, da multiplicação elemento a elemento das listas
    
    Parâmetros:
    vetor--lista de inteiros
    mascara--lista de inteiros menor
    '''
    
def transforma_int(list):
    for i in list:
        list[i] = int(list[i])

    return list
      







def main():
    vetores = input().split(',')
    transforma_int(vetores)

    while True:
        procedimento = input()

        if procedimento == 'fim':
            break

        elif procedimento == 'soma_vetores':
            vetores_soma = input().split(',')
            transforma_int(vetores_soma)
            soma_vetores(list[int],vetores_soma)


        elif procedimento == 'subtrai_vetores':
            vetores_subtracao = input().split(',')
            transforma_int(vetores_subtracao)
            subtrai_vetores(list[int],vetores_subtracao)

        elif procedimento == 'multiplica_vetores':
            vetores_multiplica = input().split(',')
            transforma_int(multiplica_vetores)
            multiplica_vetores(list[int],vetores_multiplica)

        elif procedimento == 'divide_vetores':
            vetores_divide = input().split(',')
            transforma_int(divide_vetores)
            divide_vetores(list[int],vetores_divide)

        elif procedimento == 'multiplicacao_escalar':
            multiplica_escalar = int(input())
            multiplicacao_escalar(list[int],multiplica_escalar)

        elif procedimento == 'n_duplicacao':
            duplicacao = int(input())
            n_duplicacao(list[int],duplicacao)
        
        elif procedimento == 'soma_elementos':
            soma_elementos(list[int])

        elif procedimento == 'produto_interno':
            vetores_produto_interno = input().split(',')
            transforma_int(vetores_produto_interno)
            produto_interno(list[int],vetores_produto_interno)

        elif procedimento == 'multiplica_todos':
            vetores_mtodos = input().split(',')
            transforma_int(vetores_mtodos)
            multiplica_todos(list[int],vetores_mtodos)

        elif procedimento == 'correlacao_cruzada':
            vetores_correlacao_cruzada = input().split(',')
            transforma_int(vetores_correlacao_cruzada)
            correlacao_cruzada(list[int],vetores_correlacao_cruzada)

if __name__ == "__main__":
    main()


        


    
        