'''from math import factorial
print('FATORIAL 1')
n = int(input('Insira um número inteiro: '))
fat = factorial(n)
print(f'O fatorial de {n} é {fat}')'''

print('FATORIAL 2')
n = int(input('Insira um número inteiro: '))
c = n
fat = 1
print(f'{n}!... ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(f'FIM! o resultado de {n}! é {fat}')



