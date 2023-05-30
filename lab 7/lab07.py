#Programa que decifra mensagens.


operacao = input() #Operação a ser feita com a posição dos caracteres procurados na string dada.Pode ser "+" , "-" ou "*".

caractere1 = input() #Primeiro caractere a ser procurado na string

caractere2 = input() #Segundo caractere a ser procurado na string.

linhas = int(input()) #Número de linhas da mensagem.

mensagens = []


for i in range(0,linhas):
    mensagem = input() #Mensagem a ser decodificada.
    mensagens.append(mensagem)

achar_chave = ''.join(mensagens)





def verificacao(caracter1: str)->int:
    
    def verificacao2(caractere2:str)->int:
        if caractere2 == 'vogal':
            for c in range(x,len(achar_chave)):
                if achar_chave[c] in 'AEIOUaeiou':
                    y = c
                    return y

        elif caractere2 == 'consoante':
            for c in range(x,len(achar_chave)):
                if achar_chave[i].isalpha():
                    if achar_chave[c] not in 'AEIOUaeiou':
                        y = c
                        return y
                        
        elif caractere2 == 'numero':
            for c in range(x,len(achar_chave)):
                if achar_chave[c] in '0123456789':
                    y = c
                    return y


        else:
            y = achar_chave[x:].find(caractere2) + x
            return y
        
    
    
    
    
    
    
    if caracter1 == 'vogal':
        for i in range(0,len(achar_chave)):
            if achar_chave[i] in 'AEIOUaeiou':
                x = i
                y = verificacao2(caractere2)
                return (x, y)




    elif caracter1 == 'consoante':
        for i in range(0,len(achar_chave)):
            if achar_chave[i].isalpha():
                if achar_chave[i] not in 'AEIOUaeiou':
                    x = i
                    y = verificacao2(caractere2)
                    return (x, y)
    elif caracter1 == 'numero':
        for i in range(0,len(achar_chave)):
                if achar_chave[i] in '0123456789':
                    x = i
                    y = verificacao2(caractere2)
                    return (x, y)


    else:
        x = achar_chave.find(caracter1)
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


for m in mensagens:
    msg_decodificada = ''
    for c in m:
        pos1 = (ord(c) + chave - 32) % 95 + 32
        msg_decodificada += chr(pos1)
                         
    

    print(msg_decodificada)










    
            
            





        







