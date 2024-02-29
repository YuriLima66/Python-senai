times = list(('Palmeiras', 'Santos'))

print(times)

marcas = ['Ford',
          'Fiat',
          'Ferrari',
          'McLaren']

for pos, valor in enumerate(marcas):
    print(f' O {pos}º item da sua lista é {valor}')
    
    print('\n')
    marcas[0] = 'Bugatti'
    
for pos, valor in enumerate(marcas):
        print(f'O {pos}º item da sua lista é {valor}')
        print('\n')
        adicionar = str (input('Adicione uma nova marca:'))
        marcas.append(adicionar)
        
for pos, valor in enumerate(marcas):
    print(f'O {pos}º item da sua lista é valor{valor}')
        
        
print('\n')
marcas.insert(1, 'Tesla')

for pos, valor in enumerate(marcas):
    print(f'O {pos}º item da sua lista é {valor}')
    
print('\n')
