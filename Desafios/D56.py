soma = 0
media = 0
maiorvalor = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('-'*20)
    print(f'{c}° PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maiorvalor = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorvalor:
        maiorvalor = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = soma / 4
print(f'Idade média do grupo: {media} anos')
print(f'O homem mais velho é {nomevelho} e tem {maiorvalor} anos de idade')
print(f'No total, há {totmulher20} mulheres com idades abaixo de 20 anos')