#Usando While para definir maior e menor valores de uma lista:

c=0

l=[]

while c<3:
    c+=1
    n=int(input(f'Digite aqui o {c}º valor: '))
    l.append(n)

    
l.sort()

print(l)

print(f'O maior valor da lista será {l[-1]} e o menor deles será {l[0]}')
