#Verificando se um ano é bissexto ou não:

a=int(input('insira aqui algum ano específico:'))


if a%4 == 0 and a%100 != 0:
    print(f'{a} é um ano bissexto')

else:
    print(f'{a} não é um ano bissexto')    
