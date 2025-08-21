import numpy as np
import random

# 1
arr1 = np.ones(8, dtype=int)
arr2 = np.random.randint(0, 10, 8)
arr3 = arr1 + arr2
if arr3.sum() >= 40:
    arr3 = arr3.reshape(4, 2)
else:
    arr3 = arr3.reshape(2, 4)
print(arr3)

# 2
a = np.arange(0, 52, 2)
b = np.arange(100, 49, -2)
c = np.concatenate((a, b))
print(np.sort(c))

# 3
mat = np.zeros((2, 2), dtype=int)
x, y = random.randint(0, 1), random.randint(0, 1)
mat[x, y] = 1
tentativas = 0
while tentativas < 3:
    i, j = map(int, input("Digite linha e coluna (0 ou 1): ").split())
    tentativas += 1
    if mat[i, j] == 1:
        print("Game Over! :( Try Again!")
        break
    if tentativas == 3:
        print("Congratulations! You beat the game! :)")

# 4
M = np.random.randint(1, 10, (3, 5))
linhas, colunas = M.shape
total = linhas * colunas
print("Par" if total % 2 == 0 else "Ímpar")

# 5
np.random.seed(10)
M = np.random.randint(1, 51, (4, 4))
print(M.mean(axis=1))
print(M.mean(axis=0))
print(max(M.mean(axis=1)))
print(max(M.mean(axis=0)))
valores, contagens = np.unique(M, return_counts=True)
print(dict(zip(valores, contagens)))
print(valores[contagens == 2])

import pandas as pd

df = pd.read_csv("missions.csv")

# 1
print((df["MissionStatus"] == "Success").mean() * 100)

# 2
print(df.loc[df["Cost"] > 0, "Cost"].mean())

# 3
print((df["Country"] == "USA").sum())

# 4
print(df[df["Company"] == "SpaceX"].loc[df["Cost"].idxmax()])

# 5
empresas = df["Company"].value_counts()
for empresa, qtd in empresas.items():
    print(empresa, qtd)
