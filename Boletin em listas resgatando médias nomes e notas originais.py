#Mostrando a média dos alunos a partir de suas respectivas notas inseridas e depois mostrando em específico as suas notas:

a=0

Continuar='s'

NomesNotas=[]

Alunos=[]

Nota=[]

Média=[]

qtdn=int(input('Quantas notas deseja inserir'))

while Continuar in 'SIMSImSimsIMsiMsImSiMSs':
    Alunos.append(str(input('Nome: ')))
    
    
    s=0

    
    for i in range(0,qtdn):    
        Nota.append(int(input('Nota: ')))
        
        s+=Nota[i]
    
    
    m=s/(i+1)
    Média.append(m)
    
    Alunos.append(Nota[:])
    Nota.clear()
    
    NomesNotas.append(Alunos[:])
    Alunos.clear()
    
    
    Continuar=str(input('Quer continuar? '))


print()


print('♮  Nome       Média')

for i,var in enumerate(NomesNotas):
    print(f'♮ {i} {var[0]}',end='....')
    print(f'{Média[i]}')


print()    


print('Para sair digite 999')

while a<=999:
    
    a=int(input('Insira o número do aluno tal qual deseja ver as notas: '))
    
    print(f'Notas de {NomesNotas[a][0]} são {NomesNotas[a][1]}')
    
    
    if a==999:
        break

