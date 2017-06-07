# Motra dobro, triplo e raiz quadrada

import math

n = int(input('Entre com um inteiro para receber o dobro, triplo e raiz quadrada: \n'))

dob = pow(n, 2)
tri = pow(n, 3)
r = math.sqrt(n)

print(' Dobro: {}\n Triplo: {}\n Raiz Quadrada: {:.2f} '.format(dob, tri, r))
