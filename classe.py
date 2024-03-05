class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        ataque = ''
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou ataque indefinido'
        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")


# Função para ler entrada do usuário e criar instância do herói
def criar_heroi():
    nome = input('Digite o nome do herói: ')
    idade = int(input('Digite a idade do herói: '))
    tipo = input('Digite o tipo do herói (mago, guerreiro, monge, ninja): ')
    return Hero(nome, idade, tipo)


# Exemplo de uso
heroi = criar_heroi()
heroi.atacar()
