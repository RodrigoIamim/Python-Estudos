from datetime import date
nasc = int(input('Digite o ANO em que nasceu: '))
if date().year - nasc <= 9:
    print('MIRIM')
elif date().year - nasc > 9 and date().year - nasc <= 14:
    print('INFANTIL') 
elif date().year - nasc > 14 and date().year - nasc <= 19:
    print('JUNIOR')
elif date().year - nasc > 19 and date().year - nasc <= 20:
    print('SENIOR')
else:
    print('MASTER')