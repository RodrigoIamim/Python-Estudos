while True:
    print('-=-'*13)
    x = int(input('Deseja ver a tabuada de que número? '))
    if x<0:
        break
    y = 1
    for y in range(1,11):
        print(f'{x} x {y} = {x*y}')
        y += 1
print('fim')    
