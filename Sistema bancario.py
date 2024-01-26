print('''
    ========== BEM VINDO AO SISTEMA BANCARIO DIO ==========
    =======================================================
''')
max_saque = 3
limite_saldo_saque = float(500)
extrato = []

saldo = 1000

print('\n Opções')
print('1. Sacar')
print('2. Depositar')
print('3. Saldo')
print('4. Extrato')

opcao = int(input('O que quer fazer: '))
while True:
    if opcao == 1:
        print('''Ferramenta De Saque Dio''')
        saque_usuario = int(input('Quanto deseja Sacar: '))
        saldo = saldo - saque_usuario
        print('Você realizou o saque de {saque_usuario} reais'.format(saque_usuario = saque_usuario))
        print('Seu limite agora é de {saldo} reais'.format(saldo = saldo))
        extrato.append('''Você realizou o saque de {saque_usuario} reais,
                    Saldo total: {saldo} Reais'''.format(saque_usuario = saque_usuario, saldo = saldo))
    elif opcao == 2:
        print('''FERRAMENTA DE DEPOSITO DIO''')
        deposito_usuario = int(input('Quanto Deseja Depositar: '))
        saldo = saldo + deposito_usuario
        print('Você realizou o deposito de {deposito_usuario} reais'.format(deposito_usuario = deposito_usuario))
        print('Seu saldo atual é de {saldo} reais'.format(saldo = saldo))
    elif opcao == 3:
        print('''FERRAMENTA DE SALDO DIO''')
        print('Seu saldo atual é de {saldo} reais'.format(saldo = saldo))
    elif opcao == 4:
        print('''FERRAMENTA DE EXTRATO DIO''')
        print(extrato)
    else:
        print('0')



