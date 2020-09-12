#Somando valores infinitamente até digitar 999:

soma=n=0

contador=1


while True:
    n=int(input(f'digite o {contador}º da lista para a soma ou 999 para parar: '))
    
    if n==999:
        break
        exit()

    contador+=1
    
    soma+=n
    
print(f'A soma dos {contador-1} valores inseridos tem um total de {soma}')
