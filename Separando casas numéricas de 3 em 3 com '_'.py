#Defini-se as variáveis que serão utilizadas, fazendo a requisição do número que vai passar pelo algorítimo:
f=''
l=[]
s=str(input('Digite um número aqui:'))


#Primeiramente se adicionam os números em uma lista:
for i in s:
    l.append(i)


#Invertemos a lista para realizar um processo de inserção da "_":
l.reverse()


#Definimos que para cada index divisível por 4 seja inserido naquele espaço o caractere "_":
for i,v in enumerate(l):
    if i%4==0:
        l.insert(i,'_')


#Invertemos novamente o número para maior legibilidade no output:
l.reverse()


#Retiramos os '_' extras:
if l[-1] in '_':
    l.pop()


#Constuimos uma String completa com todos os caracteres juntos:
for i in l:
    f+=str(i)

print(f)
