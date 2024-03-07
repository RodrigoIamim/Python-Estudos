n = int(input('Digite um número inteiro qualquer: '))
print('Digite [1] para BINÁRIO \nDigite [2] para OCTAL \nDigite [3] para HEXADECIMAL: ')
base =int(input('BASE ESCOLHIDA: '))
if base == 1:
    print(f'{n} em BINÁRIO é {bin(n)[2:]}')
elif base == 2:
    print(f'{n} em OCTAL é {oct(n)[2:]}')
elif base == 3:
    print(f'{n} em HEXADECIMAL é {hex(n)[2:]}')
else:
    print('OPÇÃO INVÁLIDA!')