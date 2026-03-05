# Felipe Soares Paterni Chaves

# 1
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"Soma: {num1 + num2}")

# 2
metros = int(input("Digite o valor em metros cúbicos: "))
mililitros = metros * 1000
print(f"Mililitros: {mililitros}")

# 3
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos (0-60): "))

if minutos > 60:
    raise ValueError("Os minutos devem ser menores que 60.")

segundos = int(input("Digite a quantidade de segundos: "))

horas += dias * 24
minutos += horas * 60
segundos += minutos * 60
print(f"Total em segundos: {segundos}")

# 4
salario = float(input("Digite o valor do salário: "))
porcent = float(input("Digite a porcentagem do aumento: "))
result = salario + (salario * porcent / 100)
print(f"Salário com aumento: {result}")

# 5 
preco = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o valor do desconto (%): "))
result = preco + (preco * desconto / 100)
print(f"Preço final: {result}")

# 6
dist = float(input("Digite a distância: "))
velo = float(input("Digite a velocidade média: "))
result = dist / velo
print(f"Tempo de viagem: {result} horas")

# 7
c = float(input("Digite o valor em graus Celsius: "))
f = 9 / 5 * c + 32
print(f"Temperatura em Fahrenheit: {f}")

# 8
km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))
result = 60 * dias + 0.15 * km
print(f"Valor a pagar: {result}")

# 9
qtdCigas = int(input("Digite quantos cigarros você fuma por dia: "))
anos = int(input("Digite há quantos anos você fuma: "))

cigasPorAno = qtdCigas * anos
minPerdidos = cigasPorAno * 10
diasPer = minPerdidos // 525600

print(f"Dias de vida perdidos: {diasPer}")
