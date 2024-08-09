print('SOMADOR 999')
totn = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número [999 para encerrar]:'))
    totn += 1
    soma += n
print(f'foram inseridos {totn-1} valores e a soma entre eles é {soma-999}')
print('FIM')