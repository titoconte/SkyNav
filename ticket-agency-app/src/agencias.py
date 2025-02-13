import streamlit as st
from utils.google_sheets import *

# Initialize Google Sheets utility
# gs = GoogleSheets()

def inserir_agencia():
    st.subheader("Inserir Informações da Agência")
    nome = st.text_input("Nome da Agência", key="nome")
    telegram = st.text_input("Telegram", key="telegram")
    balcao = st.text_input("Balcão", key="balcao")
    telefone = st.text_input("Telefone", key="telefone")
    instagram = st.text_input("Instagram", key="instagram")
    email = st.text_input("Email", key="email")
    cidade = st.text_input("Cidade", key="cidade")
    mastermiles = st.text_input("MasterMiles", key="mastermiles")
    qtde_milhas = st.text_input("Quantidade de Milhas", key="qtde_milhas")
    preco = st.text_input("Preço", key="preco")
    taxas = st.text_input("Taxas", key="taxas")
    total = st.text_input("Total", key="total")
    
    if st.button("Salvar"):
        # Logic to save agency information to Google Sheets
        # gs.inserir_agencia(nome, endereco, telefone)
        st.success("Agência inserida com sucesso!")

def consultar_agencia():
    st.subheader("Consultar Milheiro")
    nome = st.text_input("Nome da Milheiro")
    
    if st.button("Consultar"):
        # Logic to fetch agency information from Google Sheets
        agencia = True # gs.consultar_agencia(nome)
        if agencia:
            st.write(agencia)
        else:
            st.warning("Agência não encontrada.")

def alterar_agencia():
    st.subheader("Alterar Informações da Agência")
    nomes_milheiro = ["Agência 1", "Agência 2", "Agência 3"]  # Replace with dynamic fetching of agency names
    nome = st.selectbox("Nome da Milheiro", nomes_milheiro, key="alter_nome")
    telegram = st.text_input("Telegram", key="alter_telegram")
    balcao = st.text_input("Balcão", key="alter_balcao")
    telefone = st.text_input("Telefone", key="alter_telefone")
    instagram = st.text_input("Instagram", key="alter_instagram")
    email = st.text_input("Email", key="alter_email")
    cidade = st.text_input("Cidade", key="alter_cidade")
    mastermiles = st.text_input("MasterMiles", key="alter_mastermiles")
    qtde_milhas = st.text_input("Quantidade de Milhas", key="alter_qtde_milhas")
    preco = st.text_input("Preço", key="alter_preco")
    taxas = st.text_input("Taxas", key="alter_taxas")
    total = st.text_input("Total", key="alter_total")
    
    if st.button("Buscar"):
        # Logic to fetch agency information for editing
        agencia = True #gs.consultar_agencia(nome)
        if agencia:
            
            if st.button("Atualizar"):
                # Logic to update agency information in Google Sheets
                # gs.alterar_agencia(nome, novo_nome, novo_endereco, novo_telefone)
                st.success("Agência atualizada com sucesso!")
        else:
            st.warning("Agência não encontrada.")

def agencia_screen():
    st.title("Controle de Agências")
    tab1, tab2, tab3 = st.tabs(["Inserir", "Consultar", "Alterar"])
    with tab1:
        inserir_agencia()
    with tab2:
        consultar_agencia()
    with tab3:
        alterar_agencia()

