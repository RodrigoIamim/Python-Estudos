print('-=-'*10, end='')
print(' LOJAS TICARACATICAS ', end='')
print('-=-'*10)
total = min = max = totmil = 0
while True:
    produto = str(input('Produto: ')).strip().upper()
    valor = float(input('Valor: '))
    min = max = valor
    total += valor
    if valor > 1000:
        totmil += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar comprando? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break    
print(f'minimo {min}')
print(f'maximo {max}')
print(f'acima de mil {totmil}')
print(f'total {total}')