from datetime import date
nasc = int(input('Digite o ANO em que nasceu: '))
idade = date.today().year - nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL') 
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')