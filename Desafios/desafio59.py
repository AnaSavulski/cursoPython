n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]sair do programa
    ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        Somar = n1+n2
        print('A soma entre {}+{} = {}'.format(n1,n2,Somar))
    elif opcao ==2:
        Multiplicar = n1*n2
        print('A multiplicação entre {}x{} = {}'.format(n1,n2,Multiplicar))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1,n2))
        else:
            print('O número {} é maior que {}'.format(n2,n1))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro: '))
        n2 = int(input('Segundo: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-='*10)

print('Fim do programa! Volte sempre!')