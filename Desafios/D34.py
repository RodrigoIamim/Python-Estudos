sal = float(input('Digite o valor do salário: R$'))
if sal > 1250:
    aum = sal*1.1
    print(f'Com aumento de 10% fica R${aum:.2f}')
else:
    aum = sal*1.15
    print(f'Com aumento de 15% fica R${aum:.2f}')