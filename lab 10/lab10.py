class Player():

    def __init__(self, vida,flechas):
        self.vida = vida
        self.flechas = flechas
        
    



class Monster():


    def __init__(self,vida_monstro, ataque, num_partes):
        self.vida_monstro = vida_monstro
        self.ataque = ataque
        self.num_partes = num_partes

    

def ler_aloy():
    '''Função que lê a vida da aloy e suas flechas'''
    vida_aloy = int(input())  #Recebe a vida da aloy
    flechas_temp = input().split()  #Recebe a entrada dos tipos de flecha e suas quantidades e guarda em uma lista
    flechas = {}

    for i in range(0,len(flechas_temp),2):    #Esse loop serve pra transformar os dados da lista em um dicionário onde os tipos de flecha são a chave e sua quantidade são os valores.
        flechas[flechas_temp[i]] = int(flechas_temp[i+1])

    return Player(vida_aloy, flechas)



def le_monstros_rodada()->list:
    '''Função que lê os monstros e adiciona eles em uma lista'''
    lista_monstros = []
    monstros_por_rodada = int(input())
    
    for _ in range(monstros_por_rodada):
        m = le_monstro()
        lista_monstros.append(m)

    return lista_monstros


def le_monstro()->None:
    '''Função que lê um monstro e transforma ele em uma instância da Classe Monstro'''
    entrada = input().split()
    monstro = Monster(int(entrada[0]),int(entrada[1]),int(entrada[2]))

    
    dict_partes = {}
    for i in range(monstro.num_partes):
        entrada1 = input().split(', ')
        dict_partes[entrada1[0]] = [int(entrada[1]),int(entrada[2]), (int(entrada[3]),int(entrada[4]))]
        
        








    return monstro

    



    

    
        






def main():
    aloy = ler_aloy()
    monstros = le_monstros_rodada()
    




if __name__ == "__main__":
    main()
    




    








        
