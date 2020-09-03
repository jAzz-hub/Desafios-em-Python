tupla=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')

escolha=int(input('Digite um número entre 0 e 20: '))

while escolha not in range(len(tupla)):
    escolha=int(input('Tente de novo,digite um número entre 0 e 20:'))

print(f'Você digitou o número {tupla[escolha].lower()}.')

