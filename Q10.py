'''Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame? '''

import pandas as pd

df = pd.read_csv('seu-arquivo.csv')

#Idenficar valores ausentes
df.isna()

#Remover linhas ou colunas com valores ausentes
remover_colunas = df.dropna() 
remover_linhas = df.dropna(axis=1)

#Preencher valores ausentes com um valor especifico
preencher_valores = df.fillna(1)

#Preencher valores ausentes com media
df ['coluna_exemplo'].fillna(df['coluna_exemplo'].mean(), inplace=True)

#Caso os valores ausentes sejam do tipo String, pode-se também substituir-los por uma string especifica
df['coluna_exemplo'].fillna('Jujuba', inplace=True)