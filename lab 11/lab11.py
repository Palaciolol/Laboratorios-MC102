# Um herói e uma missão.

class Player:

    def __init__(self, vida, ataque, x, y) -> None:
        self.vida = vida
        self.ataque = ataque
        self.x = x
        self.y = y

    def tomar_dano(self, dano):
        '''
        Função que o link toma dano de um monstro

        Parâmetros:
        -dano: dano que o link vai receber
        
        '''

        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0

    def descer_tudo(self, mat):
        '''Função em que o link se move pra baixo na matriz
        atualiza a matriz com a posição do link
        atualiza a posição do link
        '''
        mat[self.x][self.y] = "."
        mat[self.x + 1][self.y] = "P"
        self.x = self.x + 1

    def mover(self, mat):
        '''
        Função que o link se move uma vez que ele está na última linha da matriz
        
        Parâmetros:
        mat: matriz 

        atualiza a matriz com a nova posição do link
        atualiza a posição do link depois que ele se move
        
        
        '''


        if self.x % 2 == 0:
            if self.y == 0:
                mat[self.x][self.y] = "."
                mat[self.x - 1][self.y] = "P"
                self.x = self.x - 1

            else:
                mat[self.x][self.y] = "."
                mat[self.x][self.y - 1] = "P"
                self.y = self.y - 1

        else:
            if self.y == len(mat[0]) - 1:
                mat[self.x][self.y] = "."
                mat[self.x - 1][self.y] = "P"
                self.x = self.x - 1
            else:
                mat[self.x][self.y] = "."
                mat[self.x][self.y + 1] = "P"
                self.y = self.y + 1

    def buffar(self, tipo, buff):
        '''Função que o link adquiri novos status de vida ou de dano
        Parâmetros:
        -tipo: tipo do buff que o link vai receber
        -buff: valor numérico do status recebido
        
        '''
        if tipo == "ataque":
            if self.ataque + buff <= 0:
                self.ataque = 1
            else:
                self.ataque += buff

        else:
            self.vida += buff


class Monster:

    def __init__(self, vida, ataque, tipo, x, y):
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.x = x
        self.y = y

    def mover(self, mat):
        '''Função que move os monstros, ela verifica se ele pode se mover na matriz e se ele tem vida pra isso, depois ele se move normalmente'''
        if self.tipo == "U" and self.vida > 0:
            if self.x - 1 >= 0:
                if (
                    mat[self.x][self.y] == "P"
                    or mat[self.x][self.y] == "*"
                    
                ):
                    mat[self.x - 1][self.y] = "U"
                    self.x = self.x - 1
                elif  mat[self.x ][self.y ] == 'D'or mat[self.x ][self.y ] == 'L' or mat[self.x ][self.y ] == 'R':
                    mat[self.x-1][self.y] = self.tipo
                    self.x = self.x -1 
                else:
                    mat[self.x][self.y] = "."
                    if mat[self.x-1][self.y] != '*' and mat[self.x-1][self.y] != 'P':
                        mat[self.x - 1][self.y] = "U"
                    self.x = self.x - 1
            elif mat[self.x][self.y] != "P" and mat[self.x][self.y] != '*':
                mat[self.x][self.y] = self.tipo

        elif self.tipo == "D" and self.vida > 0:
            if self.x + 1 < len(mat):
                if (
                    mat[self.x][self.y] == "P"
                    or mat[self.x][self.y] == "*"
                    
                    
                ):
                    mat[self.x + 1][self.y] = "D"
                    self.x = self.x + 1
                elif  mat[self.x ][self.y ] == 'U'or mat[self.x][self.y ] == 'L' or mat[self.x][self.y ] == 'R':
                    mat[self.x+1][self.y] = self.tipo
                    self.x = self.x +1

                else:
                    mat[self.x][self.y] = "."
                    if mat[self.x+1][self.y] != '*' and mat[self.x][self.y-1] != 'P':
                        mat[self.x + 1][self.y] = "D"
                    self.x = self.x + 1
            elif mat[self.x][self.y] != "P" and mat[self.x][self.y] != '*':
                mat[self.x][self.y] = self.tipo

        elif self.tipo == "L" and self.vida > 0:
            if self.y - 1 >= 0:
                if (
                    mat[self.x][self.y] == "P"
                    or mat[self.x][self.y] == "*"
                    
                ):
                    mat[self.x][self.y - 1] = "L"
                    self.y = self.y - 1

                elif  mat[self.x ][self.y ] == 'D'or mat[self.x][self.y ] == 'U' or mat[self.x][self.y ] == 'R':
                    mat[self.x][self.y-1] = self.tipo
                    self.y = self.y -1

                else:
                    mat[self.x][self.y] = "."
                    if mat[self.x][self.y-1] != '*' and mat[self.x][self.y-1] != 'P':
                        mat[self.x][self.y - 1] = "L"
                    self.y = self.y - 1

            elif mat[self.x][self.y] != "P" and mat[self.x][self.y] != '*':
                mat[self.x][self.y] = self.tipo

        elif self.tipo == "R" and self.vida > 0:
            if self.y + 1 < len(mat[0]):
                if (
                    mat[self.x][self.y] == "P"
                    or mat[self.x][self.y] == "*"
                    
                ):
                    mat[self.x][self.y + 1] = "R"
                    self.y = self.y + 1

                elif  mat[self.x ][self.y ] == 'D'or mat[self.x][self.y ] == 'L' or mat[self.x][self.y ] == 'U':
                    mat[self.x][self.y+1] = self.tipo
                    self.y = self.y +1

                else:
                    mat[self.x][self.y] = "."
                    if mat[self.x][self.y+1] != '*' and mat[self.x][self.y+1] != 'P':
                        mat[self.x][self.y + 1] = "R"
                    self.y = self.y + 1
            elif mat[self.x][self.y] != "P" and mat[self.x][self.y] != '*':
                mat[self.x][self.y] = self.tipo

    def colocar_na_matriz(self, mat):
        '''Função que coloca os monstros na matriz se a posição a ser colocada for diferentes da saída da masmorra , do link e do link morto'''
        if mat[self.x][self.y] != "*" and mat[self.x][self.y] != 'P' and mat[self.x][self.y] != 'X':
            mat[self.x][self.y] = self.tipo


class Item:
    
    def __init__(self, nome, tipo, x, y, status,usado = False) -> None:
        self.nome = nome
        self.tipo = tipo
        self.x = x
        self.y = y
        self.status = status
        self.usado = usado

    def inserir_na_matriz(self, mat):
        '''Função que insere os itens na matriz'''
        mat[self.x][self.y] = self.tipo



def imprime_masmorra(mat: list[list[str]]) -> None:
    """Função que que recebe como parâmetro uma lista de listas e imprime a matriz"""
    for linha in mat:
        for caractere in range(len(linha)):
            if caractere == len(linha) - 1:
                print(linha[caractere], end="")

            else:
                print(linha[caractere], end=" ")

        print()


def ler_link():
    """Função que lê a vida de Link e seus pontos de ataque
    
    """
    entrada_atributos = input()
    vida_link, ataque_link = map(int, entrada_atributos.split())

    return (vida_link, ataque_link)


def ler_monstros():
    '''
    Função que lê os monstros e transforma cada um deles em uma instância da classe Monster 
    
    Retorno:
    -lista de monstros
    '''
    lista_monstros = []
    tot_monstros = int(input())

    for _ in range(tot_monstros):
        entrada_atributos_monstro = input().split()
        vida, ataque, tipo, pos = (
            int(entrada_atributos_monstro[0]),
            int(entrada_atributos_monstro[1]),
            entrada_atributos_monstro[2],
            entrada_atributos_monstro[3],
        )
        x_monstro, y_monstro = map(int, pos.split(","))
        monstro = Monster(vida, ataque, tipo, x_monstro, y_monstro)
        lista_monstros.append(monstro)

    return lista_monstros


def ler_objetos():
    """Função que lê os objetos e cria uma instância da classe Item
    Retorno:
    -lista de objetos
    """
    lista_objetos = []
    tot_objetos = int(input())

    for _ in range(tot_objetos):
        entrada_objetos = input().split()
        nome_objeto, tipo, (pos), status = (
            entrada_objetos[0],
            entrada_objetos[1],
            entrada_objetos[2],
            int(entrada_objetos[3]),
        )
        x_objeto, y_objeto = map(int, pos.split(","))
        objeto = Item(nome_objeto, tipo, x_objeto, y_objeto, status)
        lista_objetos.append(objeto)

    return lista_objetos


def link_ataca(ataque: int, monstro: Monster):
    """Função que o link ataca um monstro
    
    Parâmetros:
    -ataque: dano que vai ser aplicado no monstro
    -monstro: monstro atacado
    
    """

    monstro.vida -= ataque


def pegar_item(vida: int, ataque: int, item: Item):
    """Função que o link pega um item
    
    Parâmetros:
    -vida: vida do link
    -ataque: ataque do link
    -item: item que o link pegou

    Retorno:
    - tipo de buff que ele recebe, valor numérico do buff
    
    """
    if item.tipo == "d":
        return "ataque", item.status
    
    else:
        return "vida", item.status

def main():
    vida_link, ataque_link = ler_link()  

    entrada_masmorra = input()
    num_linhas, num_colunas = map(int, entrada_masmorra.split())
    mat = []
    for _ in range(num_linhas):
        l = []
        for _ in range(num_colunas):
            l.append(".")
        mat.append(l)

    entrada_pos_inicial_link = input()
    x_link, y_link = map(int, entrada_pos_inicial_link.split(","))
    mat[x_link][y_link] = "P"

    link = Player(vida_link, ataque_link, x_link, y_link)

    entrada_pos_saida = input()
    x_saida, y_saida = map(int, entrada_pos_saida.split(","))
    mat[x_saida][y_saida] = "*"

    lista_monstros = ler_monstros()    

    lista_objetos = ler_objetos()

    for objeto in lista_objetos:
        objeto.inserir_na_matriz(mat)

    for monstro in lista_monstros:
        monstro.colocar_na_matriz(mat)

    imprime_masmorra(mat)
    print()
    while link.vida > 0 and link.x != (len(mat)-1):
        link.descer_tudo(mat)
        for monstro in lista_monstros:
            monstro.mover(mat)
        for objeto in lista_objetos:
                if (link.x, link.y) == (objeto.x, objeto.y):
                    if objeto.usado == False:
                        tipo, buff = pegar_item(link.vida, link.ataque, objeto)
                        link.buffar(tipo, buff)
                        print(
                            f"[{objeto.tipo}]Personagem adquiriu o objeto {objeto.nome} com status de {objeto.status}"
                    )
                        objeto.usado = True
                
        for monstro in lista_monstros:
            if (link.x, link.y) == (monstro.x, monstro.y):
                dano_realizado = min(link.ataque, monstro.vida)
                link_ataca(link.ataque, monstro)
                print(
                    f"O Personagem deu {dano_realizado} de dano ao monstro na posicao ({link.x}, {link.y})"
                )
                if monstro.vida > 0:
                    lista_dano = [link.vida, monstro.ataque]
                    dano_tomado = sorted(lista_dano)
                    link.tomar_dano(monstro.ataque)
                    print(
                        f"O Monstro deu {dano_tomado[0]} de dano ao Personagem. Vida restante = {link.vida}"
                    )

                if link.vida <= 0:
                    mat[link.x][link.y] = "X"
                    break
        
        
        for objeto in lista_objetos:
            if objeto.tipo == 'd':
                if (objeto.usado == False and mat[objeto.x][objeto.y] == '.') or (mat[objeto.x][objeto.y] == 'v' and objeto.usado == False):
                    objeto.inserir_na_matriz(mat)
            else:
                if (objeto.usado == False and mat[objeto.x][objeto.y] == '.') or (mat[objeto.x][objeto.y] == 'd' and objeto.usado == False):
                    objeto.inserir_na_matriz(mat)
                         
        for monstro in lista_monstros:
            monstro.colocar_na_matriz(mat)
        imprime_masmorra(mat)
        print() 

    while link.vida > 0 and (link.x, link.y) != (x_saida, y_saida):
        link.mover(mat)
        

        for monstro in lista_monstros:
            monstro.mover(mat)

        for objeto in lista_objetos:
            if (link.x, link.y) == (objeto.x, objeto.y):
                if objeto.usado == False:
                    tipo, buff = pegar_item(link.vida, link.ataque, objeto)
                    link.buffar(tipo, buff)
                    print(
                        f"[{objeto.tipo}]Personagem adquiriu o objeto {objeto.nome} com status de {objeto.status}"
                )
                    objeto.usado = True
            
        for monstro in lista_monstros:
            if (link.x, link.y) == (x_saida, y_saida):
                break
            if (link.x, link.y) == (monstro.x, monstro.y):
                dano_feito = min(link.ataque, monstro.vida)

                link_ataca(link.ataque, monstro)
                print(
                    f"O Personagem deu {dano_feito} de dano ao monstro na posicao ({link.x}, {link.y})"
                )
                if monstro.vida > 0:
                    lista_dano_resultante = [link.vida,monstro.ataque]
                    dano_resultante = sorted(lista_dano_resultante)
                    link.tomar_dano(monstro.ataque)
                    print(
                        f"O Monstro deu {dano_resultante[0]} de dano ao Personagem. Vida restante = {link.vida}"
                    )

                if link.vida <= 0:
                    mat[link.x][link.y] = "X"
                    break
        
        for objeto in lista_objetos:
            if objeto.tipo == 'd':
                if (objeto.usado == False and mat[objeto.x][objeto.y] == '.') or (mat[objeto.x][objeto.y] == 'v' and objeto.usado == False):
                    objeto.inserir_na_matriz(mat)
            else:
                if (objeto.usado == False and mat[objeto.x][objeto.y] == '.') or (mat[objeto.x][objeto.y] == 'd' and objeto.usado == False):
                    objeto.inserir_na_matriz(mat)

        imprime_masmorra(mat)
        print()

    if (link.x, link.y) == (x_saida, y_saida):
        print("Chegou ao fim!")


if __name__ == "__main__":
    main()
