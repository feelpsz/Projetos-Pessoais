## IMPORTAÇÃO DO MÓDULO E CONFIGURAÇÕES

import pandas as pd

pd.options.mode.chained_assignment = None

## VARIÁVEIS GERAIS

versao = int(input("Qual a versão da Brasíndice será importada? "))

colunas_ordenadas = ['PROFAT', 'CÓD. LAB.', 'LABORATÓRIO', 'CÓD. PROD.', 'PRODUTO', 'CÓD. APRES.', 'PMC INT.', 'PF INT.', 'QTDE. EMB.',
                      'PMC UNIT.', 'PF UNIT.', 'EDIÇÃO', 'TISS', 'TUSS']

colunas_raw = ["CÓD. LAB.", "LABORATÓRIO", "CÓD. PROD.", "A", "CÓD. APRES.",
           "B", "PMC INT.", "PF INT.", "QTDE. EMB.", "C", "PMC UNIT.",
           "D", "PF UNIT.", "EDIÇÃO", "E", "F", "TISS", "TUSS"]

## MEDICAMENTOS

df = pd.read_csv("Medicamentos - TXT D Brasíndice Edição {}.txt".format(versao), names=colunas_raw, encoding='windows-1252')

df['PRODUTO'] = df['A'].map(str)+" "+df['B'].map(str)

df.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df['PROFAT'] = df['TUSS']

df = df[colunas_ordenadas]

df2 = df.loc[df['PROFAT'].isna()]

df2['PROFAT'] = df2['TISS']

df.dropna(subset=['PROFAT'], inplace = True)

df = pd.concat([df, df2], axis = 0)