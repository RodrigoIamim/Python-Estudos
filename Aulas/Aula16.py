lanches = ('Ambugue', 'garana', 'partel', 'requejaum')
# tuplas são IMUTAAAAAAAVEIS
print(len(lanches))
print(lanches[1])
print(lanches[0:3])
print(lanches[-4:-1])
print(lanches[1:])
print(lanches[:2])
for c in lanches:
    print(f'vo pidi um {c} no ifood pprt cria')
print('arrotei')

for c in range (0, len(lanches)):
    print(f'vo pidi um {lanches[c]} no ifood pprt cria')
print('to co fome dinovo')

for pos, c in enumerate(lanches):
    print(f'vo pidi um {c} #{pos} no ifood pprt cria')
