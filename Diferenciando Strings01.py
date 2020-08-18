

S1=input(str('insira aqui a sua 1º string: ')).strip()
S2=input(str('insira aqui a sua 2º string: ')).strip()

ls1=len(S1)
ls2=len(S2)

print(f'a 1º string será igual a {S1}')
print(f'e a 2º  igual a {S2}')

if S1==S2:
  print('as strings são iguais')
else:
  print('as strings são diferentes!')

print(f'o tamanho da string {S1} é de {ls1} caracteres(sem espaços)')
print(f'o tamanho da string {S2} é de {ls2} caracteres(sem espaços)')

if ls1==ls2:
  print('as duas strings tem os mesmos tamanhos!')
else:
    print('as duas strings tem tamanhos diferentes!')

