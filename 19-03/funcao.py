def soma(a,b):
    print(a+b)

soma(2, 9)
soma(7,8)
soma(10,15)

def soma(a,b):
    return (a+b)

print(soma(2, 9))
print(soma(7,8))
print(soma(10,15))

def epar(x):
    return x % 2 == 0

def par_ou_impar(x):
    if epar(x):
        return "par"
    else:
        return "impar"
    
print(par_ou_impar(2))
print(par_ou_impar(3))


a = 5
def muda_e_imprime():
   a = 7
   print(f'dentro da função: {a}')

print(f'antes de mudar: {a}')
muda_e_imprime()
print(f'depois de mudar: {a}')


a= 5

def muda_e_imprime():
   global a
   a = 7
   print(f'dentro da função: {a}')

print(f'antes de mudar: {a}')
muda_e_imprime()
print(f'depois de mudar: {a}')
