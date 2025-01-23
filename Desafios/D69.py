tot18 = totH = totM20 = total = 0
while True:
    print('-=-'*10)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade < 20 and sexo == 'M':
        totM20 += 1
    total += 1
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == "N":
        break
print(f'Foram registradas {total} pessoas')
print(f'{totH} são homens')
print(f'{tot18} são maiores de idade')
print(f'{totM20} são mulheres menores de 20 anos')