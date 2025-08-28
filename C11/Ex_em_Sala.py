import numpy as np
#Questao 1
ds = np.loadtxt('paises.csv',
                delimiter =';',
                dtype=str,
                encoding='utf-8')
print(ds[0,:4])
#Questao 2
regiao = ds[0:,1]
unique_regiao = np.unique(regiao)
print(unique_regiao)
#Question 3
ds_cost = ds[1:,9]
ds_cost = ds_cost.astype(float)
median = np.mean(ds_cost)
print(median)
#Questao 4
north_ds = np.sum(np.char.find(ds, 'NORTHERN AMERICA') != -1)
print(north_ds)
#Questa 5
rendas = ds[0:,9]
region = ds[0:,1]
america_index = np.where(region == 'LATIN AMER. & CARIB    ')
rendas_america = rendas[america_index]
local = ds[0:,0]
contry = local[america_index]
maiorRenda = np.argmax(rendas_america)
print(contry[maiorRenda])
