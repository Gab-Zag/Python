#Questao 1
lista = ['Liverpool', 'Barcelona', 'Arsenal', 'Inter de Milao', 'Atletico de Madrid']
lista_ordenada = sorted(lista)
elemento = 'Barcelona'
indice = lista.index(elemento)
print(lista[:3])
print(lista[3:])
print(lista[:])
print(lista_ordenada)
if elemento in lista:
    print(f'O elemento {elemento} esta na lista e se encontra no indice: {indice}')

#Questao 2
loja1 = {'Iphone 14', 'Iphone 15', 'Iphone 16', 'Samsung z fold'}
loja2 = {'Samsung z fold', 'Samsung s25', 'Samsung tab s10', 'Iphone 16'}
print(f'Caso queira nos visitar possuimos um total de {len(loja1) + len(loja2)} em nossas lojas')
print(f'Os modelos sao {loja1} na nossa loja do centro e {loja2} na nossa loja no bairro do inatel')
print(f'lembrando que os modelos {loja1.intersection(loja2)} possuimos nas duas lojas')

#Questao 3
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))
aluno = {
    "nome": nome,
    "media": media
}
if media >= 50:
    aluno["situacao"] = "AP"
else:
    aluno["situacao"] = "RP"

print('Dados do aluno:')
print(aluno)

#Questao 4
menor = 999
maior = -999
pessoamaisleve = ''
pessoamaispesada = ''
for c in range (1,4):
    nome = input(f'Digite o nome do {c}º pessoa: ')
    peso = float(input(f'Digite o peso do {nome}: '))
    if peso < menor:
        menor = peso
        pessoamaisleve = nome
    if peso > maior:
        maior = peso
        pessoamaispesada = nome
print(f'A pessoa mais leve e {pessoamaisleve}')
print(f'A pessoa mais pesada e {pessoamaispesada}')

#Questao 5
pessoas = []

n = int(input("Quantas pessoas deseja cadastrar? "))

for _ in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    pessoa = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo
    }

    pessoas.append(pessoa)

soma_idades = sum(p["idade"] for p in pessoas)
media_idade = soma_idades / len(pessoas)

mulheres_menos_20 = sum(1 for p in pessoas if p["sexo"] == "F" and p["idade"] < 20)

print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")