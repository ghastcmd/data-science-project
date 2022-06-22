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
        'Data_diploma_legal',
        'Ocorrência de ingresso no serviço público',
        'Data_ingresso_serv_publico',
        'Rendimento_liq'
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