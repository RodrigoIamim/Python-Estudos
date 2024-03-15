n = int(input('Digite um número inteiro: '))
primos = 0
for c in range(1, n+1):
    if n%c==0:
        print(f'({c})', end=' -> ')
        primos += 1
    else:
        print(f'{c}', end=' -> ')
print('FIM!')
print(f'{n} é divisível por {primos} número(s).')
if primos == 2: 
    print(f'{n} é primo!')
else: 
    print(f'{n} não é primo!')