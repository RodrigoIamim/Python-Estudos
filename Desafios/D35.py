a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))
if a > b + c:
    print('NÃO FORMA TRIÂNGULO')
if b > a + c:
    print('NÃO FORMA TRIÂNGULO')
if c > a + b:
    print('NÃO FORMA TRIÂNGULO')
else:
    print('FORMA TRIÂNGULO!')