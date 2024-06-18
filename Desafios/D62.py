print('PA V3')
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n1
c = 1
print(f'Calculando PA partindo de {n1} com razão {r}...')

while c <= 10:
    print(f' {termo} -> ', end='')
    termo += r
    c += 1
print('PAUSA!')
escolha = input('Ver mais termos dessa mesma PA? [S/N] ').strip().upper()

