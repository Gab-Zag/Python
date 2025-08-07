# Exemplos com TUPLAS
# Tupla e uma colecao imutavel
tupla = ('Goku', 'Vegeta','Trunk','Gohan')
# Mostrando elementos
print(tupla)
# Slicing de Elementos (Fatiamento)
print(tupla[1:3])# Vegeta, Trunks, Primeiro valor inclusive segundo valor exclusive
print(tupla[2:])#Trunks, Gohan
print(tupla[-2])#Ele aceita valores negativos
#Funcoes pre-prontas de Python
print(len(tupla))
print(max(tupla))
print(min(tupla))
#Exemplos com LISTAS
#LISTAS sao Mutaveis
lista = ['Goku', 'Vegeta','Trunk','Gohan']
#Mostrando elementos da lista
print(lista)
#Inserindo Elementos
lista.append('Bulma')#Adiciona no final da lista
lista.insert(1,'Kuririn')#adciiona no indice desejado
print(lista)
#Alterando elementos
lista[0] = 'Piccolo'
print(lista)
#Excluindo Elementos
del lista[0]#removendo pelo indice
lista.remove('Bulma')
print(lista)
#Exemplos com CONJUNTOS
#Nao guarda a ordem dos elementos
#Conjuntos e Mutavel
#Ele nao permite elementos repetidos
#Mostrando os elementos
conjunto = {'Goku', 'Vegeta','Trunks','Gohan'}
print(conjunto)
#Adicionando Elementos
conjunto.add('Bulma')
conjunto.add('Goku')
print(conjunto)
#Removendo Elementos
conjunto.remove('Trunks')
#Checar o comando replace
#Como descobrir o tipo de algo em python
print(type(conjunto))
#Exemplos com DICIONARIOS
#Estrutura que tranbalha com chave e valor
#Dicionario trabalha com o key value
pessoa = {
          'nome':'Goku',
          'idade':43,
          'sexo':'masculino'
          }
print(pessoa)
#Adicionando no Dicionario
pessoa['raca'] = 'sayajin'
pessoa['familia'] = ['Gohan','Goten','Chichi','Pan']
print(pessoa)
#Update
pessoa['idade']=45
print(pessoa)
#Delete
del pessoa['sexo']
print(pessoa)
#Acessando a Chichi
print(pessoa['familia'][2])