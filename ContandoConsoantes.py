#Este programa conta o número de consoantes em uma variável do tipo str e mostra quais e quantas elas são.
c=0

consoantes='qwrtyplkjhgfdsmnbvcxz'

consi=[]


i=(str(input('Digite uma palavra: ')))


for l in range(len(i)):

    if i[l] in consoantes:
        consi.append(i[l])
        print('CONSOANTE!')  

    else:
        print('VOGAL!')

    c+=1


print(f'Na palavra {i} foram lidas {len(consi)} consoantes sendo estas {consi}')