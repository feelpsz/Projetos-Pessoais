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

