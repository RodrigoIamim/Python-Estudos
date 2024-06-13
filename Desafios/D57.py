sexo = input('Digite o sexo da pessoa [M/F]: ').upper().strip()[0]
s = ''
while sexo != 'M' and sexo != 'F':
    print('VALOR INVÁLIDO! Digite M ou F')
    sexo = input('Digite o sexo da pessoa [M/F]: ').upper().strip()[0]
    if sexo == 'M':
        s = 'masculino'
    if sexo == 'F':
        s = 'feminino'
print(f'O sexo {s} foi selecionado')
