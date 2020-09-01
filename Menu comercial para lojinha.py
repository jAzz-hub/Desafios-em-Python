"========Loja do seu Zé========"


p=int(input('preço das compras: R$'))

f=int(input('''Insira o número correspondente a forma de pagamento abaixo:
( 1 )~~~~>à vista dinheiro/cheque 
( 2 )~~~~>à vista cartão
( 3 )~~~~>2 vezes no cartão
( 4 )~~~~>3 vezes ou mais no cartão

insira a opção aqui : '''))



z=p - ((p*10)/100) 
x=p - ((p*5)/100)
y=p/2
w=p - ((p*20)/100) + p


if f==1:
    print('O preço das suas compras foi de {} mas com pagamento a vista no dinheiro/cheque o valor a ser pago será {}'.format(p,z))

elif f==2:
    print('O preço das suas compras foi de {} mas com o pagamento realizado a vista no cartão o valor a ser pago será de {}'.format(p,x))

elif f==3:
    print('O preço das suas compras foi de {} mas com o pagamento realizado em duas vezes no cartão serão pagas 2 parcelas de {} sem juros'.format(p,y))

elif f==4:
    c=int(input('qual o número de parcelas em que o pagamento será realizado? '))
    print('O preço das suas compras foi de {} nas com o pagamento realizado em 3 vezes ou mais no cartão serão pagas {} parcelas de {} com juros de 20%'.format(p,c,w/c))
