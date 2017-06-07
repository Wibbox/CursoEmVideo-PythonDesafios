print('...Calcula quantidade de tinta necessária...')
l = float(input('Largura da Parede: '))
h = float(input('Altura da Parede: '))
m2 = l*h
tint = 1*(m2/2)

print('Para pintar {}m² você precisa de {} litro(s) de tinta.'.format(m2, tint))
