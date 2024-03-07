sal = float(input('Digite o valor do salário: R$'))
casa = float(input('Digite o valor da casa: R$ '))
anos = int(input('Digite em quantos anos vai parcelar: '))
prest = (casa/anos) / 12
if prest > (sal * 0.3):
    print(f'parcelas de R${prest:.2f} excedem o limite de R${sal*0.3:.2f} (30% do salário).Empréstimo NEGADO!')
else:
    print(f'Parcelas de R${prest:.2f} estão dentro do limite de R${sal*0.3:.2f} (30% do salário). Empréstimo ACEITO!')