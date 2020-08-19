#Mostrando um nome completo em maiúsculas e minúsculas, seu tamanho, e transformando tudo em lista com o tamanho dos nomes
name =input('Digite seu nome completo aqui: ')

n2=name.split()



print('Seu nome em maiúsculas é: {}'.format(name.upper()))


print('Seu nome em minúsculas é: {}'.format(name.lower()))


print('Seu nome tem ao todo: {} caracteres'.format(len(name)))


print('o seu primeiro nome é:{} e tem {} carateres.'.format(n2[0],(len(n2[0]))))

print(n2)




