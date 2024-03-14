num = int(input('Digite um número: '))
print(f' TABUADA DE {num} ')
for c in range(1,11):
    print(f'{c:2}  x {num:2} = {c*num:2}')
print('fim')