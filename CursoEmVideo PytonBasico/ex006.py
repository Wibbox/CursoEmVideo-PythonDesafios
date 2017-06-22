# Motra dobro, triplo e raiz quadrada

import math

n = int(input('Entre com um inteiro para receber o dobro, triplo e raiz quadrada: \n'))

dob = n * 2
tri = n * 3
r = math.sqrt(n)

print(' Dobro: {}\n Triplo: {}\n Raiz Quadrada: {:.2f} '.format(dob, tri, r))
