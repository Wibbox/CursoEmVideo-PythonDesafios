#Exercício dissecando uma variável

var = input('Digite alguma coisa:\n')
print('O tipo primitivo da variável {} é '.format(var), '-->', type(var))
print('É composto só por espaços? ', var.isspace())
print('É um número? ', var.isnumeric())
print('É alfabético? ', var.isalpha())
print('É alfanumérico? ', var.isalnum())
print('Está em maiúsculas?', var.isupper())
print('Está em minúsculas? ', var.islower())
print('Está capitalizada? ', var.istitle())



