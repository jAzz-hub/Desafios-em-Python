"""conversor ºCelsius para Fahrenheit #1."""


# // Line 5: Aqui o código recebe as temperaturas em Celsius.
Celsius = [30, 22, 34, 55, 76, 100, 99, 55, 67, 20, 24]


#// Line 9: As variáveis em Celsius são convertidas em Fahrenheit dentro de uma função e depois colocadas em uma lista.
Fahrenheit = list(map( lambda c: c*9/5 + 32, Celsius ))


#// Line 13-19: A lista é apresentada para o usuário do programa.
print(f'a comparação entre as temperatura passadas em Celsius se transformadas em Fahrenheit ficam de tal forma:')

print('     Celsius <=~=> Fahrenheit')

for i in range(len(Celsius)):
    print(f'temp{i+1})       {Celsius[i]} = {Fahrenheit[i]}')
    print()
