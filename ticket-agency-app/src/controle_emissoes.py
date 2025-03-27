import streamlit as st
from utils.google_sheets import *
from utils import google_sheets as gs


# Initialize Google Sheets utility
# gs = GoogleSheets()

def controle_emissoes():
    st.title("Controle de Emissões de Voos")
    df_vendas = gs.read_sheet('Controle de Vendas')
    df_compras = gs.read_sheet('Controle de Compras')
    df = df_vendas.merge(df_compras, left_on='Lastro', right_on='Numero Compra')
    numero_venda_emissao_dados = df['Numero Venda'].values

    numero_venda_emissao = st.selectbox("Número Venda", numero_venda_emissao_dados, key="numero_venda_emissao")
    data_emissao = st.date_input("Data da Emissão", key="data_emissao")
    cod_reserva_emissao = st.text_input("Código de Reserva", key="cod_reserva_emissao")
    nu_compra_emissao = st.text_input("Número da Compra", key="nu_compra_emissao")

    if st.button("Salvar"):
        # Logic to save agency information to Google Sheets
        if numero_venda_emissao and data_emissao and cod_reserva_emissao and nu_compra_emissao:
            data = df.loc[df['Numero Venda'] == numero_venda_emissao,['Cliente','Número Cliente','Programa','Qtde milhas','Número Milheiro']]
            cliente_emissao = data['Cliente'].values[0]
            numero_cliente_emissao = data['Número Cliente'].values[0]
            programa_emissao = data['Programa'].values[0]
            qtd_milhas_emissao = data['Qtde milhas'].values[0]
            numero_milheiro_emissao = data['Número Milheiro'].values[0]

            values=[[
                str(cliente_emissao),
                str(numero_cliente_emissao), 
                str(numero_venda_emissao),
                data_emissao.strftime('%d/%m/%y'), 
                str(cod_reserva_emissao), 
                str(nu_compra_emissao), 
                str(programa_emissao),
                str(qtd_milhas_emissao),
                str(numero_milheiro_emissao)
                ]]
            gs.insert_data_row_sheet('Controle de Emissões',values)
            st.success("Emissao de Passagem inserida com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
    

if __name__ == "__main__":
    controle_emissoes()