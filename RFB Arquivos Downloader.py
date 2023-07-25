import os
import requests as rqst
def baixar(url, endereco):
    r= rqst.get(url)
    if r.status_code == rqst.codes.OK:
        with open(endereco, 'wb') as n_a:
            n_a.write(r.content)
        print(f"Donwload finalizado. Salvo em: {endereco}")
    else:
        r.raise_for_status()
def pasta(pstnm):
    if(not os.path.exists(pstnm)):
        os.mkdir(pstnm)
def RFB(aqvf):
    #Empresas
    print(f"-=-=-={aqvf}=-=-=-")
    pst=aqvf
    pasta(pst)
    for x in range(0,10):
        ende=f'{pst}/{aqvf}{x}.zip'
        baixar(f'http://200.152.38.155/CNPJ/{aqvf}{x}.zip',ende)
def cpl():
    pst='Complementos'
    pasta(pst)
    baixar('http://200.152.38.155/CNPJ/Simples.zip',f'{pst}/Simples.zip')
    baixar('http://200.152.38.155/CNPJ/Cnaes.zip', f'{pst}/Cnaes.zip')
    baixar('http://200.152.38.155/CNPJ/Motivos.zip', f'{pst}/Motivos.zip')
    baixar('http://200.152.38.155/CNPJ/Municipios.zip', f'{pst}/Municipios.zip')
    baixar('http://200.152.38.155/CNPJ/Naturezas.zip', f'{pst}/Naturezas.zip')
    baixar('http://200.152.38.155/CNPJ/Paises.zip', f'{pst}/Paises.zip')
    baixar('http://200.152.38.155/CNPJ/Qualificacoes.zip', f'{pst}/Qualificacoes.zip')
    baixar('http://200.152.38.155/CNPJ/anual/Dados%20Abertos%20S%c3%adtio%20RFB%20Extracao%2020.10.2021.zip', f'{pst}/Dados Abertos Sítio RFB Extracao 20.10.2021.zip')
RFB('Empresas')
RFB('Estabelecimentos')
RFB('Socios')
cpl()