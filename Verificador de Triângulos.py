#Verificando se as 3 retas podem formar um triângulo considerando que ambas pertencem às mesmas unidades de medidas

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

else:
    print('    isso não é um triangulo')
