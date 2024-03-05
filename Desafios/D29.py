vel = float(input('Velocidade do carro (km/h): '))
if vel > 80:
    print(f'MULTADO! R${(7*(vel-80)):.2f} de multa por excesso')
else:
    print('Velocidade aceitável!')
print('Se beber, não dirija!')