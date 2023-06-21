#Um herói e uma missão.

class Player():

    def __init__(self,vida, ataque,x, y) -> None:
        self.vida = vida
        self.ataque = ataque
        self.x = x
        self.y = y


    def tomar_dano(self, dano):
        self.vida -= dano
    
    def descer_tudo(self,mat):
        mat[self.x][self.y] = '.'
        mat[self.x+1][self.y] = 'P'
        self.x = self.x+1

    def mover(self,mat):
        '''Função que move o link'''
        
        if self.x % 2 == 0:
            if self.y ==  0:
                mat[self.x][self.y] = '.'
                mat[self.x-1][self.y] = 'P'
                self.x = self.x -1
                
            else:
                mat[self.x][self.y] = '.'
                mat[self.x][self.y-1] = 'P'
                self.y = self.y - 1

        else:
            if self.y == len(mat[0])-1:
                mat[self.x][self.y] = '.'
                mat[self.x-1][self.y] = 'P'
                self.x = self.x - 1
            else:
                mat[self.x][self.y] = '.'
                mat[self.x][self.y+1] = 'P'
                self.y = self.y +1
    
    def buffar(self, tipo, buff):
        if tipo == 'ataque':
            if self.ataque  + buff <= 0:
                self.ataque == 1
            else:
                self.ataque += buff
        
        else:
            self.vida = self.vida + buff

        



class Monster():

    def __init__(self, vida, ataque, tipo, x, y):
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.x = x
        self.y = y

    def mover(self,mat):
        if self.tipo == 'U':
            if self.x -1 >= 0:
                if mat[self.x][self.y] == 'P':
                    mat[self.x -1][self.y] = 'U'
                    self.x = self.x -1
                else:
                    mat[self.x][self.y] = '.'
                    mat[self.x -1][self.y] = 'U'
                    self.x = self.x -1

        elif self.tipo == 'D':
            if self.x +1 < len(mat):
                if mat[self.x][self.y] == 'P':
                    mat[self.x +1][self.y] = 'D'
                    self.x = self.x + 1
                else:
                    mat[self.x][self.y] = '.'
                    mat[self.x +1][self.y] = 'D'
                    self.x = self.x + 1
                

        elif self.tipo == 'L':
            if  self.y -1 > 0:
                if mat[self.x][self.y] == 'P':
                    mat[self.x][self.y-1] = 'L'
                    self.y = self.y - 1
                    
                else:
                    mat[self.x][self.y] = '.'
                    mat[self.x][self.y-1] = 'L'
                    self.y = self.y - 1

        
        elif self.tipo == 'R':
            if self.y +1 < len(mat[0]):
                if mat[self.x][self.y] == 'P':
                    mat[self.x][self.y+1] = 'R'
                    self.y = self.y + 1
                else:
                    mat[self.x][self.y] = '.'
                    mat[self.x][self.y+1] = 'R'
                    self.y = self.y + 1


    def colocar_na_matriz(self,mat):
        mat[self.x][self.y] = self.tipo


        

class Item():

    def __init__(self, nome, tipo, x, y, status) -> None:
        self.nome = nome
        self.tipo = tipo
        self.x = x
        self.y = y
        self.status = status    
    

    def inserir_na_matriz(self,mat):
        mat[self.x][self.y] = self.tipo

    

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

    return (vida_link,ataque_link)


def ler_monstros():
    '''Função que lê os monstros '''
    lista_monstros = []
    tot_monstros = int(input())

    for _ in range(tot_monstros):
        entrada_atributos_monstro = input().split()
        vida, ataque, tipo,(pos)  = int(entrada_atributos_monstro[0]), int(entrada_atributos_monstro[1]), entrada_atributos_monstro[2], entrada_atributos_monstro[3]
        x_monstro, y_monstro = map(int,pos.split(','))
        monstro = Monster(vida, ataque, tipo, x_monstro, y_monstro)
        lista_monstros.append(monstro)

    
    return lista_monstros

def ler_objetos():
    '''Função que lê os objetos'''
    lista_objetos = []
    tot_objetos = int(input())

    for _ in range(tot_objetos):
        entrada_objetos = input().split()
        nome_objeto, tipo, (pos), status = entrada_objetos[0], entrada_objetos[1], entrada_objetos[2],int(entrada_objetos[3])
        x_objeto, y_objeto = map(int, pos.split(','))
        objeto = Item(nome_objeto, tipo, x_objeto, y_objeto, status)
        lista_objetos.append(objeto)


    return lista_objetos


def link_ataca(ataque: int,monstro: Monster):
    '''Função que o link ataca um monstro'''

    monstro.vida -= ataque

def pegar_item(vida: int,ataque: int,item: Item):
    '''Função que o link pega um item'''
    if item.tipo == 'd':
        ataque = ataque + item.status
        return 'ataque',ataque
    
    else:
        vida = vida + item.status
        return 'vida',vida

    
def main():
    vida_link, ataque_link = ler_link()
    
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

    link = Player(vida_link,ataque_link, x_link, y_link)
    
    entrada_pos_saida = input()
    x_saida, y_saida = map(int, entrada_pos_saida.split(','))
    mat[x_saida][y_saida] = '*'

    lista_monstros = ler_monstros()
    
    for monstro in lista_monstros:
        monstro.colocar_na_matriz(mat)


    lista_objetos = ler_objetos()

    for objeto in lista_objetos:
        objeto.inserir_na_matriz(mat)

    imprime_masmorra(mat)
    print()
    
    for _ in range(len(mat)-1):
        link.descer_tudo(mat)
        for monstro in lista_monstros:
            monstro.mover(mat)

            imprime_masmorra(mat)
            print()


    while link.vida > 0 and (link.x,link.y) != (x_saida,y_saida):
        link.mover(mat)

        for monstro in lista_monstros:
            monstro.mover(mat)

        for monstro,objeto in zip(lista_objetos,lista_monstros):
            if (link.x,link.y) == (monstro.x,monstro.y) and (link.x,link.y) == (objeto.x,objeto.y):
                tipo,buff = pegar_item(link.vida, link.ataque, objeto)
                link.buffar(tipo,buff)
                print(f'[{objeto.tipo}]Personagem adquiriu o objeto {objeto.nome} com status de {objeto.status}')
                link_ataca(link.ataque,monstro)
                print(f'O personagem deu {link.ataque} de dano ao monstro na posição ({link.x},{link.y})')
                if monstro.vida > 0:
                    link.tomar_dano(monstro.ataque)
                    print(f'O monstro deu {monstro.ataque} de dano ao Personagem. Vida restante = {link.vida}')
                    if link.vida <= 0:
                        mat[link.x][link.y] = 'X'
                        break
            elif (link.x,link.y) == (objeto.x,objeto.y):
                tipo,buff = pegar_item(link.vida, link.ataque, objeto)
                link.buffar(tipo,buff)
                print(f'[{objeto.tipo}]Personagem adquiriu o objeto {objeto.nome} com status de {objeto.status}')


            elif (link.x,link.y) == (monstro.x,monstro.y):
                link_ataca(link.ataque,monstro)
                print(f'O personagem deu {link.ataque} de dano ao monstro na posição ({link.x},{link.y})')
                if monstro.vida > 0:
                    link.tomar_dano(monstro.ataque)
                    print(f'O monstro deu {monstro.ataque} de dano ao Personagem. Vida restante = {link.vida}')
                    if link.vida <= 0:
                        mat[link.x][link.y] = 'X'
                        break
            
        imprime_masmorra(mat)
        print()
            

        if link.vida <= 0:
            break
    if (link.x,link.y) == (x_saida,y_saida):
        print('Chegou ao fim!')


if __name__ == "__main__":
    main()




   
