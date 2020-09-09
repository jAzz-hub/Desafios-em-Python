#Usando tuplas e listas para definir maiores e menores números sorteados:

from random import randint

c=str(randint(0,9))


for i in range(0,4):
    a=str(randint(0,9))
    a+=c
    c=a
    

d=tuple(a)

print(f'os valores sorteados foram{d}')

l=list(d)

l=sorted(l)

print(f'o maior valor foi {l[4]}')


print(f'e o menor valor foi {l[0]}')

