#Pedindo 2 valores e mostrando o maior entre eles

V1=float(input('insira aqui o primeiro valor: '))
V2=float(input('insira aqui o segundo valor: '))

if V1>V2:
    print('O maior valor é {}'.format(V1))
elif V2>V1:
    print('O maior valor é {}'.format(V2))
elif V2==V1:
    print(f'O valor de amboas é igual sendo que ambos são {V1}')
else:
    print('Os valores são iguais!Rode o programa de novo para tentar novamente')
    