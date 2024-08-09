print('PA V3')
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n1
c = 1
print(f'Calculando PA partindo de {n1} com razão {r}...')
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f' {termo} -> ', end='')
        termo += r
        c += 1
    print('PAUSA!')
    mais = int(input('Quer ver mais quantos termos? [0 para encerrar] '))
print(f'{total} termos foram exibidos!')
print('FIM!')
