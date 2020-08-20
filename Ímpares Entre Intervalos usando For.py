#Imprimindo na tela apenas os números ímpares entre dois números:

n1=int(input('Insira aqui o primeiro número do intervalo: '))
n2=int(input('Insira aqui o último número do intervalo: '))

for i in range(n1,n2):
    if i%2 != 0:
        print('{} ~~> Ímpar'.format(i))


