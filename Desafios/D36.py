sal = float(input('Digite o valor do salário: '))
casa = float(input('Digite o valor da casa: '))
anos = int(input('Digite em quantos anos vai parcelar: '))
prest = (casa/anos) / 12
if prest > (sal * 0.3):
    print(f'parcelas de {prest} excedem o limite de {sal*0.3} (30% do salário).Empréstimo NEGADO!')
else:
    print(f'Parcelas de {prest} estão dentro do limite de {sal*0.3} (30% do salário). Empréstimo ACEITO!')