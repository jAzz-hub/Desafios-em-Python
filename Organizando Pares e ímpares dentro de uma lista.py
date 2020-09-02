#Pares e ímpares dentro de uma lista em ordem crescente

lista=[[],[]]

for i in range(0,7):
    
    n=int(input(f'Digite o {i} valor: '))
    
    if n%2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)


lista[0].sort()
print(f'Os valores pares digitados foram {lista[0]}')

lista[1].sort()
print(f'Os valores ímpares digitados foram {lista[1]}')

