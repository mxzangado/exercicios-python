# Cálculo Lucro
print("----Calculando Lucro----")
# Tratando com try:
try:
    produto = float(input("Comprou por: ").replace(',','.'))
    venda = float(input("Vendeu por: ").replace(',','.'))

    lucro = venda - produto
    print(f'Seu produto de {produto:.2f}.R$\nEfetuou Venda {venda:.2f}.R$\nSeu lucro foi de: {lucro:.2f}.R$')
except Exception as e:
    print(f'Apenas números!',e)