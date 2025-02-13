import streamlit as st
from utils.google_sheets import *

def controle_compras():
    st.title("Controle de Compras")

    # Aba 1 - Relatório de Compras
    if st.sidebar.radio("Selecione uma aba", ["Relatório de Compras", "Inserir Informações", "Consultar Compra", "Alterar Informação"]) == "Relatório de Compras":
        st.subheader("Relatório de Compras")
        # Aqui você pode adicionar a lógica para exibir o relatório de compras
        compras_data = read_data("compras")  # Função para ler dados da aba "compras"
        st.write(compras_data)

    # Aba 2 - Inserir Informações
    elif st.sidebar.radio("Selecione uma aba", ["Relatório de Compras", "Inserir Informações", "Consultar Compra", "Alterar Informação"]) == "Inserir Informações":
        st.subheader("Inserir Informações de Compras")
        # Campos para inserir informações de compras
        produto = st.text_input("Produto")
        quantidade = st.number_input("Quantidade", min_value=1)
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")

        if st.button("Inserir"):
            insert_data("compras", {"produto": produto, "quantidade": quantidade, "preco": preco})  # Função para inserir dados
            st.success("Informações inseridas com sucesso!")

    # Aba 3 - Consultar Compra
    elif st.sidebar.radio("Selecione uma aba", ["Relatório de Compras", "Inserir Informações", "Consultar Compra", "Alterar Informação"]) == "Consultar Compra":
        st.subheader("Consultar Compra")
        # Campo para consultar informações de compras
        produto_consulta = st.text_input("Produto para consulta")
        if st.button("Consultar"):
            compra_data = read_data("compras", query=produto_consulta)  # Função para ler dados com consulta
            st.write(compra_data)

    # Aba 4 - Alterar Informação
    elif st.sidebar.radio("Selecione uma aba", ["Relatório de Compras", "Inserir Informações", "Consultar Compra", "Alterar Informação"]) == "Alterar Informação":
        st.subheader("Alterar Informação de Compras")
        # Campos para alterar informações de compras
        produto_alterar = st.text_input("Produto a ser alterado")
        nova_quantidade = st.number_input("Nova Quantidade", min_value=1)
        novo_preco = st.number_input("Novo Preço", min_value=0.0, format="%.2f")

        if st.button("Alterar"):
            update_data("compras", produto_alterar, {"quantidade": nova_quantidade, "preco": novo_preco})  # Função para atualizar dados
            st.success("Informações alteradas com sucesso!")