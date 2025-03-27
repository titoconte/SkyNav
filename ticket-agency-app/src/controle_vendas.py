import streamlit as st
from utils.google_sheets import *
from utils import google_sheets as gs

def controle_vendas():
    st.subheader("Controle de Vendas")
    # ler aba de milheiros na coluna numero milheiro coletar todos os códigos e exibir em lista suspensa
    nomes = gs.read_sheet('CRM Clientes')['Nome'].values
    numero_cliente = gs.read_sheet('CRM Clientes')['Número Cliente'].values
    lastro = gs.read_sheet('Controle de Compras')['Numero Compra'].values
    nome_venda = st.selectbox("Cliente", nomes, key="nome_venda")
    categoria_venda = st.text_input("Categoria", key="categoria_venda")
    lastro_venda = st.selectbox("Lastro", lastro, key="lastro_venda")
    # data da venda
    data_venda = st.date_input("Data da Venda", key="data_venda")
    qtd_emissoes_venda = st.text_input("Quantidade de Emissões", key="qtd_emissoes_venda")
    valor_venda = st.text_input("Valor", key="valor_venda")
    qtd_milhas_venda = st.text_input("Quantidade de Milhas", key="qtd_milhas_venda")
    taxa_venda = st.text_input("Taxa", key="taxa_venda")    
    margem_venda = st.text_input("Margem", key="margem_venda")
    pix_enviado_venda = st.text_input("PIX Enviado", key="pix_enviado_venda")

    if st.button("Salvar"):
        # Logic to save agency information to Google Sheets
        if nome_venda and categoria_venda and lastro_venda and data_venda and qtd_emissoes_venda and valor_venda and qtd_milhas_venda  and taxa_venda and pix_enviado_venda:
            venda_code = len(gs.read_sheet('Controle de Vendas')['Numero Venda'].values) + 1
            valor_total_venda = float(valor_venda) * (float(qtd_milhas_venda))/1000
            total_plus_taxas_venda = valor_total_venda + float(taxa_venda) +float(margem_venda)
            numero_cliente_venda = numero_cliente[nomes==nome_venda]
            if len(numero_cliente_venda) >1:
                numero_cliente_venda = numero_cliente_venda[0]
            venda_code = f"V{venda_code}"
            values=[[
                str(venda_code),
                str(nome_venda), 
                str(numero_cliente_venda),
                str(categoria_venda), 
                str(lastro_venda), 
                data_venda.strftime('%d/%m/%y'), 
                str(qtd_emissoes_venda),
                str(valor_venda),
                str(qtd_milhas_venda),
                str(valor_total_venda),
                str(taxa_venda), 
                str(margem_venda),
                str(total_plus_taxas_venda),
                str(pix_enviado_venda)
                ]]
            gs.insert_data_row_sheet('Controle de Vendas',values)
            st.success("Venda inserida com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")