n1 = float(input('Digite a nota n1: '))
n2 = float(input('Digite a nota n2: '))
m = (n1+n2) / 2
print(f'Média = {m:.1f}')
if m < 5:
    print('REPROVADO!')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')