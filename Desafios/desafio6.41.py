from datetime import date
print('******************CONFEDERAÇÃO NACIONAL DE NATAÇÃO******************')
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade= atual - nascimento
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria atual: MIRIM')
elif idade <=14:
    print('Categoria atual: Infantil')
elif idade <=19:
    print('Categoria atual: JÚNIOR')
elif idade <=25:
    print('Categoria atual: SÊNIOR')
else:
    print('Categoria atual: MASTER')
