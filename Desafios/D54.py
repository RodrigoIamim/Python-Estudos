from datetime import date
atual = date.today().year
idade = 0
for x in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {x}° pessoa?'))
    idade = atual - nasc
    print(f'{x}° tem {idade} anos')
