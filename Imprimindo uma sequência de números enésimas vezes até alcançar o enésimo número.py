#Inserindo um limite para que uma sequência de números seja mostrada até chegar no mesmo:


n=0


x=int(input("Insira aqui um valor para x"))


def enésimo(x):
    print(x,end='')


for i in range(0,x+1):
    n=0
    print()
    
    while n<=i:
        enésimo(n)
        n+=1
        

