
saldo = 0
limite = 500
extrato = ''
numero_saques = 3

print('''
============ BANCO CENTRAL ============
      1. DEPOSITO
      2. SAQUE
      3. EXTRATO
     
========================================
''')
opcao = int(input('O que deseja: '))

if opcao == 1:
    deposito = float(input('O valor depositado é de: '))
    saldo = saldo + deposito
    print('deposito de ', deposito,' reais concluído com sucesso')
elif opcao == 2:
    x = 3
    while x < 3: 
        if numero_saques <= 3:
            retirada = float(input('Quanto deseja retirar: '))
            saldo = saldo - retirada
            print('Saque de ',retirada,'reais concluído com sucesso')
        else:
            print('Você não pode mais fazer retiradas hoje, tente novamente amanhã')
    x+=1
elif opcao == 3:
    print(extrato)
