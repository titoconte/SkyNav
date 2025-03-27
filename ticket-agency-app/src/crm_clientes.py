import streamlit as st
from utils import google_sheets as gs

# Initialize Google Sheets utility
# gs = GoogleSheets()

def insert_client_info():
    st.subheader("Inserir Informações Cadastrais de um Cliente")
    crm_instagram = ''
    crm_name = st.text_input("Nome do Cliente", key="crm_name")
    crm_birth_date = st.date_input("Data de Nascimento", key="crm_birth_date")
    crm_cpf = st.text_input("CPF", key="crm_cpf")
    crm_email = st.text_input("Email do Cliente", key="crm_email")
    crm_phone = st.text_input("Telefone do Cliente", key="crm_phone")
    crm_instagram = st.text_input("Instagram", key="crm_instagram")
    crm_city = st.text_input("Cidade", key="crm_city")
    crm_address = st.text_input("Endereço", key="crm_address")
    crm_rg = st.text_input("RG", key="crm_rg")
    crm_passport = st.text_input("Passaporte", key="crm_passport")
    crm_passport_expiry_date = st.date_input("Data de Validade do Passaporte", key="crm_passport_expiry_date")
    
    if st.button("Salvar"):
        if crm_name and crm_birth_date and crm_cpf and crm_email and crm_phone and crm_instagram and crm_city and crm_address and crm_rg and crm_passport and crm_passport_expiry_date:
            client_code = len(gs.read_sheet('CRM Clientes')['Número Cliente'].values) + 1
            client_code = f"P{client_code}"
            values = [[
                client_code,
                crm_name, 
                str(crm_birth_date), 
                crm_cpf, 
                crm_email, 
                crm_phone, 
                crm_instagram, 
                crm_city, 
                crm_address, 
                crm_rg, 
                crm_passport, 
                str(crm_passport_expiry_date)
                ]]
            gs.insert_data_row_sheet('CRM Clientes', values)
            st.success("Informações do cliente inseridas com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

def alter_client_info():
    st.subheader("Consulta e Alteração de Informação Cadastral")
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
    tab1, tab2 = st.tabs(["Inserir", "Consultar e Alterar"])
    
    with tab1:
        insert_client_info()
    
    with tab2:
        alter_client_info()