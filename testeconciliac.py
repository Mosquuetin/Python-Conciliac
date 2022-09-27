import pandas as pd
import numpy as np

arquivo = r"C:\Users\ELDAN\Desktop\Inputs\LC - 26.09.2022 - BB 1 pix BR.Fernandes.xlsx"

dfpainel = pd.read_excel(arquivo, sheet_name="Base Painel", na_filter=False)
dfextrato = pd.read_excel(arquivo, sheet_name="Base Extrato", na_filter=False)

cpfs = list(dfpainel['Input CPF'])
datas = list(dfpainel['Input\nDATA'])
valores = list(dfpainel['Input\nBRL'])
invoices = list(dfpainel['Input\nID'])
dfsaida = pd.DataFrame()
listaduplicadas = list()
x = 0
print('Iniciando Conciliac')
for invoice in invoices:
    idconciliada = str(x + 1)
    idtotal = str(len(invoices))
    print('Conciliando ID '+idconciliada+' de '+ idtotal)
    data = datas[x]
    valor = valores[x]
    cpf = cpfs[x]
    dflinhapainel = dfpainel[dfpainel['Input\nID'] == invoice]
    dflinhapainelfinal = pd.DataFrame()
    dflinhapainelfinal = pd.concat([dflinhapainelfinal,dflinhapainel], ignore_index=True)
    dfcheck = dfextrato[dfextrato['INFO CONCILIAR 2'] == cpf]
    dfcheckfinal = pd.DataFrame()
    dfcheckfinal = pd.concat([dfcheckfinal,dfcheck], ignore_index=True)
    datacheck = list(dfcheckfinal['DATA'])
    valorcheck = list(dfcheckfinal['VALOR'])
    if  len(dfcheckfinal.index) == 1:
        if data == datacheck[0] and valor == valorcheck[0]:
            dfauxiliar = pd.DataFrame()
            dfauxiliar = pd.concat([dfcheckfinal, dflinhapainelfinal], axis=1)
            dfauxiliar.insert(0,'Comentários', value = '')
            dfauxiliar.insert(0,'Diferença', value = 0)
            dfauxiliar.insert(0,'ID Regra', value = 1)
            dfauxiliar.insert(0,'ID Registro', value = 'BBPixTestePerfeitoUnico')
            dfauxiliar.insert(0,'Info', value = 'Conciliado')
            if dfsaida.empty:
                dfsaida = dfauxiliar 
            else:
                dfsaida = pd.concat([dfsaida,dfauxiliar])
        else:
            dfauxiliar = pd.DataFrame()
            dfauxiliar.insert(0,'IDENTIFICADOR LINHA', value = '')
            dfauxiliar.insert(0,'Detalhe', value = '')
            dfauxiliar.insert(0,'DOCTO CLIENTE', value = '')
            dfauxiliar.insert(0,'AGENCIA', value = '')
            dfauxiliar.insert(0,'CONTA', value = '')
            dfauxiliar.insert(0,'NOME', value = '')
            dfauxiliar.insert(0,'SALDO', value = '')
            dfauxiliar.insert(0,'VALOR', value = '')
            dfauxiliar.insert(0,'DESCRIÇÃO', value = '')
            dfauxiliar.insert(0,'DATA', value = '')
            dfauxiliar.insert(0,'INFO CONCILIAR 2', value = '')
            dfauxiliar.insert(0,'INFO CONCILIAR 1', value = '')
            dfauxiliar = pd.concat([dfauxiliar, dflinhapainelfinal], axis=1) 
            dfauxiliar.insert(0,'Comentários', value = '')
            dfauxiliar.insert(0,'Diferença', value = 0)
            dfauxiliar.insert(0,'ID Regra', value = 0)
            dfauxiliar.insert(0,'ID Registro', value = 'BBPixTesteErroUnico')
            dfauxiliar.insert(0,'Info', value = 'Pendente')
            if dfsaida.empty:
                dfsaida = dfauxiliar 
            else:
                dfsaida = pd.concat([dfsaida,dfauxiliar])  
    else:
        y = 0
        z = 0
        idlinhas = list(dfcheck['IDENTIFICADOR LINHA'])
        if len(idlinhas) > 0:
            for idlinha in idlinhas:
                idlinha = idlinhas[y]
                y = y + 1
                if idlinha in listaduplicadas:
                    pass
                else:
                    dfcheckfinal = dfcheck[dfcheck['IDENTIFICADOR LINHA'] == idlinha]
                    dfauxiliar = pd.DataFrame()
                    dfcheckfinal = pd.concat([dfcheckfinal,dfauxiliar], ignore_index=True)
                    datacheck = list(dfcheckfinal['DATA'])
                    valorcheck = list(dfcheckfinal['VALOR'])
                    if data == datacheck[0] and valor == valorcheck[0]:
                        listaduplicadas.append(idlinha)
                        dfauxiliar = pd.DataFrame()
                        dfauxiliar = pd.concat([dfcheckfinal, dflinhapainelfinal], axis=1)
                        dfauxiliar.insert(0,'Comentários', value = '')
                        dfauxiliar.insert(0,'Diferença', value = 0)
                        dfauxiliar.insert(0,'ID Regra', value = 1)
                        dfauxiliar.insert(0,'ID Registro', value = 'BBPixTestePerfeitoS' + str(x + 1))
                        dfauxiliar.insert(0,'Info', value = 'Conciliado')
                        if dfsaida.empty:
                            dfsaida = dfauxiliar 
                        else:
                            dfsaida = pd.concat([dfsaida,dfauxiliar])
                        z = 1
                        break
                    else:
                        pass 
            if z == 0:
                dfauxiliar = pd.DataFrame()
                dfauxiliar.insert(0,'IDENTIFICADOR LINHA', value = '')
                dfauxiliar.insert(0,'Detalhe', value = '')
                dfauxiliar.insert(0,'DOCTO CLIENTE', value = '')
                dfauxiliar.insert(0,'AGENCIA', value = '')
                dfauxiliar.insert(0,'CONTA', value = '')
                dfauxiliar.insert(0,'NOME', value = '')
                dfauxiliar.insert(0,'SALDO', value = '')
                dfauxiliar.insert(0,'VALOR', value = '')
                dfauxiliar.insert(0,'DESCRIÇÃO', value = '')
                dfauxiliar.insert(0,'DATA', value = '')
                dfauxiliar.insert(0,'INFO CONCILIAR 2', value = '')
                dfauxiliar.insert(0,'INFO CONCILIAR 1', value = '')
                dfauxiliar = pd.concat([dfauxiliar, dflinhapainelfinal], axis=1)
                dfauxiliar.insert(0,'Comentários', value = '')
                dfauxiliar.insert(0,'Diferença', value = 0)
                dfauxiliar.insert(0,'ID Regra', value = 0)
                dfauxiliar.insert(0,'ID Registro', value = 'BBPixTesteSemRecebimento' + str(x + 1))
                dfauxiliar.insert(0,'Info', value = 'Pendente')
                if dfsaida.empty:
                    dfsaida = dfauxiliar 
                else:
                    dfsaida = pd.concat([dfsaida,dfauxiliar]) 
            else:
                pass 
        else:
            dfauxiliar = pd.DataFrame()
            dfauxiliar.insert(0,'IDENTIFICADOR LINHA', value = '')
            dfauxiliar.insert(0,'Detalhe', value = '')
            dfauxiliar.insert(0,'DOCTO CLIENTE', value = '')
            dfauxiliar.insert(0,'AGENCIA', value = '')
            dfauxiliar.insert(0,'CONTA', value = '')
            dfauxiliar.insert(0,'NOME', value = '')
            dfauxiliar.insert(0,'SALDO', value = '')
            dfauxiliar.insert(0,'VALOR', value = '')
            dfauxiliar.insert(0,'DESCRIÇÃO', value = '')
            dfauxiliar.insert(0,'DATA', value = '')
            dfauxiliar.insert(0,'INFO CONCILIAR 2', value = '')
            dfauxiliar.insert(0,'INFO CONCILIAR 1', value = '')
            dfauxiliar = pd.concat([dfauxiliar, dflinhapainelfinal], axis=1)
            dfauxiliar.insert(0,'Comentários', value = '')
            dfauxiliar.insert(0,'Diferença', value = 0)
            dfauxiliar.insert(0,'ID Regra', value = 0)
            dfauxiliar.insert(0,'ID Registro', value = 'BBPixTesteSemRecebimento' + str(x + 1))
            dfauxiliar.insert(0,'Info', value = 'Pendente')
            if dfsaida.empty:
                dfsaida = dfauxiliar 
            else:
                dfsaida = pd.concat([dfsaida,dfauxiliar]) 
    x = x + 1
dfsaida.to_excel(r"C:\Users\ELDAN\Desktop\LC - 26.09.2022 - BB 1 pix BR.FernandesTeste.xlsx", index = False)
print('Salvando Arquivo')
