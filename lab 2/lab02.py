print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.')

print('Seu SO anterior era Linux?')
print('(0) Não')
print('(1) Sim')


Era_Linux = input()
if (Era_Linux == '0'):
    print('Seu SO anterior era um MacOS?')

    print('(0) Não')
    print('(1) Sim')

    Era_MacOS = input()
    if (Era_MacOS == '0'):
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.')
    elif (Era_MacOS == '1'):
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.')

    else:
        print('Opção inválida, recomece o questionário.')
elif (Era_Linux == '1'):
    print('É programador/ desenvolvedor ou de áreas semelhantes?')

    print('(0) Não')
    print('(1) Sim')
    print('(2) Sim, realizo testes e invasão de sistemas')

    Era_programador = input()
    if (Era_programador == '0'):
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.')
    elif (Era_programador == '2'):
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.')
    elif (Era_programador == '1'):
        print('Gostaria de algo pronto para uso ao invés de ficar configurando o SO?')

        print('(0) Não')
        print('(1) Sim')

        Queria_pronto = input()
        if (Queria_pronto == '0'):
            print('Já utilizou Arch Linux?')
            print('(0) Não')
            print('(1) Sim')
            Usou_Linux = input()
            if (Usou_Linux == '0'):
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.')
            elif (Usou_Linux == '1'):
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.')
            else:
                print('Opção inválida, recomece o questionário.')

        elif (Queria_pronto == '1'):
            print('Já utilizou Debian ou Ubuntu?')
            print('(0) Não')
            print('(1) Sim')
            Já_Usou = input()
            if (Já_Usou == '0'):
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.')
            elif (Já_Usou == '1'):
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.')
            else:
                print('Opção inválida, recomece o questionário.')

        else:
            print('Opção inválida, recomece o questionário.')
else:
    print('Opção inválida, recomece o questionário.')
