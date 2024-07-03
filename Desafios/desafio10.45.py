from random import randint
print('******************PEDRA, PAPEL E TESOURA*************')
itens =('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*15)
print('O computador jogou {} e você jogou {}'.format(computador, jogador))
print('-='*15)
if computador == 0:#pedra
    if jogador ==0:
        print('Empate!')
    elif jogador ==1:
        print('Você ganhou!')
    elif jogador ==2:
        print('Computador ganhou!')
    else:
        print('Inválido!')
elif computador ==1:  #Papel
    if jogador ==0:
        print('Computador ganhou')
    elif jogador ==1:
        print('Empate!')
    elif jogador ==2:
        print('Você ganhou!')
    else:
        print('Inválido!')
elif computador == 2: #Tesoura
    if jogador ==0:
        print('Você ganhou!')
    elif jogador ==1:
        print('Computador ganhou!')
    elif jogador ==2:
        print('Empate!')
    else:
        print('Inválido!')