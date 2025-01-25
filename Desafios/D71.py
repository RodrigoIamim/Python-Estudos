print('-=-'*10, end=' ')
print(' CEVBANK ', end=' ')
print('-=-'*10)
valor = int(input('Digite o valor a ser sacado (SOMENTE OS NÚMEROS): R$'))
print(f'{valor} em notas de 50, 20, 10 e 1')
while True:
    c50 = valor//50
    valor-=50
    if valor//50==0:
        break
print(f'{c50} notas de 50 para {valor}')