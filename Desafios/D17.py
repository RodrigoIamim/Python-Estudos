from math import hypot
cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cop, cad)
print(f'A hipotenusa desse triângulo é {hip:.2f}')