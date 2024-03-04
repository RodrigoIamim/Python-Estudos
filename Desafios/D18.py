from math import sin, cos, tan, radians
ang = float(input('Valor do ângulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print(f' sen {ang}°= {s:.2f}\n cos {ang}° = {c:.2f}\n tan {ang}° = {t:.2f}')