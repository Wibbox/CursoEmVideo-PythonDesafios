#Taboada

print('Calcula Taboada')
n = int(input('Número para cálculo: '))
t = 0
while t <= 10:
    i = n * t
    print("{} x {} = {}".format(n, t, i))
    t += 1
