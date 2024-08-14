nome = 'Iago'
altura = 1.75
peso = 80
imc = (peso / (altura ** 2))
# f-strings permite formatar uma string para colocar variaveis usando {} em torno delas
# e :.xf para especificar o numero de casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é: {imc:.2f}'
print(linha_1)