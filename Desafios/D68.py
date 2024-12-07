import random
print('-=-'*10)
print('        PAR OU ÍMPAR')
print('-=-'*10)
while True:
    poi = str(input('Par ou impar? ')).strip().lower()
    eu = int(input('Qual é a sua jogada? '))
    randn = random.randint(1, 10)
    res = eu+randn
    print(f'{randn} ~~ {res}')
    if res%2==0:
        if poi == 'par':
            print('Você ganhou! ')
        elif poi == 'impar':
            break
print('Você perdeu hahahaha')