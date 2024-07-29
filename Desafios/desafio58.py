from random import randint
computador = randint(0,10)

print('''Olá! Sou o seu computador...
Vamos jogar? 
Acabei de pensar num número entre 0 e 10.
Será que você advinha qual foi? 
''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou! Você precisou de {} palpites para acertar!'.format(palpites))