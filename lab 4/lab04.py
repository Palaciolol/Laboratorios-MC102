# Organizção do Pet Shop.
def lab4():
    quantos_pares_brigam = int(input())

    pares_brigam = []

    for i in range(0, quantos_pares_brigam):
        # Lista dos pares de animais que brigam.
        pares_brigam.append(str(input()).split())

    # Procedimentos e suas dispinibilidades.
    servicos_disponiveis = str(input()).split()
    i = 1
    # Esse loop serve pra transformar a quantidade de procidimento disponível em interiro.
    while i in range(0, len(servicos_disponiveis)):
        servicos_disponiveis[i] = int(servicos_disponiveis[i])
        i += 2

    animais_presentes = int(input())
    animal_procedimento = []
    lista_animais = []

    # Loop que cria uma lista de listas do animal e seu procedimento desejado.
    for i in range(0, animais_presentes):
        animal_procedimento.append(str(input()).split())

    # Loop que cria uma lista só dos animais que estavam presentes no dia.
    for i in range(0, len(animal_procedimento)):
        lista_animais.append(animal_procedimento[i][0])

    brigas = 0
    # Loop que vê quantas brigas teve no dia.
    for i in range(0, len(pares_brigam)):
        if pares_brigam[i][0] in lista_animais and pares_brigam[i][1] in lista_animais:
            brigas += 1
    print('Brigas: {}'.format(brigas))

    nao_atendidos = []
    nao_disponivel = []
    atendidos = []
    for i in range(0, len(animal_procedimento)):
        if animal_procedimento[i][1] in servicos_disponiveis:
            for l in range(0, len(servicos_disponiveis)):
                if animal_procedimento[i][1] == servicos_disponiveis[l]:
                    if servicos_disponiveis[l+1] > 0:
                        servicos_disponiveis[l+1] -= 1
                        atendidos.append(animal_procedimento[i][0])

                    else:
                        nao_atendidos.append(animal_procedimento[i][0])
                    break

        else:
            nao_disponivel.append(animal_procedimento[i][0])
    if atendidos != []:
        print('Animais atendidos: ', end='')
        for i in range(0, len(atendidos)-1):
            print('{}, '.format(atendidos[i]), end='')
        print('{}'.format(atendidos[-1]))
    if nao_atendidos != []:
        print('Animais não atendidos: ', end='')
        for i in range(0, len(nao_atendidos)-1):
            print('{}, '.format(nao_atendidos[i]), end='')
        print('{}'.format(nao_atendidos[-1]))

    for i in range(0, len(nao_disponivel)):
        print('Animal {} solicitou procedimento não disponível.'.format(
            nao_disponivel[i]))


dia_analisado = int(input())
for i in range(1, dia_analisado+1):
    print('Dia: {}'.format(i))
    lab4()
    print()



