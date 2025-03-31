#Competição para pior filme do ano.

tot_fil = int(input())
filmes = []
for _ in range(tot_fil):
    filmes.append(input())

tot_aval = int(input())
lista_mais_bocejos = []
lista_mais_pausado = []
lista_revira_olhos = []
lista_sem_discussao = []
lista_sem_nocao = []

for _ in range(tot_aval):
    avaliacoes = {}
    aval_temp = input()

    if 'filme que causou mais bocejos' in aval_temp:
        avaliacoes['categoria'] = 'filme que causou mais bocejos'
        avaliacoes['filme'], avaliacoes['nota'] = aval_temp.split(', ')[-2:]

        lista_mais_bocejos.append(avaliacoes)

    elif 'filme que foi mais pausado' in aval_temp:
        avaliacoes['categoria'] = 'filme que foi mais pausado'
        avaliacoes['filme'], avaliacoes['nota'] = aval_temp.split(', ')[-2:]

        lista_mais_pausado.append(avaliacoes)

    elif 'filme que mais revirou olhos' in aval_temp:
        avaliacoes['categoria'] = 'filme que mais revirou olhos'
        avaliacoes['filme'], avaliacoes['nota'] = aval_temp.split(', ')[-2:]

        lista_revira_olhos.append(avaliacoes)

    elif 'filme que não gerou discussão nas redes sociais' in aval_temp:
        avaliacoes['categoria'] = 'filme que não gerou discussão nas redes sociais'
        avaliacoes['filme'], avaliacoes['nota'] = aval_temp.split(', ')[-2:]

        lista_sem_discussao.append(avaliacoes)

    elif 'enredo mais sem noção' in aval_temp:
        avaliacoes['categoria'] = 'enredo mais sem noção'
        avaliacoes['filme'], avaliacoes['nota'] = aval_temp.split(', ')[-2:]

        lista_sem_nocao.append(avaliacoes)


def lelista(lista: list) -> dict:
    '''Le uma lista que tem as categorias de interesse e retorna um dicionário com a chave sendo o nome do filme e o valor sendo a média dele e a quantidade de avaliadores que ele foi avaliado'''
    pontuacoes = {}

    for avaliacao in lista:
        filme = avaliacao['filme']
        nota = int(avaliacao['nota'])

        if filme in pontuacoes:
            pontuacoes[filme].append(nota)

        else:
            pontuacoes[filme] = [nota]

    # adicionando a info de num de avaliadores
    for filme, notas in pontuacoes.items():
        pontuacoes[filme] = [sum(notas) / len(notas), len(notas)]

    return pontuacoes


pontuacoes_pausado = lelista(lista_mais_pausado)
pontuacoes_bocejo = lelista(lista_mais_bocejos)
pontuacoes_revira_olhos = lelista(lista_revira_olhos)
pontuacoes_sem_discussao = lelista(lista_sem_discussao)
pontuacoes_sem_nocao = lelista(lista_sem_nocao)


def encontrar_vencedor_categoria(pontuacoes: dict) -> str:
    ''' Encontra o vencedor de acordo com as pontuações passadas'''
    vencedor = max(pontuacoes.keys(), key=lambda x: pontuacoes[x])
    return vencedor


vencedor_bocejos = encontrar_vencedor_categoria(pontuacoes_bocejo)
vencedor_pausado = encontrar_vencedor_categoria(pontuacoes_pausado)
vencedor_revira_olhos = encontrar_vencedor_categoria(pontuacoes_revira_olhos)
vencedor_sem_discussao = encontrar_vencedor_categoria(pontuacoes_sem_discussao)
vencedor_sem_nocao = encontrar_vencedor_categoria(pontuacoes_sem_nocao)

lista_vencedores = [
    vencedor_bocejos,
    vencedor_pausado,
    vencedor_revira_olhos,
    vencedor_sem_discussao,
    vencedor_sem_nocao
]

vencedores = {}
for filme in lista_vencedores:
    vencedores[filme] = [0]

for filme in lista_vencedores:
    vencedores[filme][0] += 1

for filme, x in vencedores.items():
    x.append(0)
    if filme in pontuacoes_pausado:
        x[1] += pontuacoes_pausado[filme][0]

    if filme in pontuacoes_bocejo:
        x[1] += pontuacoes_bocejo[filme][0]

    if filme in pontuacoes_revira_olhos:
        x[1] += pontuacoes_revira_olhos[filme][0]

    if filme in pontuacoes_sem_discussao:
        x[1] += pontuacoes_sem_discussao[filme][0]

    if filme in pontuacoes_sem_nocao:
        x[1] += pontuacoes_sem_nocao[filme][0]

premio_pior_filme = max(vencedores.keys(), key=lambda filme: vencedores[filme])


def encontrar_nao_merecia(dict1: dict, dict2: dict, dict3: dict, dict4: dict, dict5: dict) -> str:
    '''recebe como parâmetro cinco dicionários e a função procura neles os filmes da lista de filmes dada inicialmente'''
    i = 0
    filmes_nao_mereciam = []
    while i < len(filmes):
        if (filmes[i] not in dict1) and (filmes[i] not in dict2) and (filmes[i] not in dict3) and (filmes[i] not in dict4) and (filmes[i] not in dict5):
            filmes_nao_mereciam.append(filmes[i])

        i += 1
    return filmes_nao_mereciam


nao_merecia = encontrar_nao_merecia(pontuacoes_bocejo, pontuacoes_sem_discussao,
                                    pontuacoes_pausado, pontuacoes_revira_olhos, pontuacoes_sem_nocao)

print('#### abacaxi de ouro ####')
print()
print('categorias simples')
print('categoria: filme que causou mais bocejos')
print(f'- {vencedor_bocejos}')
print('categoria: filme que foi mais pausado')
print(f'- {vencedor_pausado}')
print('categoria: filme que mais revirou olhos')
print(f'- {vencedor_revira_olhos}')
print('categoria: filme que não gerou discussão nas redes sociais')
print(f'- {vencedor_sem_discussao}')
print('categoria: enredo mais sem noção')
print(f'- {vencedor_sem_nocao}')
print()
print('categorias especiais')
print('prêmio pior filme do ano')
print(f'- {premio_pior_filme}')
print('prêmio não merecia estar aqui')

if len(nao_merecia) == 0:
    print(f'- sem ganhadores')

else:
    print(f'- {", ".join(nao_merecia)}')
