# Exemplo 1
print('Ola Puthon')  # Somente Texto
print(7 + 7)  # operacoes matematicas
print('O resultado de 7+7 e', 7 + 7)  # texto + operacao
# Exemplo 2
nome = 'Vincent'  # str
idade = 30  # int
peso = 83.5  # float
print(nome, idade, peso)
# Exemplo 3
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
peso = float(input('Qual o seu peso? '))
print('Seu nome e {} sua idade {} e seu peso {}'.format(nome, idade, peso))
# Exemplo 4
import math

num = 2.5
print(math.trunc(num))
# Exemplo 5
var = 'Hello World'
print(var[6])
print(var[:5])
print(var[6:11])
print(var[6:])
print(var[0:19:2])
# Exemplo 6
len(var)  # retorna o umero de caracteres
print(var.count('o'))  # conta o numero de o's da palavra
print(var.count('l', 0, 5))  # conta quantos l's tem dentro de hello
print(var.find('lo'))  # indica a posicao de onde comeca 'lo'
print('World' in var)  # retorna True se a palavra se encontrar dentro do texto
print(var.replace('World', 'Python'))  # troca uma palavra por outra no texto
print(var.upper())  # todas as letras do texto ficam Maiusculas
print(var.lower())  # todas as letras do texto ficam Minusculas
print(var.split())  # quebra o texto em partes
# Exemplo 7
idade = int(input('Entre com sua idade: '))
if idade < 18:
    print('Voce e menor de idade')
else:
    print('Voce e maior de idade')
# Exemplo 8
for c in range(0,10):#mostra um conteudo x vezes
    print('Python e legal')

for c in range(0,10):#a variavel c assume um novo valor a cada iteracao
    print(c)

for c in range (10,0,-1):#realizando uma contagem regressiva
    print(c)
# Exemplo 8

var = 1
while var < 5:
    print(var)
    var+=1

senha = ''

while senha != 'python123':
    senha = input('Entre com a senha correta: ')
print('Bem-Vindo ao sistema!')
