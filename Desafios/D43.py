peso = float(input('Qual é o seu peso em quilos? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura**2)
print(f'IMC = {imc:.1f}')
if imc < 17:
    print('Muito abaixo do peso ideal')
elif imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Acima do peso')
elif 30 <= imc < 35:
    print('Obesidade grau 1')
elif 35 <= imc < 40:
    print('Obesidade grau 2')
else:
    print('Obesidade mórbida')