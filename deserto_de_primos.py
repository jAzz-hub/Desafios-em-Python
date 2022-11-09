'''
  Para todo número inteiro positivo n, existe uma sequência de n números inteiros consecutivos que não são primos.
  1- prove que isso é real através de um código:
'''

#Tentativa por força bruta que falhou:
#criar função recursiva(int ponto_inicial,int tamanho_seq):
    #for i in range(ponto_inicial,tamanho_seq+ponto_inicial)
        #se tamanho do vetor != contador:
            #se i não é primo:
                #contador+=1
                #armazena i no vetor
            #se i é primo:
                #função recursiva(i)
        #se não:
            #quebra

    #print("Existe uma sequência que começa em primeiro_da_seq  e termina em i de tamanho_seq elementos não primos") 
    #return True


'''
Método que considera que uma sequência de não primos é estabelecida por uma sequência que soma todos os números
de 0 até o número inteiro escolhido ao fatorial do número escolhido:
  1 - Exemplo:
    1.1 - Escolhendo 5, temos 120 = !5
    1.2 - Portanto deserto_dos_primos = [120+1,120+2,120+3,120+4,120+5]
'''

#Primeiro define-se uma entrada de números inteiros:
tamanho_seq = int(input("Insira aqui um número inteiro n:"))

#Função que calcula o fatorial do número:
def fatorial(r,fat):
    r = r*fat
    fat = fat-1
    
    if(fat==0):
        return r

    else:   
        return fatorial(r, fat)

#Associando o fatorial à um número:
x = fatorial(1,tamanho_seq)

#Cria-se um laço para elaborar uma sequência de não primos com base no fatorial calculado:
print("Os números não primos da sequência são:")
for i in range(0,tamanho_seq+1):
    if(i>0):
      print(x+i)
