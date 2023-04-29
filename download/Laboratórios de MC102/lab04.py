# Organizção do Pet Shop.

dia_analisado = int(input())
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
brigas = 0

# Loop que cria uma lista de listas do animal e seu procedimento desejado.
for i in range(0, animais_presentes):
    animal_procedimento.append(str(input()).split())


# Loop que cria uma lista só dos animais que estavam presentes no dia.
for i in range(0, len(animal_procedimento),):
    lista_animais.append(animal_procedimento[i][0])

#Loop que vê quantas brigas teve no dia.
for i in range(0, len(pares_brigam)):
    if pares_brigam[i][0] and pares_brigam[i][1] in lista_animais:
        brigas +=1

print(brigas/2)

