from random import randint
r = randint(0, 5)
n = int(input('Adivinhe o número: '))
if r == n:
    print('ACERTOU!')
else:
    print(f'ERROU! resposta: {r}')
print('Obrigado por jogar!')