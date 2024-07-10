''' Utilizando pandas, como selecionar uma coluna específica e filtrar linhas
em um “DataFrame” com base em uma condição?'''

import pandas as pd

df = pd.read_csv('seu-arquivo.csv')

coluna_exemplo = df['nome da coluna'] #Selecionar uma coluna especifica

exibir_condicao = df[df['coluna_exemplo'] > 3] #Exibe uma linha de acordo com a condição desejada

coluna_exemplo #Mostra na tela a coluna selecionada

exibir_condicao #Exibe as linhas de acordo com a condição estabelecida