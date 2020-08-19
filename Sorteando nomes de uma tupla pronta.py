#Sorteando nomes com uma tuplas pronta:

#Para isso usei a biblioteca random:
import random

alunos=('João','Alice','Bruno','Thalles','Júlia','Henrique','Isabella','Sarah')

p=random.choice(alunos)

print('o aluno sorteado foi: {}'.format(p))

