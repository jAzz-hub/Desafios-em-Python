#Lendo um vetor com 20 valores e colocando-os em vetores com apenas número ímpares ou apenas números pares:


l=[]

limpar=[]

lpar=[]


while len(l)<20:
    l.append(int(input('Insira valores aqui: ')))


z=sorted(l)


for n in z:
    if n%2==0:
        limpar.append(n)
    else:
        lpar.append(n)


print(l)

print(limpar)

print(lpar)
