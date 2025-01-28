print('-=-'*10, end=' ')
print(' CEVBANK ', end=' ')
print('-=-'*10)
valor = int(input('Digite o valor a ser sacado (SOMENTE OS NÚMEROS): R$'))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
        
    else:
        if totced > 0:
            print(f'Total de cédulas de {cedula}: {totced}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
print('fim')        