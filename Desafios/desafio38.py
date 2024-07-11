num1=int(input('Digite um número inteiro: '))
num2=int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro número {}, é maior que {}'.format(num1,num2))
elif num1 < num2:
    print('O segundo número {}, é maior que o primeiro {}.'.format(num2,num1))
elif num1 == num2:
    print('Não existe valor maior, os dois números são iguais.')
#corrigido e correto