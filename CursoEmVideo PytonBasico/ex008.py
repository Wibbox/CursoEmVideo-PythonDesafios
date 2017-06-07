# Conversor para cm e mm

print('===Este programa converte Metros em CM e MM===')
m = float(input('Quantos metros deseja converter? '))
cm = m*100
mm = m*1000

print('{:.0f} Metros é equivalente em:\nCentímetros: {:.0f}\nMilímetros: {:.0f}'.format(m, cm, mm))
