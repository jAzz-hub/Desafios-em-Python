#Construindo um interrogatório para analisar um suspeito

print('Responda 1 para verdadeiro e 0 para falso!')
a=int(input('você telefonou para a vítima?'))
b=int(input('esteve no local do crime?'))
c=int(input('mora perto da vítima?'))
d=int(input('devia algo para a vítima?'))
e=int(input('Já trabalhou com a vítima?'))

z=(a+b+c+d+e)

if z==2:
    print('suspeito(a)...')
elif 2<z<4:
    print('pode ser considerado(a) cúmplice.')
elif z==5:
    print('este é um possível assassino(a)!')
else:
    print('a pessoa é inocente.')
