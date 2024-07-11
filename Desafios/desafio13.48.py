# Faça um programa que calcule a soma entre todos os números que são multiplos de três  e que se encontram no intervalo de 1 a 500.
soma =0
cont =0
for c in range(1,501,2):
    if c % 3 ==0:
        cont = cont + 1
        soma = soma + c
        #print(c, end=' ')
print("A soma de todos os {} valores solicitado é: {}".format(cont, soma))
