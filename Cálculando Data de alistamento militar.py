a=int(input('olá jovem! Qual sua data de nascimento?'))

b=int(input('em que ano estamos agora?'))

d=(b-a)

z=(d-18)


print('você nasceu em {} tem {} anos em {}'.format(a,d,b))


if d==18:
    print('parece que já está na hora de se alistar não é mesmo...')


elif d<18:
    print('Você ainda é novo de mais para se alisar mas volte quando tiver 18 anos! :D')


elif d>18:
    print('já se passaram aproximadamente {} anos desde que você já deveria ter se alistado!\nMuito cuidado rapaz!\n Venha vamos providenciar isso agora mesmo!'.format(z))
    print('Seu alistamento foi em {}'.format(b-z))


else:
    print('Insira uma data válida!')
