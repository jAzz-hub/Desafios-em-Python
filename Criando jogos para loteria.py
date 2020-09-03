#Criando jogos com 6 números para loteria:
from random import randint

c=0

lof=[]

l=[]


a=int(input('Quantos jogos você quer gerar?'))

while c<a:
    
    for i in range(0,6):
        l.append(randint(0,60))
        if l.count(l[i])>2:
            l.pop(i)

    lof.append(l[:])
    l.clear()
    
    print()
    print(f'=~=~=~=~=~=~[[{c+1}]]=~=~=~=~=~=~')
    print(f'O jogo {c+1} recebeu os números: {lof[c]}')
    
    
    c+=1
print(f'>>>>>Boa Sorte!!<<<<<')
print()
