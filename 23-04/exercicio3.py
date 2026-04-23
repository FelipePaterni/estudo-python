i = input("1ª string: ")
j = input("2ª string: ")

result = []

for char in i:
    if char not in j and char not in result:
        result.append(char)

for char in j:
    if char not in i and char not in result:
        result.append(char)

print("".join(result))
