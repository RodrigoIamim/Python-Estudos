menor = 0
maior = 0
for x in range(1,6):
    peso = float(input(f'Digite o peso da {x}° pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    elif peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
print(f'O maior peso lido foi: {maior}Kg')
print(f'O menor peso lido foi: {menor}Kg')