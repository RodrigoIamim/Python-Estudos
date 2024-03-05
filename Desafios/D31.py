km = float(input('Distância da viagem (km): '))
if km <= 200:
    custo = 0.5*km
    print(f'Custo da viagem R${custo:.2f}')
else:
    print(f'Custo da viagem R${0.45*km:.2f}')
print('Boa viagem!')
