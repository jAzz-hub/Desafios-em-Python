
#Demonstrando 15% de um salário e dando um aumento de 15% no mesmo.

a=int(input('insira aqui o salário de um funcionário:'))


aG=(a*10/100)

aP=(a*15/100)

s=a+aG

s2=a+aP


if a>1250:
    print('o seu salário de R${:.2f} terá um aumento de R${:.2f}, e agora você recebe R${:.2f}'.format(a,aG,s))

elif a<=1250:
    print('o seu salário de R${:.2f} terá um aumento de R${:.2f}, e agora você recebe R${:.2f}'.format(a,aP,s2))
