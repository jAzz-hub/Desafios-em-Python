#intervalo entre números:
c=0
a=int(input('insisra aqui o 1º número inteiro:'))
b=int(input('insisra aqui o 2º número inteiro:'))

print(f'entre {a} e {b} temos: ')

for i in range(a+1,b):
    print(i)
    c+=1

print(f'sendo assim {c} algarísmos')