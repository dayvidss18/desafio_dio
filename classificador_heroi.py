print('''
========== BEM VINDO AO VERIFICADOR DE RANK!!! ==========
                                    ''')

heroi = input('Qual o nome do seu Herói: ')
xp_heroi = int(input('Quanto de XP tem Seu heroi: '))
nivel = ''
if xp_heroi <= 1000:
    nivel = 'Ferro'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi > 1000 and xp_heroi < 2001:
    nivel = 'Bronze'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi > 2000 and xp_heroi< 5001:
    nivel = 'Prata'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi > 5000 and xp_heroi < 7001:
    nivel = 'Ouro'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi > 7000 and xp_heroi < 8001:
    nivel = 'Platina'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi > 8000 and xp_heroi < 9001:
    nivel = 'Ascendente'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi > 9000 and xp_heroi < 10001:
    nivel = 'Imortal'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
elif xp_heroi >= 10000:
    nivel = 'Radiante'
    print('O herói de nome {nome} e está no nivel de {nivel}! '.format(nome = heroi,nivel = nivel))
else: 
    print('Você não inseriu um comando válido, Verifique seu Xp e Tente novamente!')

