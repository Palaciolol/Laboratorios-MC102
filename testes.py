def multiplicacao_escalar(vetor:list[int],escalar:int):
    '''Dada uma lista e um número inteiro, multiplica todos os elementos da lista pelo números inteiro
    
    Parâmetros:
    vetor--lista de inteiros
    escalar--número inteiro
    '''
    multiplica_escalar = []

    for x in range(0,len(vetor)):
         multiplica_escalar.append(escalar*vetor[x])

    return multiplica_escalar

def soma_elementos(vetor:list[int]):
    '''Dada uma lista de inteiros, soma todos os elementos da lista
    
    Parâmetros:
    vetor--lista de inteiros
    '''

    soma_tudo = 0
    
    for x in range(0,len(vetor)):
         soma_tudo += vetor[x]

    return soma_tudo






def multiplica_todos(vetor1:list[int],vetor2:list[int]):
    '''Dadas duas listas de inteiros, devolve uma lista na qual os elementos são a soma da multiplicação do primeiro elemento da primeira lista por todos os elementos da segunda lista
    
    Parâmetros:
    vetor1--lista de inteiros
    vetor2--lista de inteiros
    '''
   
    multi_todos = []
    for x in range(0,len(vetor1)):
        multiplicacao_escalar(vetor2,vetor1[x])
        multi_todos.append(soma_elementos(multiplicacao_escalar(vetor2,vetor1[x])))
        

            
            
    print(multi_todos)



def correlacao_cruzada(vetor: list[int], mascara: list[int]):
    '''Dadas duas listas, uma maior e outra menor, devolve uma lista na qual os elementos são a soma,até o último elemento da lista menor, da multiplicação elemento a elemento das listas

    Parâmetros:
    vetor--lista de inteiros
    mascara--lista de inteiros menor
    '''

    correlacao = []
    for x in range(0,len(mascara)):
        correlacao.append((vetor,mascara[x]))



        

        










    

