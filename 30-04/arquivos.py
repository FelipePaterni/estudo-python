#1
 
arquivo = open('numeros.txt' ,'w')

for linha in range(1, 101):
    arquivo.write("%d\n" % linha)

arquivo.close()

# 2

arquivo = open('numeros.txt' ,'r')
for linha in arquivo.readlines():
    print(linha)

arquivo.close()


# 3 
impares = open("impares.txt", "w")
pares = open("pares.txt", "w")

for n in range(0, 1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
    else:
        impares.write("%d\n" % n)

pares.close()
impares.close()


# 4
multiplo4 = open("multiplos4.txt", "w")
pares = open("pares.txt", "r")

for linha in pares.readlines():
    n = int(linha)
    if n % 4 == 0:
        multiplo4.write("%d\n" % n)

pares.close()
multiplo4.close()