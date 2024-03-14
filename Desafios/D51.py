prim = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = prim + (10-1) * r
for c in range(prim, n+r, r):
    print(f'{c} ', end='-> ')
print('FIM')