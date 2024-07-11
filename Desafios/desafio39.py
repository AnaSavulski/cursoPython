from datetime import date
print('****************ALISTAMENTO MILITAR*****************')
nascimento=int(input('Digite o ano do seu nascimento: '))
now = date.today()
anoAtual = now.year
idade= anoAtual -nascimento

if idade == 18:
    print('Parabéns você já tem 18 anos! Já esta na hora de se alistar!')
elif idade < 18:
    diferenca = 18 -idade
    ano= anoAtual + diferenca
    print('Olá, você ainda tem {} anos de idade,'
          ' e faltam {} anos para poder se alistar. Seu alistamento será no ano {}.'.format(idade,diferenca,ano))
elif idade > 18:
    sobra = idade - 18
    passou= nascimento +18
    print('Oi, sua idade é {} anos, você já deveria ter se alistado há {} anos. Seu alistamento foi em {}.'.format(idade,sobra,passou))
#corrigido e correto