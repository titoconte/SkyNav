import streamlit as st

def fluxo_caixa():
    st.title("Controle do Fluxo de Caixa")
    
    # Aqui você pode adicionar a lógica para exibir o relatório de fluxo de caixa
    st.write("Este é o relatório de fluxo de caixa.")
    
    # Exemplo de dados fictícios
    dados_fluxo_caixa = {
        "Data": ["01/01/2023", "02/01/2023", "03/01/2023"],
        "Descrição": ["Venda A", "Venda B", "Compra C"],
        "Valor": [1000, 1500, -500]
    }
    
    # Exibir dados em uma tabela
    st.table(dados_fluxo_caixa)

if __name__ == "__main__":
    fluxo_caixa()