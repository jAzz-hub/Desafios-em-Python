#Solicitando um número e exibindo a sua tabuada, caso seja inserido um valor negatico o programa fecha:


while True:
    n=int(input('Solicite um número para saber sua tabuada ou um negativo para sair: '))
    
    if n<=0:
        print('='*30)
        
        print('Obrigado por testar esse programa, Até logo! :D')
        
        break
        
        exit()
    

    print('='*30)

    for count in range(0,11):
        print(f'{n}*{count}={n*count}')
    
    print('='*30)
    