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

# Exemplo 2
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
for n in notas:
    soma += n
print("Media: %.2f" % (soma / len(notas)))

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

# Exemplo 4
v = [1,2,3,4,5,6]
l = v

print(v)
print(l)

l[0] = 9

print(v)
print(l)
