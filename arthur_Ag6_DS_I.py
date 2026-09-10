produto = float(input("digite o valor do produto: "))
if produto < 200:
    desconto = 5.00
if produto >= 200 and produto < 300:
    desconto = 10.00
if produto >= 300:
    desconto = 15.00
valor_desconto = produto * (desconto / 100)
valor_final = valor_desconto - produto
print(f"O valor do produto é: {produto:.2f}")
print(f"O valor do desconto é {desconto:.2f}")
print(f"O valor do produto será: {valor_final:.2f}") 

