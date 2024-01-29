from datetime import datetime
data = datetime.now()
print('''
    ========== BEM VINDO AO SISTEMA BANCARIO DIO ==========
    =======================================================''')
max_saque = 0
limite_saldo_saque = 0
extrato = []

saldo = 1000

menu = '''
Opções
[1] SACAR
[2] DEPOSITAR
[3] SALDO
[4] EXTRATO    
            
=> '''

# O while vai avaliar se a condição é verdadeira para retornar ao menu
while True:
    opcao = int(input(menu))
    if opcao == 1: #Esse if é pra verificar se a opção chamada no menu é compativel com algum dos laços ifs/elifs
        if  max_saque < 3: #Esse é pra identificar se a quantidade maxima de saques ja foi feita hoje
                print('''
                      =====================================================
                                    FERRAMENTA DE SAQUE DBANK
                      =====================================================
                      ''')
                saque_usuario = int(input('Quanto deseja Sacar: '))
                if saque_usuario > 0 and saque_usuario < saldo:
                    saldo = saldo - saque_usuario
                    print('''
                    ======================================================
                        Você realizou o saque de {saque_usuario} reais
                              {data}
                    ======================================================
                    '''.format(saque_usuario = saque_usuario, data = data))
                    print('''
                    ======================================================
                            Seu limite agora é de {saldo} reais
                               {data}
                    ======================================================
                    '''.format(saldo = saldo,data = data))
                    extrato.append('{data} | | | | Você realizou o saque de {saque_usuario} reais'.format(saque_usuario = saque_usuario, saldo = saldo,data = data))
                    extrato.append('{data} | | | |Saldo total: {saldo} Reais | | | |'.format(saldo = saldo,data = data))
                else:
                    print('Você não tem saldo suficiente!')
        elif max_saque > 3:
            print('''
                   ======================================================
                        Você já realizou o maximo de saques por hoje!
                   ======================================================
                   ''')
        else:print('''
                    ======================================================
                        Você já atingiu o limite de saque diario hoje!
                    ======================================================
                        ''')
        max_saque = max_saque + 1
        limite_saldo_saque = limite_saldo_saque + saque_usuario

        
    elif opcao == 2:
        print('''
              ==================================================
                        FERRAMENTA DE DEPOSITO DBANK
              ==================================================
              ''')
        deposito_usuario = int(input('Quanto Deseja Depositar: '))
        saldo = saldo + deposito_usuario
        print('''
              ==================================================================
                    Você realizou o deposito de {deposito_usuario} reais
                        {data}
              ==================================================================
              '''.format(deposito_usuario = deposito_usuario,data = data))
        print('''
              ========================================================
                        Seu saldo atual é de {saldo} reais
                        {data}
              ========================================================
              '''.format(saldo = saldo,data = data))
        extrato.append('{data}| | | | Você realizou o deposito de  {deposito_usuario} reais'.format(deposito_usuario = deposito_usuario,data =  data))
        extrato.append(' {data} | | | |Saldo total: {saldo} | | | |'.format(saldo = saldo,data = data))

    elif opcao == 3:
        print('''
              =====================================================
                            FERRAMENTA DE SALDO DBANK
              =====================================================
              ''')
        print('''
              ========================================================
                        Seu saldo atual é de {saldo} reais
                        {data}
              ========================================================
              '''.format(saldo = saldo, data = data))
    elif opcao == 4:
        print('''
              =====================================================
                            FERRAMENTA DE EXTRATO DBANK
              =====================================================
              ''')
        print(extrato)
    else:
        print('Opção Inválida! Tente Novamente')



