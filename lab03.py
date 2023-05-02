# Jogo no qual o vencedor é aquele que obtem a maior pontuação.

n_jogadores = int(input())

n_caixa = (input().split())

intervalos_input = (input().split())
diferenca_intervalos = []
pontuacoes = []

i = 0
while i < len(intervalos_input):
    diferenca_intervalos.append( int(intervalos_input[i + 1]) - int(intervalos_input[i]))

    i += 2


# Como o númuro máximo de jogadores é 20, entao:

i = 0
while i < (n_jogadores//2 + n_jogadores % 2):
    pontuacoes.append(int(n_caixa[i]) * diferenca_intervalos[i])
    i += 1


while i < n_jogadores:
    pontuacoes.append(int(n_caixa[i]) + diferenca_intervalos[i])
    i += 1

# Achando o maior valor da lista

i = 0
maior_valor = 0
vencedor = 0
n_vencedores = 0

while i < len(pontuacoes):
    if (pontuacoes[i] > maior_valor):
        vencedor = i
        maior_valor = pontuacoes[i]
        n_vencedores = 1
    elif (pontuacoes[i] == maior_valor):
        n_vencedores = n_vencedores + 1

    i += 1


if n_vencedores == 1:
    print('O jogador número', vencedor+1,
          'vai receber o melhor bolo da cidade pois venceu com', maior_valor, 'ponto(s)!')

else:
    print('Rodada de cerveja para todos os jogadores!')
