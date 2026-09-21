import pandas as pd

df = pd.read_csv(r"C:\Users\andre\OneDrive\Desktop\Projeto DATA\banco de dados\datatran2023.csv", sep = ';', encoding = 'latin1')

print('Primeiras Linhas')
print(df.head())

---

print('Dimensão da base')
print(df.shape)

---

print('Colunas')
print(df.columns.tolist())

---

print('Tipos de dados')
print(df.dtypes)

---

print('Valores nulos')
print(df.isnull().sum())

---

print('Informações gerais')
df.info()

#Inspeção básica - 01
