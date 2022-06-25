#%%
import os
import glob

import pandas as pd

#%%

# Insira o caminho da pasta com o dado dos aposentados
dir_path = r'./dataset/Datasets/Aposentados 2021'
files = glob.glob(dir_path + "/*.csv")
cols = ['Nome',
        'CPF',
        'Matrícula do Servidor',
        'Nome do órgão',
        'Sigla do órgão',
        'Código do órgão superior',
        'Cargo',
        'Classe',
        'Padrão', 
        'Referência',
        'Nível',
        'Tipo de Aposentadoria',
        'Fundamentação da inatividade',
        'Nome Diploma Legal',
        'Data publicação do Diploma Legal',
        'Ocorrência de ingresso no serviço público',
        'Data de ocorrência de ingresso no serviço público',
        'Rendimento líquido'
        ]
df = []
for file in files:
    df.append(
        pd.read_csv(
            file, header=None, names=cols, encoding='Latin1',
            sep=';', on_bad_lines = 'skip'
        )
    )

df_ap = pd.concat(df) 
df_ap.head()# %%

#%%

# Insira o caminho da pasta com o dado dos abonos
dir_path = r'./dataset/Datasets/Abono 2021'
files = glob.glob(dir_path + "/*.csv")

df = []
for file in files:
    read_csv = pd.read_csv(
        file, encoding='Latin1', sep=';', index_col=False,
    )
    
    df.append(read_csv)
    
df_abono = pd.concat(df)
df_abono = df_abono[df_abono['Nome'] != 'Nome']

print(df_abono.head())
# %%
anos_ab = ['2017', '2018', '2019', '2020']
df_abonos = []
for i in range(0,4):
    dir =  r'./dataset/Datasets/Abono{}'.format(anos_ab[i])
    files = glob.glob(dir + "/*.csv")
    df = []
    dfs = []
    for i in range(len(files)):
        df.append(pd.read_csv(files[i], encoding='Latin1',sep=';', index_col=False, on_bad_lines = 'skip'))
    dfs = pd.concat(df)
    dfs = dfs[dfs['Nome'] != 'Nome']
    df_abonos.append(dfs)