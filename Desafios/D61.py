from time import sleep
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print(f'Calculando os 10 primeiros termos da PA partindo do número {n1} com razão {r}... ')
c = 1
pt = n1
sleep(1)
while c < 11:
    c+=1
    print(f' {pt} -> ', end='')
    pt += r
print('FIM!')    