cont=0

soma=0

for i in range(1,7):
    a=int(input(f'insira o {i}º valor'))
    
    count=i
    
    if a%2 == 0:
        cont=cont+1
        soma=soma+a


print(f'você inseriu um total de {count} valores sendo {cont} deles par(es) ')

print(f'assim a soma dos números pares é igual a {soma}')