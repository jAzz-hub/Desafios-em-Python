#Verificando se os argumentos de uma função representam números múltiplos entre si:

n1=int(input('Insira algum número número:  '))

n2=int(input('Insira outro número número: '))


print('Verificando se ambos são multiplos entre si')


def is_multiple(a,b):
    if a%b==0:
        print(f'{a} e {b} São multiplos entre si!')
        return(True)

    elif b%a==0:
        print(f'{a} e {b} São multiplos entre si!')
        return(True)

    else:
        print(f'{a} e {b} Não são multiplos entre si!')
        return(False)


is_multiple(n1,n2)


