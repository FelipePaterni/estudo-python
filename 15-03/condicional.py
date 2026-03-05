def separador(value):
    print("\n====================================================================")
    print(f"                            {value}                                        ")
    print("====================================================================\n")


separador("Exemplo 1")

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))

if a > b:
    print("O primeiro numero é maior")
elif b > a:
    print("O segundo numero é maior")
else:
    print("Os numeros são iguais")


separador("Exemplo 2")

idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")


separador("Exemplo 3")


minutos = int(input("quantos minutos você utilizou este mês: "))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
        print(f"Voce vai pagar este mes: R${minutos * preco:.2f}")


separador("Exemplo 4")

categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    preco = 0

print(f"O preço do produto é: R${preco:.2f}")

separador("Exemplo 5")
