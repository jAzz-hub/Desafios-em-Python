#Jogando impoar ou par com o computador até que a máquina vença:

from time import sleep

from random import randrange

from random import random


turn=vict=lose=0


print('+=+'*30)

print('Bem vindo ao Par ou Ímpar do milhão')

print('+=+'*30)


while True:
    hc=int(input('Escolha um número, humano: '))
    
    humano=str(input('''Você quer par ou ímpar, 
    digite [I para ímpar/ P para par]? ''')).upper().split()[0]
    
    pc=randrange(0,10)

    soma=hc+pc
    
    
    if humano in 'IÍ':
        if soma%2==0:
            r='Derrota!'
            
            print(f'Você jogou {hc} e o computador {pc}, no total de {soma} DEU PAR')
            
            print(r)
            
            break
        
        
        elif soma%2!=0:
            r='Vitória'
            
            turn+=1
            
            print(f'Você jogou {hc} e o computador {pc}, no total deu {soma} DEU IMPAR')
            
            print(f'{r} Você venceu {turn} vezes')
    
    
    elif humano in 'P':
        if soma%2==0:
            r='Vitória'
            
            turn+=1
            
            print(f'Você jogou {hc} e o computador {pc}, no total deu {soma} DEU PAR')
            
            print(f'{r} Você venceu {turn} vezes')
        
        
        elif soma%2!=0:
            
            r='Derrota'
            
            print(f'Você jogou {hc} e o computador {pc}, no total deu {soma} DEU IMPAR')
            
            print(f'{r} Você venceu {turn} vezes')
            
            break

