print('************NOTAS SEMESTRAIS****************')
notaPort=float(input('Português: '))
notaMat=float(input('Matemática: '))
notaGeo=float(input('Geoagráfia: '))
notaCie=float(input('Ciências: '))
notaArt=float(input('Artes: '))
notaHis=float(input('História: '))
notaIng=float(input('Inglês: '))
media = (notaPort+notaMat+notaGeo+notaCie+notaArt+notaHis+notaIng)/7
print('A sua média é {:.1f}'.format(media))
if media >= 7:
    print('Parabéns você foi aprovado!')
elif media <5:
    print('REPROVADO!')
elif 5 <= media <6.9:
    print('Você esta na RECUPERAÇÃO:')