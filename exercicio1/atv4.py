"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

nome_produto = "Cadeira Infantil"
Preco = 12.40
quantidade = 3

preco_total = Preco * quantidade
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {Preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")