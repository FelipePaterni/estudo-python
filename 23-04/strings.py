# Exemplo 1

L = list("Hello, World!")
print(L)
L[0] = "h"

print(L)
s = "".join(L)
print(s)


# Exemplo 2

nome = "Felipe Soares Paterni Chaves"
print(nome.startswith("Felipe"))
print(nome.startswith("felipe"))
print(nome.endswith("Chaves"))

# Exemplo 3

s = "o Rato roeu a roupa do rei de Roma"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.lower().startswith("o rato"))
print(s.upper().endswith("ROMA"))

# Exemplo 4

s = "Ana Maria Chico"
print("Ana" in s)
print("Maria" in s)
print("Chico" in s)
print("a A" in s)
print("ana" in s)

# Exemplo 6

s = "Todos os caminhos levam a Roma"
print("levam" not in s)
print("Caminhos" not in s)
print("AS" not in s)

# Exemplo 7

t = "um tigre, dois tigres, tres tigres"

print(t.count("tigre"))
print(t.count("tigres"))
print(t.count("t"))
print(t.count("z"))

# Exemplo 8

s = "Olá mundo"
print(s.find("mun"))
print(s.find("ok"))

# Exemplo 9
s = "um tigre, dois tigres, tres tigres"
print(s.replace("tigre", "gato"))

# Exemplo 10 
t = "     Olá     "
print(t.strip())

# Exemplo 11
s = "A riqueza que nós temos ninguém consegue perceber"
print(f"Frase: {s}")
t = s.split()
print(f"Frase: {t}")

# Exemplo 12

s = "16-08-2006 "
print(f"Frase: {s}")
t = s.split("-")
print(f"Frase: {t}")
