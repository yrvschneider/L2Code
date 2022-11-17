
# Instalar o Pandas.

import pandas as pd

arquivo_excel_1 = pd.read_excel('Tabela_PESSOAS.xlsx') # Importsando arquivo em excel
arquivo_excel_2 = pd.read_excel('Tabela_CONTRATOS.xlsx') # Importsando arquivo em excel
arquivo_excel_3 = pd.read_excel('Tabela_PAGAMENTOS.xlsx') # Importsando arquivo em excel

# Juntando os arquivos e comparando as informações dos IDS para alinhas as informações entre as tabelas
mg_clientes = pd.merge(arquivo_excel_1, arquivo_excel_3, left_on='CONTRATO_ID', right_on='PESSOA_ID') 
mg_clientes2 = pd.merge(arquivo_excel_2, mg_clientes,  left_on='ID', right_on='CONTRATO_ID')
mg_clientes2.to_excel('db_organizado.xlsx') # Exportando o arquivo completo
organizado_excel = pd.read_excel('db_organizado.xlsx') # Importando o arquivo completo

#                              CODIGO PARA OS INADIPLENTES

inadimplente_sim = organizado_excel.loc[organizado_excel['INADIMPLENTE'] == 'S'] # Irá pegar somente as linhas que tem a informação 'S' na coluna 'INADIMPLENTE'
devedores = inadimplente_sim.drop(columns=['Unnamed: 0','ID','ID_x','CONTRATO_ID','INADIMPLENTE','DT_COMPLETO','ID_y','PESSOA_ID', 'PARCELAS']) # Removendo colunas desnecessárias
devedores['DIA_MES'] = devedores['DT_PAGAMENTO'].dt.day # Pegando somente o dia da coluna 'DT_PAGAMENTO' e criando uma nova coluna 'DIA_MES'
devedores = devedores[['NOME','DIA_MES', 'VALOR_PARCELA']] # Organizando colunas
print(''''
                INADIPLENTES
    
{}
'''.format(devedores)) # Imprimindo da tela as informações
devedores.to_excel('inadimplentes.xlsx') # Exportando resultado em excel

#                           CODIGO PARA PAGAMENTOS COMPLETOS

inadimplente_nao = organizado_excel.loc[organizado_excel['INADIMPLENTE']=='N'] # Irá pegar somente as linhas que tem a informação 'N' na coluna 'INADIMPLENTE'
ct_pago1 = inadimplente_nao.drop(columns=['Unnamed: 0','ID','ID_x','CONTRATO_ID','INADIMPLENTE','DT_COMPLETO','ID_y','PESSOA_ID','DT_PAGAMENTO']) # Removendo colunas desnecessárias
ct_pago1 = ct_pago1[['NOME', 'VALOR_PARCELA','PARCELAS']] # Organizando colunas
ct_pago1['VALOR_TOTAL'] = ct_pago1['VALOR_PARCELA'] * ct_pago1['PARCELAS'] # Criando uma nova coluna 'VALOR_TOTAL' e ira receber a multiplicação entre as colunas 'VALOR_PARCELA' * 'PARCELAS'
saida_pagos = ct_pago1.drop(columns=['VALOR_PARCELA', 'PARCELAS']) # Removendo colunas desnecessárias
print('''

                PAGAMENTO COMPLETO

{}
'''.format(saida_pagos)) # Imprimindo da tela as informações
saida_pagos.to_excel('Pagamento completo.xlsx') # Exportando resultado em excel