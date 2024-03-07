import datetime
nasc = int(input('Informe o ANO em que nasceu: '))
atual = datetime.date.today().year
idade = atual - nasc
if idade < 18:
    print(f'Você ainda vai se alistar daqui a {18 - idade}anos no ano de {nasc+18}')
elif idade == 18:
    print('Chegou a sua hora!')
else:
    print(f'Já possui {idade} anos. Seu ano de alistamento foi em {nasc+18}')