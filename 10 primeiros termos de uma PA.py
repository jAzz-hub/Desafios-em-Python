
print('\n',30*'#','\n')

print('10 primeiros Termos de uma PA')

print('\n',30*'#','\n')


pt = int(input('insira aqui o primeiro termo de uma PA: \n'))

R = int(input('insira aqui a razão entre os termos da PA: \n'))

cont = pt+R


for i in range(1,11):
    cont=cont+R
    print(cont, end=' -> ')


print('FIM')
