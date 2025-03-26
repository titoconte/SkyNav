import streamlit as st
from utils.google_sheets import *

# Initialize Google Sheets utility
# gs = GoogleSheets()

def insert_milheiro():
    st.subheader("Inserir Milheiro")
    nome = st.text_input("Nome:")
    telegram = st.text_input("Telegram:")
    balcao = st.text_input("Balcão:")
    telefone = st.text_input("Telefone:")
    instagram = st.text_input("Instagram:")
    email = st.text_input("Email:")
    cidade = st.text_input("Cidade:")
    programa1 = st.text_input("Programa 1:")
    senha_prog1 = st.text_input("Senha Prog1:")
    programa2 = st.text_input("Programa 2:")
    senha_prog2 = st.text_input("Senha Prog2:")
    programa3 = st.text_input("Programa 3:")
    senha_prog3 = st.text_input("Senha Prog3:")
    programa4 = st.text_input("Programa 4:")
    senha_prog4 = st.text_input("Senha Prog4:")
    programa5 = st.text_input("Programa 5:")
    senha_prog5 = st.text_input("Senha Prog5:")
    programa6 = st.text_input("Programa 6:")
    senha_prog6 = st.text_input("Senha Prog6:")
    cpf = st.text_input("CPF:")

    if st.button("Salvar"):
        # gs.insert_data_row_sheet("Milheiros", milheiro_data)
        st.success("Milheiro inserido com sucesso!")

def consult_milheiro():
    st.subheader("Consultar Milheiro")
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
                st.error("Milheiro não encontrado")
        else:
            st.error("Por favor, insira o nome ou cpf do milheiro.")

def alter_milheiro():
    st.subheader("Alterar Milheiro")
    milheiro_names = ["Milheiro 1", "Milheiro 2", "Milheiro 3"]  # Replace with dynamic list from Google Sheets
    # milheiro_names = gs.get_all_milheiro_names()  # Uncomment this line to fetch from Google Sheets
    milheiro_id = st.selectbox("Selecione o milheiro a ser alterado:", milheiro_names)
    telegram = st.text_input("Telegram:")
    balcao = st.text_input("Balcão:")
    telefone = st.text_input("Telefone:")
    instagram = st.text_input("Instagram:")
    email = st.text_input("Email:")
    cidade = st.text_input("Cidade:")
    programa1 = st.text_input("Programa 1:")
    senha_prog1 = st.text_input("Senha Prog1:")
    programa2 = st.text_input("Programa 2:")
    senha_prog2 = st.text_input("Senha Prog2:")
    programa3 = st.text_input("Programa 3:")
    senha_prog3 = st.text_input("Senha Prog3:")
    programa4 = st.text_input("Programa 4:")
    senha_prog4 = st.text_input("Senha Prog4:")
    programa5 = st.text_input("Programa 5:")
    senha_prog5 = st.text_input("Senha Prog5:")
    programa6 = st.text_input("Programa 6:")
    senha_prog6 = st.text_input("Senha Prog6:")
    cpf = st.text_input("CPF:")

    if st.button("Alterar"):
        # if gs.update_data("Milheiros", milheiro_id, new_data):
        if True:
            st.success("Milheiro alterado com sucesso!")
        else:
            st.error("Erro ao alterar milheiro.")

def milheiros_screen():
    st.title("Milheiros")
    tab1, tab2, tab3 = st.tabs(["Inserir", "Consultar", "Alterar"])
    
    with tab1:
        insert_milheiro()
    
    with tab2:
        consult_milheiro()
    
    with tab3:
        alter_milheiro()

if __name__ == "__main__":
    milheiros_screen()