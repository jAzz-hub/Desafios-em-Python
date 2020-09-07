#Imprimindo uma sequência de frases como argumentos de uma função para torná-las títulos com margens proporcionáis à seus respectivos tamanhos:

c=0

f='s'

frases=[]


def escreva(frase):
    ldf=len(frase)+3
    
    print(ldf*'~')
    print( frase)
    print(ldf*'~')


while f in ' s S sim SIM sIM Sim SiM sIm siM sIm ':
    frase=str(input('Digite aqui suas frases em sequência: '))
    
    frases.append(frase) 
    
    f=str(input('Deseja continuar? '))


for frase in frases:
    escreva(frase)

