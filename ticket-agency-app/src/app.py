import streamlit as st
from crm_clientes import crm_clientes
from milheiros import milheiros_screen
from agencias import agencia_screen
from controle_compras import controle_compras
from controle_vendas import controle_vendas_screen
from controle_emissoes import controle_emissoes
from fluxo_caixa import fluxo_caixa
from match_margens import match_margens_report
from projecao_financeira import projecao_financeira
from calculadoras import calculadoras_screen

def main():
    st.title("Agência de Emissão de Passagens")
    
    menu = ["CRM Clientes", "Milheiros", "Agências", "Controle de Compras", 
            "Controle de Vendas", "Controle de Emissões de Voos", 
            "Controle do Fluxo de Caixa", "Match de Margens", 
            "Projeção Financeira", "Calculadoras"]
    
    choice = st.sidebar.radio("Selecione uma Tela", menu)

    if choice == "CRM Clientes":
        crm_clientes()
    elif choice == "Milheiros":
        milheiros_screen()
    elif choice == "Agências":
        agencia_screen()
    elif choice == "Controle de Compras":
        controle_compras()
    elif choice == "Controle de Vendas":
        controle_vendas_screen()
    elif choice == "Controle de Emissões de Voos":
        controle_emissoes()
    elif choice == "Controle do Fluxo de Caixa":
        fluxo_caixa()
    elif choice == "Match de Margens":
        match_margens_report()
    elif choice == "Projeção Financeira":
        projecao_financeira()
    elif choice == "Calculadoras":
        calculadoras_screen()

if __name__ == "__main__":
    main()