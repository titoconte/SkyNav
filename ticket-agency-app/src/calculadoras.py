# Calculadoras Screen Implementation

import streamlit as st

def converter_milhas(milhas):
    # Função para converter milhas em outra unidade (exemplo: km)
    return milhas * 1.60934  # Conversão de milhas para quilômetros

def calcular_margem(valor_pago, valor_venda):
    # Função para calcular a margem de lucro
    return (valor_venda - valor_pago) / valor_venda * 100  # Retorna a margem em porcentagem

def calculadoras_screen():
    st.title("Calculadoras")

    # Aba 1 - Conversão de milhas
    st.header("Conversão de Milhas")
    milhas = st.number_input("Insira o valor em milhas:", min_value=0.0)
    if st.button("Converter"):
        km = converter_milhas(milhas)
        st.success(f"{milhas} milhas equivalem a {km:.2f} quilômetros.")

    # Aba 2 - Margem de voos pagos em moedas estrangeiras
    st.header("Margem de Voos Pagos em Moedas Estrangeiras")
    valor_pago = st.number_input("Valor pago:", min_value=0.0)
    valor_venda = st.number_input("Valor de venda:", min_value=0.0)
    if st.button("Calcular Margem"):
        margem = calcular_margem(valor_pago, valor_venda)
        st.success(f"A margem de lucro é de {margem:.2f}%.")

if __name__ == "__main__":
    main()