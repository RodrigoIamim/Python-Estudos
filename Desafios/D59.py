n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opc = 0
while opc != 5:
    print("""
[1] somar
[2] multiplicar
[3] maior
[4] inserir novos valores
[5] sair
""")
    opc = int(input('Selecione uma das opções: '))
    if opc > 5:
        print('OPÇÃO INVÁLIDA!')
    if opc == 1:
        res = n1 + n2
        print(f'Resultado: {n1} + {n2} = {res} ')
    if opc == 2:
        res = n1*n2
        print(f'Resultado: {n1} x {n2} = {res} ')
    if opc == 3:
        if n1 > n2:
            print(f'Resultado: {n1} é maior que {n2}  ')
        elif n2 > n1:
            res = n2
            print(f'Resultado: {n2} é maior que {n1}')
        else:
            print('ambos possuem o mesmo valor!')
    if opc == 4:
        n1 = float(input('Novo primeiro valor: '))
        n2 = float(input('Novo segundo valor: '))
    print(':-:'*10)
print('FIM! :)')

    