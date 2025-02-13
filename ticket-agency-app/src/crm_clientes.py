import streamlit as st
from utils.google_sheets import *

# Initialize Google Sheets utility
# gs = GoogleSheets()

def insert_client_info():
    st.subheader("Inserir Informações Cadastrais de um Cliente")
    instagram = ''
    name = st.text_input("Nome do Cliente")
    birth_date = st.date_input("Data de Nascimento")
    cpf = st.text_input("CPF")
    email = st.text_input("Email do Cliente")
    phone = st.text_input("Telefone do Cliente")
    instagram = st.text_input("Instagram")
    city = st.text_input("Cidade")
    address = st.text_input("Endereço")
    rg = st.text_input("RG")
    passport = st.text_input("Passaporte")
    passport_expiry_date = st.date_input("Data de Validade do Passaporte")
    
    if st.button("Salvar"):
        if name and birth_date and cpf and email and phone and instagram and city and address and rg and passport and passport_expiry_date:
            # gs.insert_client_data(name, birth_date, cpf, email, phone, instagram, city, address, rg, passport, passport_expiry_date)
            st.success("Informações do cliente inseridas com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

def consult_client():
    st.subheader("Consulta do Cliente")
    search_option = st.radio("Pesquisar por", ["Nome", "CPF"])
    if search_option == "Nome":
        client_name = st.text_input("Nome do Cliente", key="client_name")
    else:
        client_cpf = st.text_input("CPF do Cliente", key="client_cpf")
    
    if st.button("Consultar"):
        if client_name or client_cpf:
            # client_data = gs.get_client_data(client_id)
            client_data= True
            if client_data:
                st.write(client_data)
            else:
                st.error("Cliente não encontrado.")
        else:
            st.error("Por favor, insira o nome ou cpf do cliente.")

def alter_client_info():
    st.subheader("Alteração de Informação Cadastral")
    sel_client_name = st.text_input("Nome do Cliente", key="sel_client_name")
    new_birth_date = st.date_input("Nova Data de Nascimento")
    new_cpf = st.text_input("Novo CPF")
    new_email = st.text_input("Novo Email")
    new_phone = st.text_input("Novo Telefone")
    new_instagram = st.text_input("Novo Instagram")
    new_city = st.text_input("Nova Cidade")
    new_address = st.text_input("Novo Endereço")
    new_rg = st.text_input("Novo RG")
    new_passport = st.text_input("Novo Passaporte")
    new_passport_expiry_date = st.date_input("Nova Data de Validade do Passaporte")
    
    if st.button("Alterar"):
        if sel_client_name and (new_birth_date or new_cpf or new_email or new_phone or new_instagram or new_city or new_address or new_rg or new_passport or new_passport_expiry_date):
            # gs.update_client_data(client_name, new_birth_date, new_cpf, new_email, new_phone, new_instagram, new_city, new_address, new_rg, new_passport, new_passport_expiry_date)
            st.success("Informações do cliente alteradas com sucesso!")
        else:
            st.error("Por favor, preencha o nome do cliente e pelo menos um campo a ser alterado.")

def crm_clientes():
    st.title("CRM Clientes")
    tab1, tab2, tab3 = st.tabs(["Inserir", "Consultar", "Alterar"])
    
    with tab1:
        insert_client_info()
    
    with tab2:
        consult_client()
    
    with tab3:
        alter_client_info()