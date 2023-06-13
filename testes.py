class Monster():


    def __init__(self,vida_monstro, ataque, num_partes):
        self.vida_monstro = vida_monstro
        self.ataque = ataque
        self.num_partes = num_partes



total = int(input())
lista_monstros = []


for _ in range(total):
    entrada = input().split()
    monstro = Monster(entrada[0],entrada[1],entrada[2])
    lista_monstros.append(monstro)





print(lista_monstros[0].vida_monstro)


























    

                     
                      
               
             
      














    





