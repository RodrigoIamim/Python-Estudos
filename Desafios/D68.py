import random
from time import sleep
print('-=-'*10)
print('        PAR OU ÍMPAR')
print('-=-'*10)
while True:
    poi = str(input('Par ou impar? ')).strip().lower()
    eu = int(input('[FAÇA SUA JOGADA] '))
    randn = random.randint(1, 10)
    print('Ok, vamos lá!')
    sleep(0.3)
    print('1...')
    sleep(1)
    print('2...')
    sleep(1)
    print('3...')
    sleep(1)
    res = eu+randn
    print(f'{randn} com {eu} dá {res}')
    if res%2==0:
        if poi == 'par':
            print('Você ganhou! ')
        elif poi == 'impar':
            break
    elif res%2!=0:
        if poi == 'impar':
            print('Você ganhou! ')
        elif poi == 'par':
            break
print('Você perdeu hahahaha')