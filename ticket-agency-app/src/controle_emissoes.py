import streamlit as st
from utils.google_sheets import *

# Initialize Google Sheets utility
# gs = GoogleSheets()

def controle_emissoes():
    st.title("Controle de Emissões de Voos")

    # Aba 1 - Status das emissões ainda não concluídas
    if st.sidebar.radio("Selecione uma aba", ["Status das emissões", "Inserir informações", "Consultar emissões", "Alterar informações"]) == "Status das emissões":
        # status_emissoes = gs.read_data("Emissoes", "Status")  # Assuming "Emissoes" is the sheet name and "Status" is the tab
        # st.write(status_emissoes)
        st.sucess('Foi')

    # Aba 2 - Inserir informações cadastrais de um cliente
    elif st.sidebar.radio("Selecione uma aba", ["Status das emissões", "Inserir informações", "Consultar emissões", "Alterar informações"]) == "Inserir informações":
        cliente_nome = st.text_input("Nome do Cliente")
        voo_data = st.date_input("Data do Voo")
        if st.button("Inserir"):
            # gs.insert_data("Emissoes", [cliente_nome, voo_data])  # Adjust according to your data structure
            st.success("Informações inseridas com sucesso!")

    # Aba 3 - Consultar emissões
    elif st.sidebar.radio("Selecione uma aba", ["Status das emissões", "Inserir informações", "Consultar emissões", "Alterar informações"]) == "Consultar emissões":
        cliente_nome = st.text_input("Nome do Cliente para consulta")
        if st.button("Consultar"):
            # emissao_info = gs.read_data("Emissoes", "Consulta", cliente_nome)  # Adjust according to your data structure
            # st.write(emissao_info)
            st.sucess("foi")

    # Aba 4 - Alterar informações cadastrais
    elif st.sidebar.radio("Selecione uma aba", ["Status das emissões", "Inserir informações", "Consultar emissões", "Alterar informações"]) == "Alterar informações":
        cliente_nome = st.text_input("Nome do Cliente para alteração")
        nova_data = st.date_input("Nova Data do Voo")
        if st.button("Alterar"):
            # gs.update_data("Emissoes", cliente_nome, nova_data)  # Adjust according to your data structure
            st.success("Informações alteradas com sucesso!")

if __name__ == "__main__":
    controle_emissoes()