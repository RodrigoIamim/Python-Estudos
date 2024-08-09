print('Maior e menor valores')
resp = 'S'
maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    resp = input('Quer continuar [S/N] ? ').upper().strip()[0]
print('fim')