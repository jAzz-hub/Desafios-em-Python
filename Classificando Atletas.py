#Classificando diferentes atletas por suas respectivas idade

a=int(input('em que ano você nasceu atleta? '))
b=int(input('em que ano estamos agora?'))

c=(b-a)


if 0<c<=9:
    print('O atleta tem {} anos.\n Classificação:MIRIM'.format(c))



elif 9<c<=14:
    print('O atleta tem {} anos.\n Classificação:INFANTIL'.format(c))



elif 14<c<=19:
    print('O atleta tem {} anos.\n Classificação:JÚNIOR'.format(c))



elif 19<c<=20:
    print('O atleta tem {} anos.\n Classificação:SÊNIOR'.format(c))



elif c>20:
    print('O atleta tem {} anos.\n Classificação:MASTER'.format(c))

else:
    print('go')
    