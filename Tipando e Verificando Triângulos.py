#Verificando se as 3 retas podem formar um triângulo, considerando a mesma unidade de medida para ambas e tendo como resultado o tipo do trângulo formado


def triangle():
    print('=+=+=+=+=+=+=+=+=+=+=+')
    print('isso é um triângulo')
    print('=+=+=+=+=+=+=+=+=+=+=+')



r1=int(input('insira aqui o tamanho da reta 1:'))

r2=int(input('insira aqui o tamanho da reta 2:'))

r3=int(input('insira aqui o tamanho da reta 3:'))


a=r1+r2

b=r2+r3

c=r1+r3


if (r1<b,r2<c,r3<a)== (True,True,True):
    triangle()
    
    if r1==r2==r3:
         print('este é um triângulo equilátero')
    
    elif r1==r2 or r2==r3 or r3==r1:
         print('este é um triângulo isóceles')
    
    elif (r1!=r2,r1!=r3,r3!=r2):
         print('este é um triângulo escalêno')            


else:
    print('    isso não é um triangulo')
