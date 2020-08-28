#Criando 3 listas, 1º com todos os valores, 2º com os valores ímpares insereidos, 3º com os valores pares:


r='s'

ltotal=[]

limpar=[]

lpar=[]


while r in 'SsSimsimSIMsImsiMSiM':
    n=int(input('Um número aqui de sua escolha:'))
    
    ltotal.append(n)
    
    r=input('Quer continuar? [S/N]')


for valor in ltotal:
    if valor%2==0:
        lpar.append(valor)
    
    else:
        limpar.append(valor)


print(f'Os valores digitados são: {ltotal} ')

print(f'Sendo o valores pares: {lpar}')

print(f'E os ímpares: {limpar} ')
