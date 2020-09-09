#Verificando dentro de uma tupla a ocorrÊncia do número 9, posição o número 3 e quais os números pares:


c3=p3=c9=0

par=('')


n1=int(input('Digite aqui o 1º valor: '))

n2=int(input('Agora o 2º: '))

n3=int(input('O 3º: '))

n4=int(input('E o 4º: '))


z=(n1,n2,n3,n4)


print(f'você digitou os valores {z}')


for nx in z:

    if (nx/9)==1:
        c9+=1
    
    if (nx/3)==1:
        p3=z.index(3)+1
        c3+=1

    else:
        pass

    if nx%2==0:
        par+=' '+str(nx)+' '


b=par


print(f'o nove apareceu {c9} vezes na tupla')


if p3>1:
    
    print(f'o número 3 apareceu {p3} vezes na tupla e pela primeira vez no {p3}º espaço na tupla')


elif p3==0:
    
    print('o valor 3 não apareceu em nenhuma posição')


else:
    
    print(f'o número 3 apareceu {1} vez na tupla na {p3}º posição')


print(f'os números pares  foram: {b}')
