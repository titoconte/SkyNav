import streamlit as st
from utils.google_sheets import *
from utils import google_sheets as gs

def inserir_agencia():
    st.subheader("Inserir Informações da Agência")
    nome_agencia = st.text_input("Nome da Agência", key="nome_agencia")
    telegram_agencia = st.text_input("Telegram", key="telegram_agencia")
    balcao_agencia = st.text_input("Balcão", key="balcao_agencia")
    telefone_agencia = st.text_input("Telefone", key="telefone_agencia")
    instagram_agencia = st.text_input("Instagram", key="instagram_agencia")
    email_agencia = st.text_input("Email", key="email_agencia")
    cidade_agencia = st.text_input("Cidade", key="cidade_agencia")
    mastermiles_agencia = st.text_input("MasterMiles", key="mastermiles_agencia")
    qtde_milhas_agencia = st.text_input("Quantidade de Milhas", key="qtde_milhas_agencia")
    preco_agencia = st.text_input("Preço", key="preco_agencia")
    taxas_agencia = st.text_input("Taxas", key="taxas_agencia")
    total_agencia = st.text_input("Total", key="total_agencia")
    
    if st.button("Salvar"):
        # Logic to save agency information to Google Sheets
        if nome_agencia and telegram_agencia and balcao_agencia and telefone_agencia and instagram_agencia and email_agencia and cidade_agencia and mastermiles_agencia and qtde_milhas_agencia and preco_agencia and taxas_agencia and total_agencia:
            values =[[nome_agencia, telegram_agencia, balcao_agencia, telefone_agencia, instagram_agencia, email_agencia, cidade_agencia, mastermiles_agencia, qtde_milhas_agencia, preco_agencia, taxas_agencia, total_agencia]]
            gs.insert_data_row_sheet('Agencias',values)
            st.success("Agência inserida com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

def alterar_agencia():
    st.subheader("Consultar e Alterar Informações da Agência")
    df_all = gs.read_sheet('Agencias')
    nomes_agencia = df_all['Nome'].values  # Replace with dynamic fetching of agency names
    alter_nome_agencia = st.selectbox("Nome da Milheiro", nomes_agencia, key="alter_nome_agencia")
    
    if st.button("Buscar"):
        df = df_all.query('Nome == @alter_nome_agencia')
        alter_id_agencia = df['Número Milheiro'].values[0]
        n = df.index+1
        alter_telegram_agencia = st.text_input("Telegram", value=df['Telegram'].values[0], key="alter_telegram_agencia")
        alter_balcao_agencia = st.text_input("Balcão", value=df['Balcão'].values[0], key="alter_balcao_agencia")
        alter_telefone_agencia = st.text_input("Telefone", value=df['Telefone'].values[0], key="alter_telefone_agencia")
        alter_instagram_agencia = st.text_input("Instagram", value=df['Instagram'].values[0], key="alter_instagram_agencia")
        alter_email_agencia = st.text_input("Email", value=df['Email'].values[0], key="alter_email_agencia")
        alter_cidade_agencia = st.text_input("Cidade", value=df['Cidade'].values[0], key="alter_cidade_agencia")
        alter_mastermiles_agencia = st.text_input("MasterMiles", value=df['MasterMiles'].values[0], key="alter_mastermiles_agencia")
        alter_qtde_milhas_agencia = st.text_input("Quantidade de Milhas", value=df['qtde milhas'].values[0], key="alter_qtde_milhas_agencia")
        alter_preco_agencia = st.text_input("Preço", value=df['preco'].values[0], key="alter_preco_agencia")
        alter_taxas_agencia = st.text_input("Taxas", value=df['taxas'].values[0], key="alter_taxas_agencia")
        alter_total_agencia = st.text_input("Total", value=df['total'].values[0], key="alter_total_agencia")
            
        if st.button("Atualizar"):
            # Logic to update agency information in Google Sheets
            gs.update_row_sheet('Agencias', n, [alter_nome_agencia,alter_id_agencia,alter_telegram_agencia, alter_balcao_agencia, alter_telefone_agencia, alter_instagram_agencia, alter_email_agencia, alter_cidade_agencia, alter_mastermiles_agencia, alter_qtde_milhas_agencia, alter_preco_agencia, alter_taxas_agencia, alter_total_agencia])
            st.success("Agência atualizada com sucesso!")
    else:
        st.warning("Agência não encontrada.")

def agencia_screen():
    st.title("Controle de Agências")
    tab1, tab2 = st.tabs(["Inserir", "Consultar e Alterar"])
    with tab1:
        inserir_agencia()
    with tab2:
        alterar_agencia()

