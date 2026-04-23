i = input("1ª string: ")
j = input("2ª string: ")

result = ""
for char in i:
    if char in j and char not in result:
        result += char

print(result)
