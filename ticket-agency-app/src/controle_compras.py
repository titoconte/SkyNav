import streamlit as st
from utils.google_sheets import *
from utils import google_sheets as gs

def controle_compras():
    st.subheader("Controle de Compras")
    # ler aba de milheiros na coluna numero milheiro coletar todos os códigos e exibir em lista suspensa
    milheiro_code = gs.read_sheet('Milheiros')['Número Milheiro'].values
    numero_milheiro_compra = st.selectbox("Número Milheiro", milheiro_code, key="numero_milheiro_compra")
    quantidade_milhas_compra = st.text_input("Quantidade de Milhas", key="quantidade_milhas_compra")
    programa_compra = st.text_input("Programa", key="programa_compra")
    preco_1k_milhas_compra = st.text_input("Preço por 1k Milhas", key="preco_1k_milhas_compra")
    qtd_emissoes_compra = st.text_input("Quantidade de Emissões", key="qtd_emissoes_compra")
    saldo_utilizado_compra = st.text_input("Saldo Utilizado", key="saldo_utilizado_compra")
    saldo_remanescente_compra = st.text_input("Saldo Remanescente", key="saldo_remanescente_compra")
    valor_total_compra = st.text_input("Valor Total", key="valor_total_compra")
    # data_compra = st.text_input("Data da Compra", key="data_compra")
    taxa_compra = st.text_input("Taxa", key="taxa_compra")
    valor_total_pix_compra = st.text_input("Valor Total PIX", key="valor_total_pix_compra")
    pix_enviado_compra = st.text_input("PIX Enviado", key="pix_enviado_compra")

    if st.button("Salvar"):
        # Logic to save agency information to Google Sheets
        if numero_milheiro_compra and quantidade_milhas_compra and programa_compra and preco_1k_milhas_compra and qtd_emissoes_compra and saldo_utilizado_compra and saldo_remanescente_compra and valor_total_compra  and taxa_compra and valor_total_pix_compra and pix_enviado_compra:
            compra_code = len(gs.read_sheet('Controle de Compras')['Numero Compra'].values) + 1
            compra_code = f"C{compra_code}"
            values=[[compra_code,numero_milheiro_compra, quantidade_milhas_compra, programa_compra, preco_1k_milhas_compra, qtd_emissoes_compra, saldo_utilizado_compra, saldo_remanescente_compra, valor_total_compra, taxa_compra, valor_total_pix_compra, pix_enviado_compra]]
            gs.insert_data_row_sheet('Controle de Compras',values)
            st.success("Compra inserida com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")