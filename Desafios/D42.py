a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))
if a < b + c and b < a + c and c < a + b:
    print('Podem formar um triângulo ', end='')
    if a == b == c:
        print(f'EQUILÁTERO')    
    elif a != b != c != a:
        print(f'ESCALENO')
    else:
        print(f'ISÓSCELES')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO COM ESSAS MEDIDAS')