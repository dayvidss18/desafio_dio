from datetime import datetime
print('''
    ========== BEM VINDO AO SISTEMA BANCARIO DIO ==========
    =======================================================''')
max_saque = 0
limite_saldo_saque = 500
extrato = []

saldo = 1000

menu = '''
Opções
[1] Sacar
[2] Depositar
[3] Saldo  
[4] Extrato    
            
=> '''


while True:
    opcao = int(input(menu))
    if opcao == 1:
        while max_saque < 3 and opcao_sair == 'S':
                print('''Ferramenta De Saque Dio''')
                saque_usuario = int(input('Quanto deseja Sacar: '))
                if saque_usuario < saldo:
                    saldo = saldo - saque_usuario
                    print('''
                    ======================================================
                            Você realizou o saque de {saque_usuario} reais
                    ======================================================
                    '''.format(saque_usuario = saque_usuario))
                    print('''
                    ======================================================
                            Seu limite agora é de {saldo} reais
                    ======================================================
                    '''.format(saldo = saldo))
                    extrato.append('Você realizou o saque de {saque_usuario} reais'.format(saque_usuario = saque_usuario, saldo = saldo))
                    extrato.append('Saldo total: {saldo} Reais'.format(saldo = saldo))
                else:
                    print('Você não tem saldo suficiente!')
                opcao_sair = input('Deseja Continuar no Saque S/N')
                max_saque = max_saque + 1

        
    elif opcao == 2:
        print('''FERRAMENTA DE DEPOSITO DIO''')
        deposito_usuario = int(input('Quanto Deseja Depositar: '))
        saldo = saldo + deposito_usuario
        print('''
              ========================================================
                Você realizou o deposito de {deposito_usuario} reais
              ========================================================
              '''.format(deposito_usuario = deposito_usuario))
        print('''
              ========================================================
                        Seu saldo atual é de {saldo} reais
              ========================================================
              '''.format(saldo = saldo))
        extrato.append('Você realizou o deposito de  {deposito_usuario} reais'.format(deposito_usuario = deposito_usuario))
        extrato.append('Saldo total: {saldo}'.format(saldo = saldo))

    elif opcao == 3:
        print('''FERRAMENTA DE SALDO DIO''')
        print('''
              ========================================================
                        Seu saldo atual é de {saldo} reais
              ========================================================
              '''.format(saldo = saldo))
    elif opcao == 4:
        print('''FERRAMENTA DE EXTRATO DIO''')
        print(extrato)
    else:
        print('Opção Inválida! Tente Novamente')



