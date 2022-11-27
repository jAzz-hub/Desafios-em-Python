#Importando bibliotecas
import numpy as np
import random as rand


        #Início da definição de Funções:


#Simetria é a propriedade a qual indica que se há uma relação que contém elementos de A estes aparecem em uma ordem e depois trocados de lugar na relação:
#   Ou seja, para A = {1,2} se 1 e 2 E R logo se R é Simétrica se (1,2) e (2,1) pertencem a R}:
#   R é Simétrica se e somente se para todo (a,b E A), aRb -> bRa 
#   Ou seja para quaisquer elementos de A em R, há uma relação deste com outro indicando que para cada aresta de ida existe uma aresta de volta:

def Simetria(matriz, copias):
  """
        O método Simetria recebe os argumentos matriz, copias e informa se essa matriz é Simétrica ou não!
        matriz => É uma lista com cada elemento sendo outra lista menor de 2 elementos sendo estes 2 números inteiros.
        copias => É um número inteiro indicando quantas listas dentro da matriz tem pares de elementos iguais.
  """

  verdades = copias
  maior = 0

  if(len(matriz)==1):
    return False

  else:
    for i in matriz:

      if((i[0]>i[1]) and (i[0]>maior)):
        maior = i[0]

      elif((i[1]>i[0]) and (i[1]>maior)):
        maior = i[1]

      else:
        maior = maior
    maior+=1
    MatrizZero = np.zeros((maior,maior), dtype = int)

    veta = []
    vetb = []

    for i in matriz:
    
      if(MatrizZero[i[0]][i[1]]==0):
        MatrizZero[i[0]][i[1]]=1
      

    for i in range(len(MatrizZero)):
      for j in range(len(MatrizZero)):
        
        if((MatrizZero[i][j]==1) and (MatrizZero[j][i]==1)):
          verdades+=1
        
        else:
          verdades+=0
  
    if(verdades==len(matriz)):
      return True

    else:
      return False



#Reflexividade é a propriedade a qual indica que se há uma relação que contém elementos de A, estes aparecem em pares iguais na relação:
#   Ou seja, para A = {1,2} se 1 e 2 E R logo se R é Reflexivo, (1,1) e (2,2) tem de pertencer a R}:
#   R é transitiva se e somente se para todo (a E A), (a,a)E R
#   Ou seja para quaisquer elementos de A em R, há uma relação deste com ele mesmo o que indica que existe uma aresta que parte de um vertice para ele mesmo:

def Reflexao(matriz):
  """
        O método Reflexao recebe o argumento matriz, e informa se essa matriz é Reflexiva ou não!
        matriz => É uma lista com cada elemento sendo outra lista menor de 2 elementos sendo estes 2 números inteiros.
  """
  #percorrer a matriz:
    #Se os elementos são iguais:
  cont = 0
  vet_aux = []
  
  for i in matriz:
    vet_aux.append(i[0])
    vet_aux.append(i[1])
  
  vet_aux = set(vet_aux)

  for i in matriz:
    if(i[0]==i[1]):
      cont+=1
    else:
      cont+=0

  if cont==len(vet_aux):
    return True

  else:
    return False
  


#Transitividade é a propriedade de que se há uma relação (a,b) e uma relação (b,c) tem de haver uma relação (a,c):
#   R é transitiva se e somente se para todo (a,b E A)(aRb)^(bRa)->a=b
#   Ou seja caso haja aresteas entre vertices 1, 2 e 3 é necessário que haja arestas entre os vétrices 1 e 3 considerando a ordenação de 1->2, 2->3 e 1->3:

def Transitividade(matriz):
  """
        O método Transitividade recebe o argumento matriz, e informa se essa matriz é Transitiva ou não!
        matriz => É uma lista com cada elemento sendo outra lista menor de 2 elementos sendo estes 2 números inteiros.
  """
  
  #Caso a conclusão não seja satisfeita a relação é transitiva por default:
  if(len(matriz)<3):
    return True  

  elif(len(matriz)%2==0):
    verdades = 0
    espelho = 0

    for i in matriz:
      a = i[0]
      b = i[1]

      for i in matriz:
        b_aux = i[0]
        c = i[1]

        if(b_aux == a or a==b or b==c or a==c):
          pass

        elif(b == b_aux):
          espelho +=1 

          for i in matriz:

            if((i[0]==a and i[1]==c)):
              verdades+=1        
            else:
              pass
        else:
            pass

    if(espelho==verdades):
      return True

    else:
      return False

    #Fim da definição de Funções:



    #Início da definição de relações:
copias = 0
c = 0
n = rand.randint(0,16)
r = []

print(f"\n\nA relação estabelecida tem {n} elementos")

while(c<n):
  z=[]

  a = rand.randint(0,10)
  b = rand.randint(0,10)

  if((a==b) and (a in r) and (b in r)):
    copias+=1

  z.append(a)
  z.append(b)
  r.append(z)
  
  c+=1

    #Fim da definição de Relações:



    #Início da realização de testes:
print("\nAs relações estabelecidas foram:")
print(r)



teste1 = Reflexao(r)
teste2 = Simetria(r,copias)
teste3 = Transitividade(r)

print("Conclusões:")
if(teste1):
  print("\n\nA relação analisada é reflexiva")

else:
  print("A relação analisada não é reflexiva!")


if(teste2):
  print("A relação analisada é simétrica")

else:
  print("A relação analisada não é simétrica!")


if(teste3):
  print("A relação analisada é transitiva")

else:
  print("A relação não é transitiva!")
    #Fim da definição de Relações:
