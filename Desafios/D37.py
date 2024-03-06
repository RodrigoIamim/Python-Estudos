n = int(input('Digite um número inteiro qualquer: '))
base = input('Digite [1] para BINÁRIO \nDigite [2] para OCTAL \nDigite [3] para HEXADECIMAL: ')
if base == 1:
    print(f'{n} em BINÁRIO é {bin(n)}')
elif base ==2:
    print(f'{n} em OCTAL é {oct(n)}')
elif base ==3:
    print(f'{n} em HEXADECIMAL é {hex(n)}')
else:
    print('OPÇÃO INVÁLIDA!')