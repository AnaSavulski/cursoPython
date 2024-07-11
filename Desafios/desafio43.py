print('***************************TESTE SEU IMC***********************')
peso = float(input('Qual é o seu peso(kg)? '))
altura = float(input('Qual é a sua altura(m)? '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você ABAIXO do peso normal.')
elif imc <25:
    print('Parabéns! Você esta no peso normal.')
elif imc <30:
    print('Você esta no SOBREPESO.')
else:
    print('Atenção! Você esta na OBESIDADE MÓRBIDA! Procure um médico.')