#Inserindo o números tipados em lista dentro de uma lista em quantidade pré-determinada:

qdn=int(input('Quantos números quer inserir? '))

l=[]

for i in range(0,qdn):
    n=int(input('Insira aqui um número'))
    
    b=[n]
    
    l.append(b)
    

print(f'Você inseriu os  {len(l)} números sendo cada um deles uma lista dentro de {l}')

