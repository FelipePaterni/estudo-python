import subprocess


def clear():
    """
    Limpa a tela
    """
    subprocess.run("cls", shell=True)


clear()
# Exemplo 1
predio = [
    "terreo",
    "primeiro andar",
    "segundo andar",
    "terceiro andar",
    "quarto andar",
    "quinto andar",
]

# print(predio[0])
# print(predio[2])
# print(predio[3])
# print(predio[1])
# print(predio[4])
# print(predio[5])

for p in predio:
    print(p)

predio.append(input("novo andar: "))

print(predio)

clear()
# Exemplo 2
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
for n in notas:
    soma += n
print("Media: %.2f" % (soma / len(notas)))

clear()
# Exemplo 3
numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input("Número %d: " % (x + 1)))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print("Você escolheu o número: %d" % (numeros[escolhido - 1]))

clear()
# Exemplo 4
V = [1, 2, 3, 4, 5]
L = V

print(V)
print(L)

L[0] = 9

print(V)
print(L)

clear()
# Exemplo 5
V = [1, 2, 3, 4, 5]
L = V[:]

print(V)
print(L)

L[0] = 9

print(V)
print(L)

clear()
# Exemplo 6
L = [1, 2, 3, 4, 5]

print(L[0:5])  # da posicao 0 ate a posição 5, sem incluila
print(L[:5])  # do inicio ate a posicao 5
print(L[:-1])  # do inicio até o fim sem inclui-la
print(L[1:3])  # da posicao 1 ate a posicao 3, sem incluila
print(L[1:4])  # da posicao 1 ate a posicao 4, sem incluila
print(L[3:])  # da posicao 3 até o fim
print(L[-1])  # o ultimo elemento
print(L[-2])  # o penultimo elemento

clear()
# Exemplo 7

L = [12, 9, 5]
print(len(L))
V = []
print(len(V))

clear()
# Exemplo 8

L = []
L.append("a")
print(L)
L.append("b")
print(L)
L.append("c")
print(L)
print(len(L))

clear()
# Exemplo 9
L = []
while True:
    escolhido = int(input("Digite um número (0 para sair): "))
    if escolhido == 0:
        break
    L.append(escolhido)
print(L)