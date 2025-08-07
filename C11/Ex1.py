import random
import math

# Questao 1
nome = input('Qual o seu nome? ')

print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome.count(' '))
partes = nome.split()
if len(partes) > 1:
    partes[-1] = "do Inatel"
    novo_nome = " ".join(partes)
else:
    novo_nome = nome + " do Inatel"
print("Nome com 'do Inatel':", novo_nome)

# Questao 2
numero = int(input('Digite o numero para ver a tabuada: '))

inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intevalo: '))

print(f'\nTabuada do {numero} de {inicio} ate {fim}:\n')

for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# Questao 3
sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
    if sexo == 'F':
        print('Mulher')
    elif sexo == 'M':
        print('Homem')
    else:
        print('Sexo Invalido')
# Questao 4
km = float(input('Qual a distancia que ira viajar: '))
if km <= 200:
    gastos = km * 0.50
else:
    gastos = km * 0.45
print(f'o Gasto foi de R${gastos}')
# Questao 5
number = random.randint(1000, 9999)
number_to_sring = str(number)

print(number)
print('Unidade:',number_to_sring[3])
print('Dezena:',number_to_sring[2])
print('Centena:',number_to_sring[1])
print('Milhar:',number_to_sring[0])

#Questao 6
number = float(input('Digite um numero decimal: '))
numberint = int(number)
print('Raiz: ', math.sqrt(number))
print('Teto: ', math.ceil(number))
print('Chao: ', math.floor(number))
print('Sua parte inteira: ', numberint)
