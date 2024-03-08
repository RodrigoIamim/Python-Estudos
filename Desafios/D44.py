print(f'{' LOJAS TICARACATICAS ':=^50}')
preco = float(input('Digite o preço do produto: R$'))
print('''OPCÕES DE PAGAMENTO:
[1] - à vista dinheiro/cheque (10% de desconto)
[2] - à vista no cartão (5% de desconto) 
[3] - em 2x no cartão (preço normal) 
[4] - 3x ou mais no cartão (20% de juros)''')
opc = input('\nDigite a opção de pagamento:')
if opc == '1':
    pf = preco*0.9
    print(f'Com 10% de desconto o produto de R${preco:.2f} fica por R${pf:.2f}')
elif opc == '2':
    pf = preco*0.95
    print(f'Com desconto de 5%, o produto de R${preco:.2f} fica por R${pf:.2f}')
elif opc == '3':
    print(f'Preço normal do produto é R${preco:.2f}. Parcelado em 2x fica R${preco/2:.2f} por mês')
elif opc == '4':
    pf = preco*1.2
    print(f'Com acréscimo de 20% de juros sobre o preço de R${preco:.2f} o produto custará R${pf:.2f}')
    parcelas = int(input('parcelar em quantas vezes (de 3 até 12)? '))
    if 3 <= parcelas <= 12:
        print(f'Parcelando em {parcelas}x o produto de R${pf:.2f}, cada parcela mensal será de R${pf/parcelas:.2f}')
    else:
        print('Opção de parcelamento inválida. Tente novamente! (deve ser entre 3 e 12)')
else: 
    print('OPÇÃO INVÁLIDA! tente novamente')
