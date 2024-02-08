
def calcula_vitoria(vitorias,derrotas):
    saldo_vitoria = vitorias - derrotas
    return saldo_vitoria


def guarda_rank(saldo_vitoria):
    rank = ''
    if saldo_vitoria <= 10:
        rank = 'Bronze'
    elif saldo_vitoria > 10 and saldo_vitoria <=20:
        rank = 'Prata'
    elif saldo_vitoria > 10 and saldo_vitoria <= 50:
        rank = 'Ouro'
    elif saldo_vitoria > 50 and saldo_vitoria <= 80:
        rank = 'Platina'
    elif saldo_vitoria > 80 and saldo_vitoria <= 90:
        rank = 'Esmeralda'
    elif saldo_vitoria > 90 and saldo_vitoria <= 100:
        rank = 'Diamante'
    else:
        rank = 'Imortal'
    return rank

entrada_vitoria_player = int(input('Qual a sua quantidade de vitorias essa temporada: '))
entrada_derrota_player = int(input('Qual a sua quantidade de derrotas player: '))
saldo_vitoria = (calcula_vitoria(entrada_vitoria_player,entrada_derrota_player))
rank = guarda_rank(saldo_vitoria)

print('Seu rank atual é {rank} com o total de vitorias é {vitoria}!'.format(rank = rank,vitoria = saldo_vitoria))


