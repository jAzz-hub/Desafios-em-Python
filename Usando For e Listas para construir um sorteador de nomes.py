#Sorteando nomes com uma tuplas pronta:

#Para isso usei a biblioteca random:
import random

l=[]
keep='s'


while keep in'SIMSiMsImsIMsiMsimssSSsSs':
    aluno=str(input('Insira o número do primeiro aluno: '))
    l.append(aluno)
    keep=str(input('Deseja inserir algum aluno?[S/N] '))

p=random.choice(l)

print('o aluno sorteado foi: {}'.format(p))

