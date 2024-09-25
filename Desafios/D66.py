n = s = t = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    t+=1
    s+=n
print(f'a soma entre os {t} números digitados é {s}')