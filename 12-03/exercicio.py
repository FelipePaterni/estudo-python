# Exercicio 1
num = 0
while num == -999:
    num = int(input("Digite um número (-999 para sair): "))
    print(f"Triplo: {num * 3}")

# Exercicio 2
total = 0
while True:
    num = int(input("Digite um positivos(negativo para sair): "))
    if num < 0:
        break
    total += 1
print(f"Total de números digitados: {total}")

# Exercicio 3

total = 0
media=0
while True:
    num = int(input("Digite um positivos(negativo para sair): "))
    if num < 0:
        break
    total += 1
    media += num
print(f"Total de números digitados: {total}")
print(f"Média dos números digitados: {media / total if total > 0 else 0}")

# Exercicio 4
total = 0
while True:
    num = int(input("Digite um positivos(negativo para sair): "))
    if num == 0:
        break
    if(num > 100 and num<200):
     total += 1
print(f"Total de números digitados: {total}")

# Exercicio 5

masculino = 0
while True:
    sexo = input("Digite o sexo (m ou M para masculino, f ou F para feminino): ")
    if sexo == "m" or sexo == "M":
        masculino += 1
    elif sexo == "f" or sexo == "F":
        break
print(f"Total de pessoas do sexo masculino: {masculino}")