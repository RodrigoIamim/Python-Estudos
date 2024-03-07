a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))
if a < b+c and b < a + c and c < b + c:
    if a == b and a == c:
        print(f'lados {a} {b} {c} formam triângulo EQUILÁTERO')
    elif a == b or b == c and a != c:
        print(f'lado {a} {b} {c} formam triângulo ISÓSCELES')
    elif a != b and a!=c and b != c:
        print(f'lados {a} {b} {c} formam triângulo ESCALENO')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO COM ESSAS MEDIDAS')