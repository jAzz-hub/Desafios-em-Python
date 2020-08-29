#Verificando se as posições de parênteses em expressões algébricas estão sendo expressadas corretamente

c=0

lista=[]


expressão=input('Insira uma variável aqui: ')


for caractere in expressão:
    lista.append(caractere)


for prtzs in lista:
    if prtzs==')' or prtzs=='(':
        c+=1


if c%2!=0:
    print('Sua expressão está errada!')

else:
    print('Sua expressão está sussa!')
    
