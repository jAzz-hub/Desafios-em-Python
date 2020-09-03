from math import sqrt


r=0

j=i=1

aij=[]


for e in range(0,9):
    if e==3 or e==6:
        j=1
        i+=1

    aij.append(list(input(f'Digite um valor para a{i}{j}: ')))
    j+=1


ordem=sqrt(len(aij))


print(f'você tem uma matriz de ordem {ordem:.0f}')


for i in range(0,9):
    print(f'[ {aij[r][0]} ]',end='')
    r+=1
    
    if r==3 or r==6:
        print()

