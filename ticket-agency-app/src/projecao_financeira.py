# Projeção Financeira Screen

import streamlit as st

def projecao_financeira():
    st.title("Projeção Financeira")
    
    st.subheader("Insira os dados para projeção")
    
    # Inputs for financial projection
    receita = st.number_input("Receita Mensal", min_value=0.0, format="%.2f")
    despesas = st.number_input("Despesas Mensais", min_value=0.0, format="%.2f")
    meses = st.number_input("Número de Meses para Projeção", min_value=1, max_value=60, value=12)
    
    if st.button("Calcular Projeção"):
        lucro = receita - despesas
        projecoes = [lucro * i for i in range(1, meses + 1)]
        
        st.write("Projeção de Lucro Mensal:")
        for i, valor in enumerate(projecoes, start=1):
            st.write(f"Mês {i}: R$ {valor:.2f}")

if __name__ == "__main__":
    projecao_financeira()