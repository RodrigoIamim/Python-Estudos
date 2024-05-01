from datetime import date
atual = date.today().year
idade = 0
menor = 0
maior = 0
for x in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {x}° pessoa?'))
    idade = atual - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Entre essas 7 pessoas, existe(m) {menor} pessoa(s) menor(es) de idade e {maior} maior(es) de idade!')
