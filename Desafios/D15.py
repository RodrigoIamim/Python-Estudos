dias = int(input('Por quantos dias utilizou o carro? '))
km = float(input('Quantos km rodou no total? '))
valor = km*0.15 + 60*dias
print(f'Após percorrer {km}km em {dias} dias, o valor do aluguel é R${valor:.2f}')