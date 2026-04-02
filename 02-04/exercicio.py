# 1

lista = []

for i in range(1, 6):
    lista.append(int(input(f"Digite o {i}º número: ")))

print(f"Lista de números: {lista}")

#2
lista = []

for i in range(1, 11):
    lista.append(int(input(f"Digite o {i}º número: ")))

print(f"Lista de números: {lista[::-1]}")

#3

notas = []

for i in range(1, 5):
    notas.append(float(input(f"Digite a {i}ª nota: ")))

media = sum(notas) / len(notas)
print(f"notas: {notas}")
print(f"A média das notas é: {media}")

#4

caracteres = []
consoantes = []
for i in range(1, 6):
    caracteres.append(input(f"Digite o {i}º caractere: "))

for c in caracteres:
    if c.lower() in "bcdfghjklmnpqrstvwxyz":
        consoantes.append(c)

print(f"Consoantes: {len(consoantes)}")

#5 

lista1 = [1,2,3,4]
lista2 = [5,6,7,8,9,10]
lista3 = []




lista3.extend(lista1)
lista3.extend(lista2)

print(f"Lista combinada: {lista3}")