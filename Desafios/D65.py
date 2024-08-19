print('Maior e menor valores')
resp = 'S'
maior = menor = media = soma = totn = 0
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    totn += 1
    soma += n
    if totn == 1:
        maior = menor = n
    elif totn > 1:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = input('Quer continuar [S/N] ? ').upper().strip()[0]
media = soma/totn
print(f'A média entre TODOS os {totn} valores é {media:.2f}')
print(f'{maior} foi o maior e {menor} foi o menor')
print('fim')