# Criando uma função para cálculo

def calcular_lucro():
    try:
        produto = float(input("Comprou por: ").replace(",","."))
        venda = float(input("Vendeu por: ").replace(",","."))

        lucro = venda - produto

        print(f"Produto:{produto:.2f}")
        print(f"Venda:{venda:.2f}")
        print(f"Lucro:{lucro:.2f}")
    except Exception as e:
        print(f"Apenas números", e)
calcular_lucro()