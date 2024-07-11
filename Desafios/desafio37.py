print('Olá, digite um número inteiro edepois escolha a base de conversão que desejar:')
num =int(input('Digite um número: '))
print("1: para binário\n2: para octal \n3: para hexadecimal")
conversao = int(input('Qual a sua escolha: '))
if conversao == 1:
    print('O número digitado foi {}, convertido para binário se escreve assim:'.format(num))
    print(bin(num))
elif conversao ==2:
    print('O número digitado foi {}, convertido para octal se escreve assim:'.format(num))
    print(oct(num))
elif conversao ==3:
    print('O número digitado foi {}, convertido para hexadecimal se escreve assim:'.format(num))
    print(hex(num))
else:
    print('Opção inválida!')
#Corrigido e correto.