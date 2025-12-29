produto = "Arroz"
preco_unitario = 5.78
quantidade = 3

# calculo do valor total
valor_total = preco_unitario * quantidade

# aplicar desconto de 10% se a quantidade for maior que 2
if quantidade >2:
    # valor_total = valor_total * 0.9
    # depurando o erro - e se eu colocar 0.8 no desconto
    valor_total = valor_total * 0.8

print("Produto:", produto)
print("Quantidade comprada:", quantidade)
print(f"Valor total da compra: R${valor_total:.2f}")