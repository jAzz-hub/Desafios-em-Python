#Usando dicionários para mostrar o nome do aluno, sua média e a partir disso sua situação:

aluno={}


aluno['Nome']=str(input('Nome: '))

aluno['Média']=int(input('Média: '))

print()
print()

print(f'Nome: {aluno["Nome"]}')

print(f'Média: {aluno["Média"]}')


if aluno['Média']<6:
    print(f'Situação: Abaixo da média')

elif aluno['Média']==6:
    print(f'Situação: Na média')

else:
    print(f'Situação: Acima da média')