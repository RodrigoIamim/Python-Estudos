from math import hypot
cop = int(input('Comprimento do cateto oposto: '))
cad = int(input('Comprimento do cateto adjacente: '))
hip = hypot(cop, cad)
print(f'A hipotenusa desse triângulo é {hip}')