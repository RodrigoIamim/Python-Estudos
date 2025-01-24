print('-=-'*10, end='')
print(' LOJAS TICARACATICAS ', end='')
print('-=-'*10)
total = min = totmil = max = 0
c = 1
while True:
    produto = str(input('Produto: ')).strip().upper()
    valor = float(input('Valor: R$'))
    total += valor
    if valor > 1000:
        totmil += 1
    if c == 1:
        min = max = valor
        maisbarato = produto
    else:
        if valor > max:
            max = valor
        if valor < min:
            min = valor
            maisbarato = produto
    c += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar comprando? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break    
print('-=-'*10, end = '')
print(' RESULTADO ', end=' ')
print('-=-'*10)
print(f'Mínimo: R${min}, {maisbarato}')
print(f'Máximo: R${max}')
print(f'Acima de mil: {totmil}')
print(f'Total: R${total}')