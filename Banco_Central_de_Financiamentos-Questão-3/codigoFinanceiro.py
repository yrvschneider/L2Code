import pandas as pd

arquivo_excel_1 = pd.read_excel('Tabela_PESSOAS.xlsx')
arquivo_excel_2 = pd.read_excel('Tabela_CONTRATOS.xlsx')
arquivo_excel_3 = pd.read_excel('Tabela_PAGAMENTOS.xlsx')

mg_clientes = pd.merge(arquivo_excel_1, arquivo_excel_3, left_on='CONTRATO_ID', right_on='PESSOA_ID')
mg_clientes2 = pd.merge(arquivo_excel_2, mg_clientes,  left_on='ID', right_on='CONTRATO_ID')
mg_clientes2.to_excel('db_organizado.xlsx')
organizado_excel = pd.read_excel('db_organizado.xlsx')

#                              CODIGO PARA OS INADIPLENTES

inadimplente_sim = organizado_excel.loc[organizado_excel['INADIMPLENTE'] == 'S']
devedores = inadimplente_sim.drop(columns=['Unnamed: 0','ID','ID_x','CONTRATO_ID','INADIMPLENTE','DT_COMPLETO','ID_y','PESSOA_ID', 'PARCELAS'])
devedores['DIA_MES'] = devedores['DT_PAGAMENTO'].dt.day
devedores = devedores[['NOME','DIA_MES', 'VALOR_PARCELA']]
print(''''
                INADIPLENTES
    
{}
'''.format(devedores))
devedores.to_excel('inadimplentes.xlsx')

#                           CODIGO PARA PAGAMENTOS COMPLETOS

inadimplente_nao = organizado_excel.loc[organizado_excel['INADIMPLENTE']=='N']
ct_pago1 = inadimplente_nao.drop(columns=['Unnamed: 0','ID','ID_x','CONTRATO_ID','INADIMPLENTE','DT_COMPLETO','ID_y','PESSOA_ID','DT_PAGAMENTO'])
ct_pago1 = ct_pago1[['NOME', 'VALOR_PARCELA','PARCELAS']]
ct_pago1['VALOR_TOTAL'] = ct_pago1['VALOR_PARCELA'] * ct_pago1['PARCELAS']
saida_pagos = ct_pago1.drop(columns=['VALOR_PARCELA', 'PARCELAS'])
print('''

                PAGAMENTO COMPLETO

{}
'''.format(saida_pagos))
saida_pagos.to_excel('Pagamento completo.xlsx')