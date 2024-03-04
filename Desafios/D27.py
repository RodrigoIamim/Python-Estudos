nome = input('Digite seu nome completo: ').title()
sep = nome.split()
primeiro = sep[0]
ultimo = sep[-1]
print(f'Primeiro nome: {primeiro} \nÚltimo nome: {ultimo}')