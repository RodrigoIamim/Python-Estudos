from random import randint
from time import sleep
print(f'{' JOKENPO ':=^40}')
print('''SUAS OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
jogador = int(input('FAÇA A SUA JOGADA: '))
if jogador < 0 or jogador > 2:
    print('OPÇÃO INVÁLIDA') 
else: 
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)
    print('~' * 20)
    print(f'COMPUTADOR: {itens[computador]}')
    print(f'JOGADOR: {itens[jogador]}')
    
    if jogador == 0:
        if computador == 0:
            print('EMPATE!')
        elif computador == 1:
            print('COMPUTADOR VENCEU!')
        elif computador == 2:
            print('JOGADOR VENCEU!')
    elif jogador == 1:  
        if computador == 0:
            print('JOGADOR VENCEU!')
        elif computador == 1:
            print('EMPATE!') 
        elif computador == 2:
            print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        if computador == 0:
            print('COMPUTADOR VENCEU!')
        elif computador == 1:
            print('JOGADOR VENCEU!')
        elif computador == 2:
            print('EMPATE!')
    print('~' * 20)