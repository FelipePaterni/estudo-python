#6
T = [-10, -8, 0, 1, 2, 5, -2, -4]
T.sort()

print(f"Menor valor: {T[0]}")
print(f"Maior valor: {T[-1]}")
print(f"Media dos valores: {sum(T)/len(T)}")

#7

V = [9, 8, 7, 12, 0, 13, 21]
P = []
i = []
for x in V:
    if x % 2 == 0:
        P.append(x)
    else:
        i.append(x)
print(f"Valores pares: {P}")
print(f"Valores ímpares: {i}")