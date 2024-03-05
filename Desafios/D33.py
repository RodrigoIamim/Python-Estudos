n1 = int(input('n1: '))
maior = n1
n2 = int(input('n2: '))
if n2 > n1:
    maior = n2
else:
    menor = n2
n3 = int(input('n3: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print(f'Maior: {maior} \nMenor: {menor}')