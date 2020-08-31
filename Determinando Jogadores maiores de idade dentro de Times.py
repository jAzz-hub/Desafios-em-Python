c=0

maiores=list()

integrante=list()

time=list()


qj=int(input('Quantos são os integrantes do seu time? '))


for i in range(0,qj):
    integrante.append(str(input('Nome: ')))
    integrante.append(int(input('Idade: ')))
    integrante.append(str(input('Função: ')))
    time.append(integrante[:])
    integrante.clear()


for integrante in time:
    if integrante[1]>18:
        c+=1
        maiores.append(integrante[0])

    
print(f'Seu time tem {qj} jogadores {c} deles são maiores de 18 anos')
print(f'Sendo estes {maiores}')


