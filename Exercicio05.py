# Rateio
# Recebe o número de apartamentos
apt = int(input('Quantidade de apartamentos: '))
# Recebe o valor da água
agua = float(input('Valor água: '))
# Recebe valor da luz
luz = float(input('Valor valor luz: '))
# Resolução a variável soma recebe valor de agua + luz
soma = agua + luz
# Total pega a soma e divide pela quantdade de apartamento
total = soma/apt
# Resultado
print(f'O rateio para {apt} apartamentos foi R$ {soma:.2f}\nCada apartamento vai pagar R$ {total}')