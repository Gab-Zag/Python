#Criando um NUMPY Array 2D
import numpy as np
mtz = np.arange(1,10,1).reshape(3,3)
print(mtz)
#Extraindo Apenas Uma linha (Terceira Linha)
print(mtz[2])
#Extraindo Apenas Uma Coluna (Segunda e Terceira Coluna)
print(mtz[:,1:])
#Condicionais no NUMPY ARRAY
print(mtz>5)
print(mtz[mtz>5])
print(mtz[mtz%2==0])
#Tratamento Textual (Supacote CHAR)
#Sempre que retornar o indice maior ou igual a 0 existe
arr = np.array(['Goku','Goten','Gohan','Trunks','Bulma'])
print(arr)
print(np.char.find(arr,'Go'))
print(np.char.find(arr,'ha'))
print(np.char.find(arr,'Go')>=0)
arr = np.char.upper(arr)
print(arr[np.char.find(arr,'GO')>=0])
#Importando DATASETS No NUMPY
ds = np.loadtxt('space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')
print(ds)
#Colunas do DATASET
print(ds[0, :])
#Calculando a media de uma missao espacial
#Slicing para extrair a coluna (Cost)
ds_cost = ds[1:,6]
#Transformando os valores em FLOAT
ds_cost = ds_cost.astype(float)
#Calculando a media
print(ds_cost.mean())