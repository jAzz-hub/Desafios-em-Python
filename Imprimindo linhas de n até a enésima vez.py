#Inserindo um número que será imprimido até sua enésima vez passando pelas enésimas vezes de números anteirores:

x=int(input("Insira aqui um valor para x"))


def enésimo(x):
    print(f' {x} '*x)


for i in range(0,x+1):
    enésimo(i)
