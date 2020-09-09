#Sorteando valores de dados rolados por jogadores e rankeando os valores mais altos dentro de um dicionário:

from random import randint
from time import sleep

c=0

l=[]

d=dict()

print('valores sorteados:')

for i in range(0,4):
    jogador=randint(1,6)
    l.append(jogador)
    print(f'''  O jogador{i+1} tirou {l[i]}''')
    sleep(0.5)

l.sort(reverse=True)

sleep(0.8)

for e in range(len(l)):
    d[f'jogador{e}']=l[e]


print('Ranking dos jogadores: ')


for v in d.values():
    c+=1
    print(f'''  O {c}º lugar tirou {v} ''')
    sleep(0.5)