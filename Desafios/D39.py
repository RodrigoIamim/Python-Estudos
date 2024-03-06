import datetime
nasc = int(input('Informe o ANO em que nasceu: '))
if datetime.date().year - nasc < 18:
    print('Você ainda vai se alistar')
elif datetime.date().year - nasc == 18:
    print('Chegou a sua hora!')
else:
    print('Já possui mais de 18 anos. Já passou da hora')