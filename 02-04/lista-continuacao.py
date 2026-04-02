# Exemplo 20
tabela ={
    "Alface": 2.50,
    "Rúcula": 3.00,
    "Espinafre": 2.80,
    "Tomate": 4.00
}
# deve dar erro
# print["Manga"]

# Exemplo 21
print("Manga" in tabela)
print("Batata" in tabela)

# Exemplo 22

print(tabela.keys())
print(tabela.values())


# Exemplo 23

while True:
    produto = input("Digite o nome do produto (ou 'fim' para sair): ")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço de {produto}: R$ {tabela[produto]:.2f}")
    else:
        print("Produto não encontrado.")

# Exemplo 24

print(tabela)
del tabela["Tomate"]