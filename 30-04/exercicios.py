# 1
aluno = open('aluno.txt', 'w')
nome = input("Digite o nome do aluno: ")
ra = input("Digite a RA do aluno: ")
curso = input("Digite o curso do aluno: ")

aluno.write("Nome: %s\n" % nome)
aluno.write("RA: %s\n" % ra)
aluno.write("Curso: %s\n" % curso)
aluno.close()


# 2

aluno = open('aluno.txt', 'r')
for linha in aluno.readlines():
    print(linha)

aluno.close()

# 3

media = open("media.txt", "w")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media.write("Nota 1: %.2f\n" % nota1)
media.write("Nota 2: %.2f\n" % nota2)
media.write("Média: %.2f\n" % ((nota1 + nota2) / 2))
media.close()

# 4
media = open("media.txt", "r")
for linha in media.readlines():
    print(linha)
media.close()

# 5
produtos = open("produtos.txt", "w")


for n in range(0, 3):
    codigo = input("Digite o código do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos.write("Código: %s\n" % codigo)
    produtos.write("Descrição: %s\n" % descricao)
    produtos.write("Preço: %.2f\n" % preco)
    produtos.write("\n")

produtos.close()





# 6 

produtos = open("produtos.txt", "r")
conteudo = produtos.read()
produtos.close()

blocos = [b.strip() for b in conteudo.split('\n\n') if b.strip()]
for bloco in blocos:
    linhas = [li.strip() for li in bloco.splitlines() if li.strip()]
    descricao = None
    preco = None
    for li in linhas:
        if li.lower().startswith('descri'):
            descricao = li.split(':', 1)[1].strip()
        if li.lower().startswith('preço') or li.lower().startswith('preco'):
            preco_str = li.split(':', 1)[1].strip()
            try:
                preco = float(preco_str.replace(',', '.'))
            except ValueError:
                preco = None
    if preco is not None and preco > 500:
        if descricao:
            print(descricao)
        else:
            print('Descrição não encontrada para produto com preço > 500')

# 7

contatos = open("contatos.txt", "w")

while True:
    nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    telefone = input("Digite o telefone do contato: ")
    contatos.write("Nome: %s\n" % nome)
    contatos.write("Telefone: %s\n" % telefone)
    contatos.write("\n")

contatos.close()
# 8

contatos = open("contatos.txt", "r")
conteudo = contatos.read()
contatos.close()
print(conteudo)


# 9
ip = open("ips.txt", "r")

ipInvalidos = open("ipinvalidos.txt", "w")
ipValidos = open("ipvalidos.txt", "w")

for linha in ip.readlines():
    ip = linha.split(".")
    if len(ip) == 4:
        for n in ip:
            if int(n) < 0 or int(n) > 255:
                ipInvalidos.write(linha)
                break
        else:
            ipValidos.write(linha)
    else:
        ipInvalidos.write(linha)
