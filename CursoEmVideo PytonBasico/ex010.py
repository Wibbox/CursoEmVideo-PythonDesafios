#Converte para dolar

tx = float(input('Taxa do Dolar: '))
qtd = float(input('Quanto em reais deseja converter? '))
t = qtd/tx

print('Com R$ {:.2f}, você consegue comprar $ {:.2f}'.format(qtd, t))
