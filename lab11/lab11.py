#Um herói e uma missão.

class Player():

    def __init__(self,vida, ataque,x, y) -> None:
        self.vida = vida
        self.ataque = ataque
        self.x_link = x
        self.y_link = y


    def tomar_dano(self, dano):
        self.vida -= dano
        
    def mover_link(self,mat, x_link, y_link):
        '''Função que move o link'''

        if 'P' not in mat[-1]:
            mat[x_link][y_link] = '.'
            mat[x_link+1][y_link] = 'P'
            
            self.x_link = x_link+1
        
    
        else:
            if x_link % 2 == 0:
                if y_link ==  0:
                    mat[x_link][y_link] = '.'
                    mat[x_link-1][y_link] = 'P'
                else:
                    mat[x_link][y_link] = '.'
                    mat[x_link][y_link-1] = 'P'

            else:
                if y_link == len(mat[0])-1:
                    mat[x_link][y_link] = '.'
                    mat[x_link-1][y_link] = 'P'
                else:
                    mat[x_link][y_link] = '.'
                    mat[x_link][y_link+1] = 'P'
        

        
        

class Monster():

    def __init__(self, vida_monstro, ataque, tipo, x_monstro, y_monstro):
        self.vida_monstro = vida_monstro
        self.ataque = ataque
        self.tipo = tipo
        self.x_monstro = x_monstro
        self.y_monstro = y_monstro

    def mover_monstros(self,mat, ):
        if self.tipo == 'U':
            if self.x_monstro -1 >= 0:
                mat[self.x_monstro][self.y_monstro] = '.'
                mat[self.x_monstro -1][self.y_monstro] = 'U'
                self.x_monstro = self.x_monstro -1

        elif self.tipo == 'D':
            if self.x_monstro +1 < len(mat):
                mat[self.x_monstro][self.y_monstro] = '.'
                mat[self.x_monstro +1][self.y_monstro] = 'D'
                self.x_monstro = self.x_monstro + 1

        elif self.tipo == 'L':
            if  self.y_monstro -1 > 0:
                mat[self.x_monstro][self.y_monstro] = '.'
                mat[self.x_monstro][self.y_monstro-1] = 'L'
                self.y_monstro = self.y_monstro - 1
        
        elif self.tipo == 'R':
            if self.y_monstro +1 < len(mat[0]):
                mat[self.x_monstro][self.y_monstro] = '.'
                mat[self.x_monstro][self.y_monstro+1] = 'R'
                self.y_monstro = self.y_monstro + 1
        

class Item():

    def __init__(self, nome, tipo, posicao, status) -> None:
        self.nome = nome
        self.tipo = tipo
        self.posicao = posicao
        self.status = status    
        

def imprime_masmorra(mat: list[list[str]]) -> None:
    '''Função que que recebe como parâmetro uma lista de listas e imprime a matriz'''
    for linha in mat:
        for caractere in range(len(linha)):
            if caractere == len(linha)-1:
                print(linha[caractere], end='')

            else:
                print(linha[caractere], end=' ')

        print() 


def ler_link():
    '''Função que lê a vida de Link e seus pontos de ataque'''
    entrada_atributos = input()
    vida_link, ataque_link, = map(int, entrada_atributos.split())

    return Player(vida_link,ataque_link)


def ler_monstros(matriz: list[list[str]]):
    '''Função que lê os monstros e os coloca na matriz'''
    lista_monstros = []
    tot_monstros = int(input())

    for _ in range(tot_monstros):
        entrada_atributos_monstro = input().split()
        vida, ataque, tipo,(pos)  = int(entrada_atributos_monstro[0]), int(entrada_atributos_monstro[1]), entrada_atributos_monstro[2], entrada_atributos_monstro[3]
        x_monstro, y_monstro = map(int,entrada_atributos_monstro[3].split(','))
        monstro = Monster(vida, ataque, tipo, x_monstro, y_monstro)
        matriz[x_monstro][y_monstro] = tipo
        lista_monstros.append(monstro)

    
    return lista_monstros, matriz

def ler_objetos(matriz: list[list[str]]):
    '''Função que lê os objetos e os coloca na matriz'''
    lista_objetos = []
    tot_objetos = int(input())

    for _ in range(tot_objetos):
        entrada_objetos = input().split()
        nome_objeto, tipo, (pos), status = entrada_objetos[0], entrada_objetos[1], entrada_objetos[2],int(entrada_objetos[3])
        objeto = Item(nome_objeto, tipo, pos, status)
        x_objeto, y_objeto = map(int, entrada_objetos[2].split(','))
        matriz[x_objeto][y_objeto] = tipo
        lista_objetos.append(objeto)


    return lista_objetos, matriz



def link_ataca_monstro():
    '''Função em que link luta com os monstros'''
    
    
def main():
    link = ler_link()
    
    entrada_masmorra = input()
    num_linhas, num_colunas = map(int, entrada_masmorra.split())
    mat = []
    for _ in range(num_linhas): 
        l = [] 
        for _ in range(num_colunas): 
            l.append('.') 
        mat.append(l) 
    
    entrada_pos_inicial_link = input()
    x_link, y_link = map(int, entrada_pos_inicial_link.split(','))
    mat[x_link][y_link] = 'P'

    entrada_pos_saida = input()
    x_saida, y_saida = map(int, entrada_pos_saida.split(','))
    mat[x_saida][y_saida] = '*'

    lista_monstros, mat = ler_monstros(mat)
    
    lista_objetos,mat = ler_objetos(mat)

    imprime_masmorra(mat)

    

    while (link.vida > 0) and (x_link,y_link) != (x_saida,y_saida):
        novo_x_link, novo_y_link = mover_link(mat, x_link, y_link)
        x_link = novo_x_link
        y_link = novo_y_link
        mover_monstros(mat,lista_monstros)
        print()
        imprime_masmorra(mat)
        

    if x_link == x_saida and y_link == y_saida:
        print('Chegou ao fim!')


if __name__ == "__main__":
    main()




   
