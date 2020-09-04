#Pedindo o peso de 8 pessoas, e lendo o maior e o menor peso:

from math import inf


l=[]


for i in range(1,8):
    pp=float(input('qual o peso da {} pessoa: '.format(i)))
    
    
    if pp>0:
        l.append(pp)
    
    else:
        print('peso inválido')


l.append(inf)

l.sort(reverse=True)

print('O maior peso lido foi {} e o menor foi {}'.format(l[1],l[7]))    
