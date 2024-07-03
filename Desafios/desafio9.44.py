print('Minha Loja')
produto = float(input('Valor do produto R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/pix
[2] à vista no cartão crédito
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    total = produto - (produto *10 / 100)
elif opcao == 2:
    total = produto - (produto * 5 / 100)
elif opcao == 3:
    total = produto
    parcela = total /2
    print('Sua compra será parcelada em 2x de R${:.2f}, SEM JUROS!'.format(parcela))
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {:.2f} de R${:.2f}, com juros.'.format(totalparcela,parcela))
else:
    print('ERRO! Opção inválida, tente novamente.')
print('Sua compra de R${:.2f} teve um desconto, e vai custar R${:.2f} no final'.format(produto,total))