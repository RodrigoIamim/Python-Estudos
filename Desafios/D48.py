soma = 0
qtd = 0
for c in range(1, 501):
    if c%2==1 and c%3==0:
        soma += c
        qtd += 1
print(f'A soma dos {qtd} números encontados é {soma}')        
print('fim')