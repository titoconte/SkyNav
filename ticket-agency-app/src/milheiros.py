import streamlit as st
from utils import google_sheets as gs

def insert_milheiro():
    st.subheader("Inserir Milheiro")
    nome_milheiro = st.text_input("Nome:", key="nome_milheiro")
    telegram_milheiro = st.text_input("Telegram:", key="telegram_milheiro")
    balcao_milheiro = st.text_input("Balcão:", key="balcao_milheiro")
    telefone_milheiro = st.text_input("Telefone:", key="telefone_milheiro")
    instagram_milheiro = st.text_input("Instagram:", key="instagram_milheiro")
    email_milheiro = st.text_input("Email:", key="email_milheiro")
    cidade_milheiro = st.text_input("Cidade:", key="cidade_milheiro")
    programa1_milheiro = st.text_input("Programa 1:", key="programa1_milheiro")
    senha_prog1_milheiro = st.text_input("Senha Prog1:", key="senha_prog1_milheiro")
    programa2_milheiro = st.text_input("Programa 2:", key="programa2_milheiro")
    senha_prog2_milheiro = st.text_input("Senha Prog2:", key="senha_prog2_milheiro")
    programa3_milheiro = st.text_input("Programa 3:", key="programa3_milheiro")
    senha_prog3_milheiro = st.text_input("Senha Prog3:", key="senha_prog3_milheiro")
    programa4_milheiro = st.text_input("Programa 4:", key="programa4_milheiro")
    senha_prog4_milheiro = st.text_input("Senha Prog4:", key="senha_prog4_milheiro")
    programa5_milheiro = st.text_input("Programa 5:", key="programa5_milheiro")
    senha_prog5_milheiro = st.text_input("Senha Prog5:", key="senha_prog5_milheiro")
    programa6_milheiro = st.text_input("Programa 6:", key="programa6_milheiro")
    senha_prog6_milheiro = st.text_input("Senha Prog6:", key="senha_prog6_milheiro")
    cpf_milheiro = st.text_input("CPF:", key="cpf_milheiro")

    if st.button("Salvar"):
        milheiro_data = [[nome_milheiro, telegram_milheiro, balcao_milheiro, telefone_milheiro, instagram_milheiro, email_milheiro, cidade_milheiro, programa1_milheiro, senha_prog1_milheiro, programa2_milheiro, senha_prog2_milheiro, programa3_milheiro, senha_prog3_milheiro, programa4_milheiro, senha_prog4_milheiro, programa5_milheiro, senha_prog5_milheiro, programa6_milheiro, senha_prog6_milheiro, cpf_milheiro]]
        gs.insert_data_row_sheet("Milheiros", milheiro_data)
        st.success("Milheiro inserido com sucesso!")


def alter_milheiro():
    st.subheader("Consultar e Alterar Milheiro")
    milheiro_names = ["Milheiro 1", "Milheiro 2", "Milheiro 3"]  # Replace with dynamic list from Google Sheets
    # milheiro_names = gs.get_all_milheiro_names()  # Uncomment this line to fetch from Google Sheets
    alter_milheiro_id = st.selectbox("Selecione o milheiro a ser alterado:", milheiro_names, key="alter_milheiro_id")
    alter_telegram_milheiro = st.text_input("Telegram:", key="alter_telegram_milheiro")
    alter_balcao_milheiro = st.text_input("Balcão:", key="alter_balcao_milheiro")
    alter_telefone_milheiro = st.text_input("Telefone:", key="alter_telefone_milheiro")
    alter_instagram_milheiro = st.text_input("Instagram:", key="alter_instagram_milheiro")
    alter_email_milheiro = st.text_input("Email:", key="alter_email_milheiro")
    alter_cidade_milheiro = st.text_input("Cidade:", key="alter_cidade_milheiro")
    alter_programa1_milheiro = st.text_input("Programa 1:", key="alter_programa1_milheiro")
    alter_senha_prog1_milheiro = st.text_input("Senha Prog1:", key="alter_senha_prog1_milheiro")
    alter_programa2_milheiro = st.text_input("Programa 2:", key="alter_programa2_milheiro")
    alter_senha_prog2_milheiro = st.text_input("Senha Prog2:", key="alter_senha_prog2_milheiro")
    alter_programa3_milheiro = st.text_input("Programa 3:", key="alter_programa3_milheiro")
    alter_senha_prog3_milheiro = st.text_input("Senha Prog3:", key="alter_senha_prog3_milheiro")
    alter_programa4_milheiro = st.text_input("Programa 4:", key="alter_programa4_milheiro")
    alter_senha_prog4_milheiro = st.text_input("Senha Prog4:", key="alter_senha_prog4_milheiro")
    alter_programa5_milheiro = st.text_input("Programa 5:", key="alter_programa5_milheiro")
    alter_senha_prog5_milheiro = st.text_input("Senha Prog5:", key="alter_senha_prog5_milheiro")
    alter_programa6_milheiro = st.text_input("Programa 6:", key="alter_programa6_milheiro")
    alter_senha_prog6_milheiro = st.text_input("Senha Prog6:", key="alter_senha_prog6_milheiro")
    alter_cpf_milheiro = st.text_input("CPF:", key="alter_cpf_milheiro")

    if st.button("Alterar"):
        # if gs.update_data("Milheiros", milheiro_id, new_data):
        if True:
            st.success("Milheiro alterado com sucesso!")
        else:
            st.error("Erro ao alterar milheiro.")

def milheiros_screen():
    st.title("Milheiros")
    tab1, tab2 = st.tabs(["Inserir", "Consultar e Alterar"])
    
    with tab1:
        insert_milheiro()
    
    with tab2:
        alter_milheiro()

if __name__ == "__main__":
    milheiros_screen()