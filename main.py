## IMPORTAÇÃO DO MÓDULO E CONFIGURAÇÕES

import pandas as pd

pd.options.mode.chained_assignment = None

## VARIÁVEIS GERAIS

aviso = 'Baixar todas as importações do Brasíndice em https://assinantes.brasindice.com.br/ \n Marcar somente as' \
        'opções a seguir: \n Código \n Descrição \n PMC \n PFAB \n TISS \n TUSS \n'

exit = 0

print(aviso)

versao = int(input("Qual a versão da Brasíndice será importada? "))

colunas_ordenadas = ['PROFAT', 'CÓD. LAB.', 'LABORATÓRIO', 'CÓD. PROD.', 'PRODUTO', 'CÓD. APRES.',
                     'PMC INT.', 'PF INT.', 'QTDE. EMB.',
                      'PMC UNIT.', 'PF UNIT.', 'EDIÇÃO', 'TISS', 'TUSS']

colunas_raw = ["CÓD. LAB.", "LABORATÓRIO", "CÓD. PROD.", "A", "CÓD. APRES.",
           "B", "PMC INT.", "PF INT.", "QTDE. EMB.", "C", "PMC UNIT.",
           "D", "PF UNIT.", "EDIÇÃO", "E", "F", "TISS", "TUSS"]

## MEDICAMENTOS

df = pd.read_csv("Medicamentos - TXT D Brasíndice Edição {}.txt".format(versao), names=colunas_raw,
                 encoding='windows-1252')

df['PRODUTO'] = df['A'].map(str)+" "+df['B'].map(str)

df.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df['PROFAT'] = df['TUSS']

df = df[colunas_ordenadas]

df2 = df.loc[df['PROFAT'].isna()]

df2['PROFAT'] = df2['TISS']

df.dropna(subset=['PROFAT'], inplace = True)

df = pd.concat([df, df2], axis = 0)

## CONVÊNIOS ONCOLÓGICOS

df_co = pd.read_csv("Convênios Oncológicos - TXT D Brasíndice Edição {}.txt".format(versao), names=colunas_raw,
                    encoding='windows-1252')

df_co['PRODUTO'] = df_co['A'].map(str)+' '+df_co['B'].map(str)

df_co.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df_co['PROFAT'] = df_co['TUSS']

df_co = df_co[colunas_ordenadas]

df_co2 = df_co.loc[df['PROFAT'].isna()]

df_co2['PROFAT'] = df_co2['TISS']

df_co.dropna(subset=['PROFAT'], inplace = True)

df_co = pd.concat([df_co, df_co2], axis = 0)

## SOLUÇÕES PARENTERAIS

df_sp = pd.read_csv('Soluções Parenterais - TXT D Brasíndice Edição {}.txt'.format(versao), names=colunas_raw,
                    encoding='windows-1252')

df_sp['PRODUTO'] = df_sp['A'].map(str)+' '+df_sp['B'].map(str)

df_sp.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df_sp['PROFAT'] = df_sp['TUSS']

df_sp = df_sp[colunas_ordenadas]

df_sp2 = df_sp.loc[df['PROFAT'].isna()]

df_sp2['PROFAT'] = df_co2['TISS']

df_sp.dropna(subset=['PROFAT'], inplace = True)

df_sp = pd.concat([df_sp, df_sp2], axis = 0 )

## MATERIAIS, DIETAS E OUTROS

df_mdo = pd.read_csv('Materiais Dietas e Outros - TXT D Brasíndice Edição {}.txt'.format(versao), names=colunas_raw,
                     encoding='windows-1252')

df_mdo['PRODUTO'] = df_mdo['A'].map(str)+' '+df_mdo['B'].map(str)

df_mdo.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df_mdo['PROFAT'] = df_mdo['TUSS']

df_mdo = df_mdo[colunas_ordenadas]

df_mdo2 = df_mdo.loc[df['PROFAT'].isna()]

df_mdo2['PROFAT'] = df_mdo2['TISS']

df_mdo.dropna(subset=['PROFAT'], inplace = True)

df_mdo = pd.concat([df_mdo, df_mdo2], axis = 0)

## DIETAS E NUTRIÇÃO

df_dn = pd.read_csv('Dietas e Nutrição - TXT D Brasíndice Edição {}.txt'.format(versao), names=colunas_raw,
                    encoding='windows-1252')

df_dn['PRODUTO'] = df_dn['A'].map(str)+' '+df_dn['B'].map(str)

df_dn.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df_dn['PROFAT'] = df_dn['TISS']

df_dn = df_dn[colunas_ordenadas]

df_dn2 = df_dn.loc[df['PROFAT'].isna()]

df_dn2['PROFAT'] = df_dn2['TUSS']

df_dn.dropna(subset=['PROFAT'], inplace = True)

df_dn = pd.concat([df_dn, df_dn2], axis = 0)

## OUTROS FÁRMACOS

df_of = pd.read_csv('Outros Fármacos - TXT D Brasíndice Edição {}.txt'.format(versao), names=colunas_raw,
                    encoding='windows-1252')

df_of['PRODUTO'] = df_of['A'].map(str)+' '+df_of['B'].map(str)

df_of.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df_of['PROFAT'] = df_of['TISS']

df_of = df_of[colunas_ordenadas]

df_of2 = df_of.loc[df['PROFAT'].isna()]

df_of2['PROFAT'] = df_of2['TUSS']

df_of.dropna(subset=['PROFAT'], inplace = True)

df_of = pd.concat([df_of, df_of2], axis = 0)

## MATERIAIS E INSUMOS

df_mi = pd.read_csv('Materiais e Insumos - TXT D Brasíndice Edição {}.txt'.format(versao), names=colunas_raw,
                    encoding='windows-1252')

df_mi['PRODUTO'] = df_mi['A'].map(str)+' '+df_mi['B'].map(str)

df_mi.drop(columns=['A', 'B', 'C', 'D', 'E', 'F'], inplace=True)

df_mi['PROFAT'] = df_mi['TISS']

df_mi = df_mi[colunas_ordenadas]

df_mi2 = df_mi.loc[df['PROFAT'].isna()]

df_mi2['PROFAT'] = df_mi2['TUSS']

df_mi.dropna(subset=['PROFAT'], inplace = True)

df_mi = pd.concat([df_mi, df_mi2], axis = 0)

## CONSTRUÇÃO DA BASE DE DADOS

df_bd = pd.concat([df, df_co, df_sp, df_mdo, df_mi, df_dn, df_of], axis = 0)

## REMOVENDO DUPLICATAS

df_bd.drop_duplicates(subset=['PROFAT'], inplace = True)

## GERANDO BASE DE DADOS XLSX

df_bd = df_bd.set_index(['PROFAT'])

nome = "Base de Cadastros - Edição {}.xlsx".format(versao)

df_bd.to_excel(nome)

print("A Base de Cadastros da Edição {} foi gerada com sucesso! \n".format(versao))

while exit == 0:
    exit = int(input("Pressione 1 e Enter para terminar o programa!\n"))