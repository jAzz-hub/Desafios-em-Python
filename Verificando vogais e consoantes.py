#Verificando a primeira letra de uma variável como vogal ou consoante

letter=str(input('Digite algo para verificar se a primeira letra é vogal ou consoante: ')).upper().strip()[0]

if letter in 'AEIOU':
    print('{} foi a primeira letra digitada e esta é uma vogal'.format(letter))
    
else:
    print('{} foi a primeira letra digitada e esta é uma consoante'.format(letter))
