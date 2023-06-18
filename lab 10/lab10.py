class Player:

    def __init__(self, vida, flechas):
        self.vida_inicial = vida
        self.vida = vida
        self.flechas = flechas

    def tomar_dano(self, dano):
        self.vida -= dano
        return self.vida

    def recuperar_vida(self):

        if self.vida + self.vida_inicial*0.5 <= self.vida_inicial:
            self.vida += self.vida_inicial*0.5

        else:
            self.vida = self.vida_inicial

    def recuperar_flechas(self, dicionario: dict):
        self.flechas.update(dicionario)


class Monster:

    def __init__(self, vida_monstro, ataque, num_partes, partes=None):
        self.vida_monstro = vida_monstro
        self.ataque = ataque
        self.num_partes = num_partes
        self.partes = partes

    def tomar_dano(self,  dano: int) -> None:
        self.vida_monstro -= dano
        return self.vida_monstro

  # def monstro_ataca_aloy(self, lista: list, aloy) -> None:
      # aloy.vida -= sum(lista)


def ler_aloy():
    '''Função que lê a vida da aloy e suas flechas'''
    vida_aloy = int(input())
    # Recebe a entrada dos tipos de flecha e suas quantidades e guarda em uma lista
    flechas_temp = input().split()
    flechas = {}

    # Esse loop serve pra transformar os dados da lista em um dicionário onde os tipos de flecha são a chave e sua quantidade são os valores.
    for i in range(0, len(flechas_temp), 2):
        flechas[flechas_temp[i]] = int(flechas_temp[i+1])

    return Player(vida_aloy, flechas)


def le_monstros_rodada() -> None:
    '''Função que lê os monstros por rodada e adiciona eles em uma lista'''

    lista_monstros = []
    monstros_por_rodada = int(input())

    for _ in range(monstros_por_rodada):
        # Recebe a vida, o dano e a quantidade de partes do monstro.
        entrada_atributos = input()
        # Transforma os atributos em int
        vida, ataque, num_partes = map(int, entrada_atributos.split())
        partes = ler_partes_monstro(num_partes)
        monstro = Monster(vida, ataque, num_partes, partes)

        lista_monstros.append(monstro)

    return lista_monstros


def ler_partes_monstro(num_partes: int) -> list:
    '''Função que lê as partes dos monstros e adiciona em um dicionário'''

    dict_partes = {}
    for _ in range(num_partes):

        entrada_parte = input().split(', ')

        dict_partes[entrada_parte[0]] = [entrada_parte[1], int(
            entrada_parte[2]), (int(entrada_parte[3]), int(entrada_parte[4]))]

    return dict_partes


def combate(lista_monstro: list)-> tuple:
    '''Função em que a Aloy ataca o monstro e retorna a vida do monstro resultante, o monstro atacado, a flecha usada,se acertou crítico ou não e o ponto de crítico'''

    monstro_atacado, parte, flecha_usada, x, y = input().split(', ')
    monstro_atacado = int(monstro_atacado)
    ponto = (int(x), int(y))
    monstro = lista_monstro[monstro_atacado]
    lista_partes = monstro.partes
    info_parte = lista_partes[parte]
    criticos_acertados = 0

    if info_parte[0] == flecha_usada or info_parte[0] == 'todas':
        if info_parte[2] == ponto:
            monstro.vida_monstro -= info_parte[1]
            criticos_acertados += 1
            return monstro.vida_monstro, monstro_atacado, flecha_usada, criticos_acertados, ponto
        else:
            D = info_parte[1] - ((abs((ponto[0] - info_parte[2][0]))) +
                                 (abs((ponto[1] - info_parte[2][1]))))
            if D > 0:
                monstro.vida_monstro -= D
                return monstro.vida_monstro, monstro_atacado, flecha_usada, None, None
            else:
                return monstro.vida_monstro, 0, flecha_usada , None, None

    elif info_parte[0] != flecha_usada:
        if D > 0:
            monstro.vida_monstro -= D//2
            return monstro.vida_monstro, monstro_atacado, flecha_usada, None, None
        else:
            return monstro.vida_monstro, 0, flecha_usada, None, None


def monstro_ataca_aloy(lista_monstro):
    total_dano = 0
    for maquina in lista_monstro:
        if maquina.vida_monstro > 0:
            total_dano += maquina.ataque

    return total_dano


def main():
    aloy = ler_aloy()  # Criação da instância aloy da classe Player.
    total_monstros = int(input())  # Número total de monstros.
    total_flechas = sum(aloy.flechas.values())
    criticos_acertados = 0
    ponto = 0
    quantidade_flechas_usadas = {}

    lista_monstros = le_monstros_rodada()  # lista de monstros da rodada
    # aloy.tomar_dano()
    i = 0
    while aloy.vida > 0 and total_flechas > 0 and i != total_monstros:
    
        vida_monstro, monstro_atacado, flecha_usada, criticos_acertados, ponto = combate(
            lista_monstros)
        if flecha_usada not in quantidade_flechas_usadas:
            quantidade_flechas_usadas[flecha_usada] = 1
        else:
            quantidade_flechas_usadas[flecha_usada] += 1
        print(f'Combate {i}, vida = {aloy.vida}')
        if vida_monstro <= 0:
            print(f'Máquina {monstro_atacado} derrotada')

        

        if i % 2 == 0 and i != 0:
            dano_monstros = monstro_ataca_aloy(lista_monstros)
            aloy.tomar_dano(dano_monstros)
            

        for maquina in lista_monstros:
            if maquina.vida_monstro > 0:
                total_dano += maquina.ataque
        i += 1
        
        aloy.recuperar_vida()
        print(f'Vida após o combate = {aloy.vida}')
        print('Flechas utilizadas:')
        for k, v in quantidade_flechas_usadas.items():
            print(f'-{k}: {v}/{aloy.flechas[flecha_usada]}')
        if criticos_acertados != None:
            print('Críticos acertados:')
            print(f'Máquina {monstro_atacado}')
            print(f'- {ponto}: {criticos_acertados}x')
        aloy.recuperar_flechas(quantidade_flechas_usadas)
        

        

    if aloy.vida < 0:
        print('Aloy foi derrotada em combate e não retornará a tribo.')

    if total_flechas < 0:
        print('Aloy ficou sem flechas e recomeçará sua missão mais preparada.')

    if i == total_monstros:
        print('Aloy provou seu valor e voltou para sua tribo.')


if __name__ == "__main__":
    main()
