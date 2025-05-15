#Jogo da Aloy.

class Player:

    def __init__(self, vida, flechas):
        self.vida_inicial = vida
        self.vida = vida
        self.flechas = flechas

    def tomar_dano(self, dano: int):
        '''
        Recebe o dano que a aloy vai receber e o aplica
        
        Parâmentro: 
        - dano: dano recebido

        Retorno: 
        - nova vida da Aloy após tomar o dano
        '''
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
        
        return self.vida

    def recuperar_vida(self):
        '''
        Recupera a vida da aloy a partir da vida atual dela
        
        
        '''
        if self.vida + self.vida_inicial // 2 <= self.vida_inicial:
            self.vida += self.vida_inicial // 2

        else:
            self.vida = self.vida_inicial

    def recuperar_flechas(self, flechas_usadas: dict):
        '''
        Recebe as flechas que a aloy usou e as recupera

        Parâmetro: 
        -flechas_usadas: flechas que ela usou e deve recuperar após o combate
        
        '''
        for flecha in flechas_usadas:
            self.flechas[flecha] += flechas_usadas[flecha]
    
    def flechas_restantes(self):
        '''
        Retorno:
        - Soma de todas as flechas disponíveis da aloy
        '''
        return sum(self.flechas.values())
    
    def usar_flechas(self, flecha):
        '''
        Recebe a flecha que a aloy usou no seu ataque e a usa

        Parâmetros:
        -flecha: flecha que a aloy usou
        
        '''
        if self.flechas[flecha] > 0:
            self.flechas[flecha] -= 1
        



class Monster:

    def __init__(self, vida_monstro, ataque, num_partes, partes):
        self.vida_monstro = vida_monstro
        self.ataque = ataque
        self.num_partes = num_partes
        self.partes = partes

    def tomar_dano(self,  dano: int) -> None:
        '''
        Recebe o dano que o monstro vai receber e o aplica
        
        Parâmetros:
        -dano: dano que o monstro vai receber

        Retorno:
        - vida do monstro depois de receber dano
        '''
        self.vida_monstro -= dano
        return self.vida_monstro

  


def ler_aloy():
    '''Função que lê a vida da aloy e suas flechas'''
    vida_aloy = int(input()) #Recebe a vida da aloy como inteiro
    # Recebe a entrada dos tipos de flecha e suas quantidades e guarda em uma lista
    flechas_temp = input().split()
    flechas = {}

    # Esse loop serve pra transformar os dados da lista em um dicionário onde os tipos de flecha são a chave e sua quantidade são os valores.
    for i in range(0, len(flechas_temp), 2):
        flechas[flechas_temp[i]] = int(flechas_temp[i+1])
        

    return Player(vida_aloy, flechas)


def le_monstros_rodada() -> list[Monster]:
    '''
    
    Função que lê os monstros por rodada e adiciona eles em uma lista
    
    Retorno:
    - lista dos monstros da rodada
    '''

    lista_monstros = []
    monstros_por_rodada = int(input())  #Recebe a quantidade de monstros que a aloy vai batalhar na rodada.

    for _ in range(monstros_por_rodada):
        # Recebe a vida, o dano e a quantidade de partes do monstro.
        entrada_atributos = input()
        # Transforma os atributos em int
        vida, ataque, num_partes = map(int, entrada_atributos.split())
        partes = ler_partes_monstro(num_partes)
        monstro = Monster(vida, ataque, num_partes, partes)

        lista_monstros.append(monstro)

    return lista_monstros


def ler_partes_monstro(num_partes: int) -> dict[str, tuple[str, int, tuple[int ,int]]]:
    '''Função que lê as partes dos monstros e adiciona em um dicionário'''

    dict_partes = {}
    for _ in range(num_partes):

        entrada_parte = input().split(', ') #Recebe as partes do monstro.

        dict_partes[entrada_parte[0]] = (entrada_parte[1], int(
            entrada_parte[2]), (int(entrada_parte[3]), int(entrada_parte[4])))

    return dict_partes


def combate(lista_monstro: list)-> tuple:
    '''
   Função que lê o ataque da aloy e aplica esse ataque ao alvo.

   Parâmetros:
   -lista_monstro: lista de monstros da rodada, ou seja, todos os monstos que a aloy pode atacar.

   Retorno:
   -Tupla:

   -vida do monstro depois de receber o ataque
   -índice do monstro atacado
   -flecha usada para atacar o monstro
   -um booleano que diz se a aloy acertou um crítico ou não
   -o ponto que a aloy acertou 
        
    '''

    monstro_atacado, parte, flecha_usada, x, y = input().split(', ')  #Recebe o ataque da aloy
    monstro_atacado = int(monstro_atacado)
    ponto = (int(x), int(y))
    monstro = lista_monstro[monstro_atacado]
    lista_partes = monstro.partes
    info_parte = lista_partes[parte]
    

    if info_parte[0] == flecha_usada or info_parte[0] == 'todas':
        if info_parte[2] == ponto:
            monstro.vida_monstro -= info_parte[1]
            
            return monstro.vida_monstro, monstro_atacado, flecha_usada, True, ponto
        else:
            D = info_parte[1] - ((abs((ponto[0] - info_parte[2][0]))) +
                                 (abs((ponto[1] - info_parte[2][1]))))
            if D > 0:
                monstro.vida_monstro -= D
                return monstro.vida_monstro, monstro_atacado, flecha_usada, False, ponto
            else:
                return monstro.vida_monstro, monstro_atacado, flecha_usada , False, ponto

    elif info_parte[0] != flecha_usada:
        if info_parte[2] == ponto:
            D = info_parte[1] - ((abs((ponto[0] - info_parte[2][0]))) +
                                    (abs((ponto[1] - info_parte[2][1]))))
            if D > 0:
                monstro.vida_monstro -= D//2
                return monstro.vida_monstro, monstro_atacado, flecha_usada, True, ponto
            else:
                return monstro.vida_monstro, monstro_atacado, flecha_usada, False , ponto
        else: 
            D = info_parte[1] - ((abs((ponto[0] - info_parte[2][0]))) +
                                    (abs((ponto[1] - info_parte[2][1]))))
            if D > 0:
                monstro.vida_monstro -= D//2
                return monstro.vida_monstro, monstro_atacado, flecha_usada, False, ponto
            else:
                return monstro.vida_monstro, monstro_atacado, flecha_usada, False, ponto


def monstro_ataca_aloy(lista_monstro):
    '''
    Função que faz com que os monstros da rodada ataque a aloy se eles estiverem vivos

    Parâmetros:
    -lista_monstro: lista de monstros da rodada, que podem atacar a aloy.

    Retorno:
    -total de dano que a aloy vai tomar
    
    '''
    total_dano = 0
    for maquina in lista_monstro:
        if maquina.vida_monstro > 0:
            total_dano += maquina.ataque

    return total_dano


def main():
    aloy = ler_aloy()  # Criação da instância aloy da classe Player.
    flechas_copia = aloy.flechas.copy()
    monstros_restantes = int(input())  # Número total de monstros.
    
    ponto = 0
    
    rodada = -1
    while True:
        
        lista_monstros = le_monstros_rodada()  # lista de monstros da rodada
        rodada += 1
        quantidade_flechas_usadas = {}
        turno = 0
        
        dict_criticos = {}
        while aloy.vida > 0 and aloy.flechas_restantes() > 0:
        
            vida_monstro, monstro_atacado, flecha_usada, foi_critico, ponto = combate(
                lista_monstros)
            if foi_critico == True:
                if monstro_atacado not in dict_criticos:
                    dict_criticos[monstro_atacado] = dict()
                if ponto not in dict_criticos[monstro_atacado]:
                    dict_criticos[monstro_atacado][ponto] = 1
                elif ponto in dict_criticos[monstro_atacado]:
                    dict_criticos[monstro_atacado][ponto] += 1
            

            aloy.usar_flechas(flecha_usada)
            aloy.flechas_restantes()

            if flecha_usada not in quantidade_flechas_usadas:
                quantidade_flechas_usadas[flecha_usada] = 1
            else:
                quantidade_flechas_usadas[flecha_usada] += 1
            
            if turno == 0:
                print(f'Combate {rodada}, vida = {aloy.vida}')

            if lista_monstros[monstro_atacado].vida_monstro <= 0:
                print(f'Máquina {monstro_atacado} derrotada')

            if (turno+1) % 3 ==  0:
                dano_monstros = monstro_ataca_aloy(lista_monstros)
                aloy.tomar_dano(dano_monstros)
                
            lista_monstros_mortos = []
            for maquina in lista_monstros:
                if maquina.vida_monstro <= 0:
                    lista_monstros_mortos.append(maquina)
                    
            if len(lista_monstros_mortos) == len(lista_monstros):
                print(f'Vida após o combate = {aloy.vida}')
                aloy.recuperar_vida()   
                print('Flechas utilizadas:')
                for k, v in flechas_copia.items():
                    if k in quantidade_flechas_usadas:
                        print(f'- {k}: {quantidade_flechas_usadas[k]}/{flechas_copia[k]}')

            
                if len(dict_criticos) != 0: 
                    print('Críticos acertados:')
                    for indice_monstro in range(len(lista_monstros)):
                            if indice_monstro not in dict_criticos:
                                continue
                            
                            print(f'Máquina {indice_monstro}:')
                            monstro = lista_monstros[indice_monstro]
                            for parte in monstro.partes:
                                ponto = monstro.partes[parte][2]
                                if ponto in dict_criticos[indice_monstro]:
                                    print(f'- {ponto}: {dict_criticos[indice_monstro][ponto]}x')
                            
                
                aloy.flechas = flechas_copia.copy()
                monstros_restantes -= len(lista_monstros_mortos)
                break
                        

            turno += 1

        if aloy.vida <= 0 or aloy.flechas_restantes() == 0 or monstros_restantes == 0:
            break
        

    if aloy.vida <= 0:
        print(f'Vida após o combate = {aloy.vida}')
        print('Aloy foi derrotada em combate e não retornará a tribo.')

    elif aloy.flechas_restantes() <= 0:
        print(f'Vida após o combate = {aloy.vida}')
        print('Aloy ficou sem flechas e recomeçará sua missão mais preparada.')

    else:
        print('Aloy provou seu valor e voltou para sua tribo.')


if __name__ == "__main__":
    main()
