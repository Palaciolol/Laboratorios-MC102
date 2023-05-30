def calcular_media_notas(lista_avaliacoes):
    filmes_notas = {}
    for avaliacao in lista_avaliacoes:
        filme = avaliacao['filme']
        nota = int(avaliacao['nota'])

        if filme not in filmes_notas:
            filmes_notas[filme] = {'total': 0, 'count': 0}

        filmes_notas[filme]['total'] += nota
        filmes_notas[filme]['count'] += 1

    medias = {}
    for filme, info in filmes_notas.items():
        media = info['total'] / info['count']
        medias[filme] = media

    return medias


def encontrar_vencedor_categoria(medias):
    vencedor = max(medias, key=medias.get)
    return vencedor


def encontrar_vencedor_pior_filme(medias_categorias):
    vencedor = max(medias_categorias, key=medias_categorias.get)
    return vencedor


def encontrar_vencedor_nao_merecia(medias_categorias, filmes_avaliados):
    filmes_nao_avaliados = list(set(filmes) - set(filmes_avaliados))
    if filmes_nao_avaliados:
        return filmes_nao_avaliados
    else:
        return "sem ganhadores"


# Leitura dos dados
tot_fil = int(input())
filmes = []
for _ in range(tot_fil):
    filmes.append(input())

tot_aval = int(input())
avaliacoes = []
filmes_avaliados = []
for _ in range(tot_aval):
    aval_temp = input().split(', ')
    avaliador = aval_temp[0]
    categoria = aval_temp[1]
    filme = aval_temp[2]
    nota = int(aval_temp[3])

    avaliacao = {'avaliador': avaliador, 'categoria': categoria, 'filme': filme, 'nota': nota}
    avaliacoes.append(avaliacao)
    filmes_avaliados.append(filme)

# Cálculo das médias das notas por filme
medias_filmes = calcular_media_notas(avaliacoes)

# Determinação dos vencedores de cada categoria
vencedores_categorias = {}
categorias_simples = ['filme que causou mais bocejos', 'filme que foi mais pausado', 'filme que mais revirou olhos',
                      'filme que não gerou discussão nas redes sociais', 'enredo mais sem noção']
for categoria in categorias_simples:
    filmes_categoria = [avaliacao['filme'] for avaliacao in avaliacoes if avaliacao['categoria'] == categoria]
    medias_categoria = {filme: medias_filmes[filme] for filme in filmes_categoria}
    vencedor_categoria = encontrar_vencedor_categoria(medias_categoria)
    vencedores_categorias[categoria] = vencedor_categoria

# Determinação do vencedor do Prêmio Pior Filme do Ano
medias_categorias = {categoria: medias_filmes[vencedor] for categoria, vencedor in vencedores_categorias.items()}
vencedor_pior_filme = encontrar_vencedor_pior_filme(medias_categorias)
vencedores_categorias['prêmio pior filme do ano'] = vencedor_pior_filme

# Determinação do vencedor do Prêmio "Não Merecia Estar Aqui"
vencedor_nao_merecia = encontrar_vencedor_nao_merecia(medias_categorias, filmes_avaliados)
vencedores_categorias['prêmio não merecia estar aqui'] = vencedor_nao_merecia

# Impressão dos resultados
print("#### abacaxi de ouro ####")
print("categorias simples")
for categoria, vencedor in vencedores_categorias.items():
    if categoria in categorias_simples:
        print(f"categoria: {categoria}")
        print(f"- {vencedor}")

print("categorias especiais")
print("prêmio pior filme do ano")
print("- " + vencedores_categorias['prêmio pior filme do ano'])
print("prêmio não merecia estar aqui")
if vencedores_categorias['prêmio não merecia estar aqui'] == "sem ganhadores":
    print("- sem ganhadores")
else:
    for vencedor in vencedores_categorias['prêmio não merecia estar aqui']:
        print(f"- {vencedor}")

