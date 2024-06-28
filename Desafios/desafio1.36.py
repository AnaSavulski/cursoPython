#Minha versão
print('Simulador de empréstimo:')
casa=float(input('Valor da casa: '))
renda= float(input('Qual o valor total da sua renda: '))
parcelas=int(input('Quantas parcelas: '))
valordaprestacao=casa/parcelas
percentualsalario=(renda*30)/100
print(f'Após calcular o valor da casa R${casa:.2f} dividido em {parcelas}x,'
      f'a prestação da casa será no valor de R${valordaprestacao:.2f} reais por mês.')
if valordaprestacao <= percentualsalario:
    print('Parabéns, seu empréstimo foi aprovado!')

else:
    print('Infelizmente seu empréstimo foi negado.')
#Corrigido e correto.