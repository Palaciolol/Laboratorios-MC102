#Programa que decifra mensagens.


operacao = input() #Operação a ser feita com a posição dos caracteres procurados na string dada.Pode ser "+" , "-" ou "*".

caractere1 = input() #Primeiro caractere a ser procurado na string

caractere2 = input() #Segundo caractere a ser procurado na string.

linhas = int(input()) #Número de linhas da mensagem.

soma_mensagem = ''


for i in range(0,linhas):
    mensagem = input() #Mensagem a ser decodificada.
    soma_mensagem += mensagem


def verificacao(caracter1: str)->int:
    
    def verificacao2(caractere2:str)->int:
        if caractere2 == 'vogal':
            for c in range(x,len(soma_mensagem)):
                if soma_mensagem[c] in 'AEIOUaeiou':
                    y = c
                    return y

        elif caractere2 == 'consoante':
            for c in range(x,len(soma_mensagem)):
                if soma_mensagem[i].isalpha():
                    if soma_mensagem[c] not in 'AEIOUaeiou':
                        y = c
                        return y
                        
        elif caractere2 == 'numero':
            for c in range(x,len(soma_mensagem)):
                if soma_mensagem[c] in '0123456789':
                    y = c
                    return y


        else:
            y = soma_mensagem.find(caractere2)
            return y
        
    
    
    
    
    
    
    if caracter1 == 'vogal':
        for i in range(0,len(soma_mensagem)):
            if soma_mensagem[i] in 'AEIOUaeiou':
                x = i
                y = verificacao2(caractere2)
                return (x, y)




    elif caracter1 == ' consoante':
        for i in range(0,len(soma_mensagem)):
            if soma_mensagem[i].isalpha():
                if soma_mensagem[i] not in 'AEIOUaeiou':
                    x = i
                    y = verificacao2(caractere2)
                    return (x, y)
    elif caracter1 == 'numero':
        for i in range(0,len(soma_mensagem)):
                if soma_mensagem[i] in '0123456789':
                    x = i
                    y = verificacao2(caractere2)
                    return (x, y)


    else:
        x = soma_mensagem.find(caracter1)
        y = verificacao2(caractere2)
        return (x,y)





x, y = verificacao(caractere1)


if operacao == '+':
    chave = x + y

elif operacao == '-':
    chave = x - y

elif operacao == '*':
    chave = x * y

print(chave)










    
            
            





        







