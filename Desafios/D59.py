n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = '0'
while opc != '5':
    print("""
[1] somar
[2] multiplicar
[3] maior
[4] inserir novos valores
[5] sair
""")
    opc = str(input('---> Selecione uma das opções: '))
    if opc == '1':
        res = n1 + n2
        print(f'Resultado: {n1} + {n2} = {res} ')
    elif opc == '2':
        res = n1*n2
        print(f'Resultado: {n1} x {n2} = {res} ')
    elif opc == '3':
        if n1 > n2:
            print(f'Resultado: {n1} é maior que {n2}  ')
        elif n2 > n1:
            res = n2
            print(f'Resultado: {n2} é maior que {n1}')
        else:
            print('ambos possuem o mesmo valor!')
    elif opc == '4':
        n1 = int(input('Novo primeiro valor: '))
        n2 = int(input('Novo segundo valor: '))
    elif opc == '5':
        print('Encerrando...')
    else:
        print('VALOR INVÁLIDO!')
print('FIM! :)')

    