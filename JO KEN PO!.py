import random
import time

p=['pedra','papel','tesoura']

print(''' Suas opções:

[0] Pedra
[1] Papel
[2] Tesoura
''')

escH=int(input('Qual a sua jogada?' ))

time.sleep(1.5)
print('JO')
time.sleep(1.5)
print('KEN')
time.sleep(1.5)
print('PO!')
time.sleep(2)


p=['pedra','papel','tesoura']

escM=random.choice(p)



def derrota():
    print('Você escolheu {} e o computador escolheu {}'.format(p[escH],escM))
    print('=-=-=-=-=-=')
    print(' DERROTA!')
    print('=-=-=-=-=-=')
    




def vitoria():
    print('Você escolheu {} e o computador escolheu {}'.format(p[escH],escM))
    print('=-=-=-=-=-=')
    print(' VITÓRIA!')
    print('=-=-=-=-=-=')
    
    


def empate():
    print('Ambos escolheram {}'.format(escM))



#Empate
if (escH == 0,escM == p[0]) == (True,True):
    empate()


elif (escH == 1,escM == p[1]) == (True,True):
    empate()


elif (escH == 2,escM == p[2]) == (True,True):
    empate()


#Outras possibilidades de jogo
elif escH == 0:
    if escM == p[2]:
        derrota()


    elif escM == p[1]:
        vitoria()




elif escH == 1:
    if escM == p[2]:
        derrota()


    elif escM == p[0]:
        vitoria()




elif escH == 2:
    if escM == p[0]:
        derrota()
    elif escM == p[1]:
        vitoria()     





