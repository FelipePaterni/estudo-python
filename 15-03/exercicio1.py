#Felipe Soares Paterni Chaves

# 1

velo = float(input("Digite a velocidade do carro: "))
limite = 80
multa = 5
result = 0
if velo > limite:
    vUltrapassado = velo - limite
    result = vUltrapassado * multa
print(f"A multa sera: {result}")


# 2
salario = float(input("Digite o salario do funcionario: "))
limite = 1250.00

if salario > limite:
    result = salario * 0.10  # 10% de aumento
else:
    result = salario * 0.15  # 15% de aumento
print(f"O resultado sera: {result}")

# 3

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))
ope = input("Qual operação (+ ,- ,* ,/ )")

match ope:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        result = a / b
    case _:
        print("operação invalida")
print(result)

# 4
valor = float(input("Valor da casa: "))
salario = float(input("Salario: "))
anos = int(input("Anos a pagar: "))

meses = anos * 12
prestacao = valor / meses
limite = salario * 0.30

if prestacao <= limite:
    print(f"Prestação mensal: R$ {prestacao:.2f}")
else:
    print(f"Prestação de R$ {prestacao:.2f} excede 30% do salário (R$ {limite:.2f})")

# 5

kWh = float(input("Consumo de energia (kWh): "))
tipoInstalacao = input("Tipo de instalação (R, C, I): ")


if tipoInstalacao == "R":
    if kWh <= 500:
        preco_kWh = 0.40
    else:
        preco_kWh = 0.65
elif tipoInstalacao == "C":
    if kWh <= 1000:
        preco_kWh = 0.55
    else:
        preco_kWh = 0.60
elif tipoInstalacao == "I":
    if kWh <= 5000:
        preco_kWh = 0.55
    else:
        preco_kWh = 0.60
else:
    print("Tipo de instalação inválido")
    exit()

valor_conta = kWh * preco_kWh


print(f"Valor da conta: R$ {valor_conta:.2f}")

