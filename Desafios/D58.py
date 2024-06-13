from random import randint
computador = randint(0, 10)
print('Pensei num número entre 0 e 10, tente advinhar qual é! ')
jogador = int(input('Palpite: '))
palpites = 1   
while jogador != computador:
    if jogador > computador:
        jogador = int(input('errou, é menor: '))
    if jogador < computador:
        jogador = int(input('errou, é maior: '))
    palpites += 1
print(f'Parabéns, você acertou! Eu realmente pensei no número {computador} e após {palpites} palpite(s) você adivinhou corretamente!')
