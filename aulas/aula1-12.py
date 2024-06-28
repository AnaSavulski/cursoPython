nome = str(input('Qual é o seu nome?'))
if nome == "Henrique":
    print('Que nome bonito!')
elif nome=='Gabriel' or nome=='Miguel' or nome=='Enzo':
    print('Seu nome é bem popular no Brasil.')
elif nome in ('Ana Lúcia Júlia Paula'):
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))