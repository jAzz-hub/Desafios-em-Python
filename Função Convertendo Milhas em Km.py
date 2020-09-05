#Construa uma função que converta milhas em quilometros:


variavel='Qualquer coisa aqui como argumento'


def conversor(milhas):
    milhas=int(input(f'Insira aqui uma quantidade de milhas: '))
    
    km=milhas*1.6
    
    print(f'{milhas} convertido em quilometros é = {km}')
    
    return(km)


conversor(variavel)
