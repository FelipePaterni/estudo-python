#1

from math import pi


def maior_num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(maior_num(5, 10))

#2

def primeiroHeMultiplo(num1, num2):
    return num1 % num2 == 0
    
print(primeiroHeMultiplo(10, 5))

#3
def areaQuadrado(lado):
    return lado * lado
print(areaQuadrado(5))

#4
def areaTriangulo(base, altura):
    return (base * altura) / 2

print(areaTriangulo(5, 10))

#5 
def areaCirculo(raio):
    return pi * raio * raio

#6
def pos_zero_neg(num):
    if num > 0:
        return 'P'
    elif num < 0:
        return 'N'
    else:
        return 'Z'
    
#7
def somaImposto(taxaImposto, custo):
    return custo + (custo * taxaImposto / 100)

print(somaImposto(10, 100))

#8

def eleitora_ou_nao(idade):
    if idade < 16:
        return "Não eleitor"
    elif idade >= 16 and idade < 18:
        return "Eleitor facultativo"
    else:
        return "Eleitor obrigatório"
    
#9
def soma_impares(a,b):
    soma = 0
    for num in range(a, b + 1):
        if num % 2 != 0:
            soma += num
    return soma

print(soma_impares(1, 10))  