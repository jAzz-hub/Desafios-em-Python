M=float(input('insira aqui o seu peso em kilogramas(Kg):'))
H=float(input('insisra aqui a sua altura em metros(m):'))


imc=M/H.__pow__(2)

if (M>0,H>0)==(True,True):
    if imc<18.5:
        print('você está abaixo do peso!')
    
    elif 18.5<=imc<=25 :
        print('você está dentro do seu peso saudável e ideal')
    
    elif 25<imc<=30:
        print('você está com sobrepeso')
    
    elif 30<imc<=40:
        print('você está com obesidade ')
    
    elif 40<imc:
        print('você está com obesidade mórbida')

else:
    print('Tente outra vez, com valores positivos! :V')